# -*- coding: utf-8 -*-

import caf_utils
import csv
import openfisca_france
from datetime import datetime
from openfisca_core.simulations import Simulation


import sys

from pprint import pprint

filename = './doc/Exemple CAF.csv'

if len(sys.argv) > 1:
  filename = sys.argv[len(sys.argv)-1]

legislation_francaise = openfisca_france.FranceTaxBenefitSystem()
with open(filename, 'r') as file:
  rows = csv.DictReader(file)
  for data in rows:
    period = datetime.strptime('2018-08-01', '%Y-%m-%d')
    situation = caf_utils.createSituation(data, period)
    pprint(situation)

    simulation_actuelle = Simulation(tax_benefit_system=legislation_francaise, simulation_json=situation)
    variable = 'af'

    periodText = period.strftime('%Y-%m')
    resultat = simulation_actuelle.calculate(variable, periodText)

    print('{0} - {1} : {2}'.format(variable, periodText, resultat))
    print('')
