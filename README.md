# OpenFisca-France Correspondance métier

## Introduction

Ce dépôt consolide le travail de correspondance entre les données des systèmes d'informations et le modèle OpenFisca


## Installation

Pour utiliser ce module vous devez avoir installer OpenFisca-France sur votre machine.

L'installation de ce module peut être fait avec les commandes suivantes :
```bash
git clone https://github.com/betagouv/openfisca-france-correpondance-metier.git &&
cd openfisca-france-correpondance-metier &&
pip install --editable .
```

Pour vérifier l'installation vous pouvez laisser la commande `python openfisca_france_correpondance_metier/test.py` qui renvoie le message suivant : « L'installation s'est bien déroulée ! »

## Mise à jour

Ce module peut être mise à jour à partir des informations disponibles dans ce dépôt avec les commandes suivantes :
```bash
git checkout master &&
git fetch --all &&
git pull
```

Plus d'informations sur git et ses commandes sont disponibles sur https://git-scm.com/doc.

## Exemple

Une situation de test est mise à disposition dans le fichier `openfisca_france_correpondance_metier/example.py`. Elle peut être lancée avec la commande suivante `python openfisca_france_correpondance_metier/example.py`.

## Notes

Les noms des champs disponibles à la CAF ont été communiqués par email le 18/07/2018 à 15:44.
