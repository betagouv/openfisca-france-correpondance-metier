#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name = 'OpenFisca-France Correspondance métier',
    version = '0.1.0',
    author = 'Incubateur de services numériques',
    author_email = 'contact@beta.gouv.fr',
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        ],
    description = u"Outils d'interrogation d'OpenFisca-France à partir des données de systèmes d'informations métiers (CAF, CNAM, PE)",
    keywords = 'france microsimulation social tax',
    license = 'http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    url = 'https://github.com/betagouv/openfisca-france-correpondance-metier',
    install_requires = [
        'OpenFisca-France >= 24.0.0, < 25',
        ],
    )
