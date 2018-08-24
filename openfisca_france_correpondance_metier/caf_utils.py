# -*- coding: utf-8 -*-
import csv

from pprint import pprint
import datetime

def id(data, fieldName):
  return fieldName + '-' + data[fieldName]


def getMainPerson(data):
  if 'NIRMME' in data and data['NIRMME']:
    return id(data, 'NIRMME'), {}
  if 'NIRMON' in data and data['NIRMON']:
    return id(data, 'NIRMON'), {}

  raise ValueError


def getSecondPerson(data):
  if not ('NIRMME' in data and data['NIRMME']):
    return None, None
  if 'NIRMON' in data and data['NIRMME']:
    return id(data, 'NIRMON'), {}

  return None, None


def getChildren(data, period):
  children = list()
  for index in range(1, 11):
    idField = 'nirenf' + str(index)
    if idField in data and data[idField]:
      child = {}

      dateField = 'dtenf' + str(index)
      if dateField in data and data[dateField]:
        dt = datetime.datetime.strptime(data[dateField], '%d/%m/%Y')
        child['date_naissance'] = { period.strftime('%Y-%m'): dt.strftime('%Y-%m-%d') }

      children.append((id(data,idField), child))

  return children

def createSituation(data, period):
  mainPersonId, mainPerson = getMainPerson(data)
  secondPersonId, secondPerson = getSecondPerson(data)

  individus = {
    mainPersonId: mainPerson
  }

  famille = {
    'parents': [mainPersonId],
    'enfants': []
  }

  menage = {
    'personne_de_reference': [mainPersonId],
    'conjoint': [],
    'enfants': []
  }

  foyerFiscal = {
    'declarants': [mainPersonId],
    'personnes_a_charge': []
  }

  rniField = 'MTRNIFOY'
  if rniField in data and data[rniField]:
    value = data[rniField]
    rev_coll = {(datetime.datetime(period.year - 2, period.month, period.day)).strftime('%Y'): value}
    foyerFiscal['rev_coll'] = rev_coll

  if secondPersonId:
    individus[secondPersonId] = secondPerson
    famille['parents'].append(secondPersonId)
    menage['conjoint'].append(secondPersonId)
    foyerFiscal['declarants'].append(secondPersonId)

  children = getChildren(data,period)
  for item in children:
    childId, child = item
    individus[childId] = child
    famille['enfants'].append(childId)
    menage['enfants'].append(childId)
    foyerFiscal['personnes_a_charge'].append(childId)

  situation = {
    'individus': individus,
    'foyers_fiscaux': {
      'ff': foyerFiscal
    },
    'familles': {
      'f': famille
    },
    'menages': {
      'm': menage
    }
  }

  return situation

