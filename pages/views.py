from django.shortcuts import render

def accueil(request):
	contexte = {
		"nom_projet": "BiblioLearn",
		"modules": ["Catalogue", "Comptes et rôles", "Emprunts", "Mini-cours"],
	}
	return render(request, "pages/accueil.html", contexte)