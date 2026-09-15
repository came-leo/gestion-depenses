from depenses import (
	ajouter_depense,
	afficher_depenses,
	calculer_total,
	total_par_catégorie,
	rechercher_depense,
	supprimer_depense,
	modifier_depense
)


def main():
	while True:
		print("\n=== GESTIONNAIRE DE DEPENSES ===")
		print("\n1. Ajouter une dépense")
		print("2. Afficher les dépenses")
		print("3. Calculer le total")
		print("4. Total par catégorie")
		print("5. Rechercher une dépense")
		print("6. Supprimer une note")
		print("7. modifier une depense")
		print("8. Quitter")

		choix = input("\nChoisir une option : ")

		if choix == "1":
			ajouter_depense()

		elif choix == "2":
			afficher_depenses()

		elif choix == "3":
			calculer_total()

		elif choix == "4":
			total_par_catégorie()

		elif choix == "5":
			rechercher_depense()

		elif choix == "6":
			supprimer_depense()

		elif choix == "7":
			modifier_depense()

		elif choix == "8":
			print("Au revoir !")
			break

		else:
			print("Choix invalide.")


if __name__ == "__main__":
	main()