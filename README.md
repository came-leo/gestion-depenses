# Gestionnaire de dépenses

Application Python en ligne de commande permettant de gérer ses dépenses personnelles.

## Fonctionnalités

- Ajouter une dépense
- Afficher les dépenses
- Attribuer un identifiant unique à chaque dépense
- Calculer le total des dépenses
- Calculer le total par catégorie
- Rechercher une dépense
- Modifier une dépense
- Supprimer une dépense
- Enregistrer les données dans un fichier JSON

## Structure du projet

```text
gestion-depenses/
|-- main.py
|-- depenses.py
|-- .gitignore
`-- README.md
```

## Technologies utilisées

- Python
- JSON
- Git
- GitHub

## Installation

Cloner le dépôt :

```bash
git clone git@github.com:came-leo/gestion-depenses.git
```

Entrer dans le dossier :

```bash
cd gestion-depenses
```

## Utilisation

Lancer le programme avec :

```bash
python main.py
```

Le programme affiche ensuite un menu permettant de gérer les dépenses.

## Stockage des données

Les dépenses sont enregistrées dans le fichier `depenses.json`.

Les données sont donc conservées lorsque le programme est fermé puis relancé.

## Objectif du projet

Ce projet a été réalisé dans le cadre de mon apprentissage de Python.

Il m'a permis de pratiquer :

- les variables
- les conditions
- les boucles
- les fonctions
- les listes et dictionnaires
- la gestion des erreurs
- la lecture et l'écriture de fichiers
- JSON
- la modularisation d'un programme
- Git et GitHub
