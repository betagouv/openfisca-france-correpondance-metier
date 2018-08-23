# -*- coding: utf-8 -*-

import openfisca_france
from openfisca_core.simulations import Simulation

situation = {
    "individus": {
        "parent_1": {}
    },
    "foyers_fiscaux": {
        "ff": {
            "declarants": ["parent_1"]
        }
    },
    "familles": {
        "f": {
            "parents": ["parent_1"]
        }
    },
    "menages": {
        "m": {
            "personne_de_reference": ["parent_1"]
        }
    }
}
legislation_francaise = openfisca_france.FranceTaxBenefitSystem()
simulation_actuelle = Simulation(tax_benefit_system=legislation_francaise, simulation_json=situation)

variable = "rsa"
period = "2018-08"

print("Cet exemple calcule la variable '" + variable + "' sur la période '" + period + "' dans le cas d'une personne isolée sans ressource.")
resultat = simulation_actuelle.calculate(variable, period)

print("Le résultat obtenu est " + str(resultat) + ".")
