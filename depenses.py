import json
from datetime import datetime

FICHIER = "depenses.json"


def lire_depenses():
	try:
		with open(FICHIER, "r") as fichier:
			return json.load(fichier)
	except FileNotFoundError:
		return []

	except json.JSONDecodeError:
		print("Erreur: le fichier depenses.json est invalide.")
		return []


def sauvegarder_depenses(depenses):
	with open(FICHIER, "w") as fichier:
		json.dump(depenses, fichier, indent=4)


def ajouter_depense():
	depenses = lire_depenses()

	description = input("Description : ").strip()

	if not description:
		print("La description ne peut pas être vide.")
		return

	try:
		montant = float(input("Montant : "))

		if montant <= 0:
			print("Le montant doit être supérieur à zéro")
			return

	except ValueError:
		print("Veuillez entrer un montant valide.")
		return

	categorie = input("Catégorie : ").strip()

	if not categorie:
		print("La catégorie ne peut pas être vide.")
		return

	if depenses:
		nouvel_id = max(depense.get("id", 0) for depense in depenses) + 1
	else:
		nouvel_id = 1

	nouvelle_depense = {
		"id": nouvel_id,
		"description": description,
		"montant": montant,
		"categorie": categorie,
		"date": datetime.now().strftime("%d/%m/%Y %H:%M")
	}

	depenses.append(nouvelle_depense)
	sauvegarder_depenses(depenses)

	print("Dépense ajoutée !")


def afficher_depenses():
	depenses = lire_depenses()

	if not depenses:
		print("Aucune dépense.")
		return

	print("\n== MES DEPENSES ==")

	for depense in depenses:
		identifiant = depense.get("id", "Sans ID")
		description = depense.get("description", "Sans description")
		montant = depense.get("montant", 0)
		categorie = depense.get("categorie", "Sans catégorie")
		date = depense.get("date","Date inconnue")

		print(f"\nID: {identifiant}")
		print(f"Description : {description}")
		print(f"Montant : {montant} FCFA")
		print(f"Catégorie : {categorie}")
		print(f"Date : {date}")


def calculer_total():
	depenses = lire_depenses()

	if not depenses:
		print("Aucune dépense.")
		return

	total = sum(depense.get("montant", 0) for depense in depenses)

	print(f"\nTotal des dépenses : {total} FCFA")


def total_par_catégorie():
	depenses = lire_depenses()

	if not depenses:
		print("Aucune dépense.")
		return []

	totaux = {}

	for depense in depenses:
		categorie = depense.get("categorie", "Sans catégorie")
		montant = depense.get("montant", 0)

		if categorie not in totaux:
			totaux[categorie] = 0

		totaux[categorie] += montant

	print("\n== TOTAL PAR CATEGORIE ==\n")

	for categorie, total in totaux.items():
		print(f"{categorie} : {total} FCFA")


def rechercher_depense():
	depenses = lire_depenses()

	if not depenses:
		print("Aucune dépense.")
		return

	recherche = input("Rechercher : ").strip().lower()

	if not recherche:
		print("La recherche ne peut pas être vide")
		return

	trouvee = False

	print("\n== RESULTAT DE LA RECHERCHE ==")

	for depense in depenses:
		description = depense.get("description", "").lower()
		categorie = depense.get("categorie", "").lower()

		if recherche in description or recherche in categorie:
			print(f"\nDescription : {depense.get('description', 'Sans description')}")
			print(f"Montant : {depense.get('montant', 0)} FCFA")
			print(f"Catégorie : {depense.get('categorie', 'Sans catégorie')}")
			print(f"Date : {depense.get('date', 'Date inconnue')}")

			trouvee = True

	if not trouvee:
		print("Aucune dépense trouvée.")


def supprimer_depense():
	depenses = lire_depenses()

	if not depenses:
		print("Aucune dépense.")
		return

	afficher_depenses()
	
	try:
		id_depense = int(input("\nID de la dépense à supprimer : "))

		for depense in depenses:
			if id_depense == depense.get("id"):
				confirmation = input(f"Supprimer << {depense['description']} >> ? (o/n) : ").strip().lower()

				if confirmation != "o":
					print("Suppression annulée.")
					return

				depenses.remove(depense)
				sauvegarder_depenses(depenses)

				print("Dépense supprimée.")
				return

		print("Aucune dépense avec cet ID.")

	except ValueError:
		print("Veuillez entrer un nombre")


def modifier_depense():
	depenses = lire_depenses()

	if not depenses:
		print("Aucune depense.")
		return

	afficher_depenses()

	try:
		id_depense = int(input("\nID de la dépense à modifier : "))

		for depense in depenses:
			if id_depense == depense.get("id"):
				nouvelle_description = input("Nouvelle description : ").strip()

				if not nouvelle_description:
					print("La description ne peut pas être vide.")
					return

				try:
					nouveau_montant = float(input("nouveau_montant : "))

					if nouveau_montant <= 0:
						print("Le montant doit être supérieur à zéro.")
						return

				except ValueError:
					print("Veuillez entrer un montant valide.")
					return

				nouvelle_categorie = input("Nouvelle catégorie : ").strip()

				if not nouvelle_categorie:
					print("La catégorie ne pas être vide.")
					return

				depense["description"] = nouvelle_description
				depense["montant"] = nouveau_montant
				depense["categorie"] = nouvelle_categorie
				depense["date"] = datetime.now().strftime("%d/%m/%Y %H:%M")

				sauvegarder_depenses(depenses)

				print("Dépense modifiée !")
				return

		print("Aucune dépense avec cet ID.")

	except ValueError:
		print("Veuillez entrer un nombre.")