recettes = {
    "omelette": ["oeufs", "sel", "poivre", "beurre"],
    "salade": ["laitue", "tomate", "concombre", "vinaigrette"],
}

def proposer_recette(ingredients):
    for recette, ing in recettes.items():
        if all(item in ingredients for item in ing):
            return f"Vous pouvez faire une {recette}."
    return "Aucune recette trouvée avec ces ingrédients."

ingredients = input("Quels ingrédients avez-vous ? (séparez par des virgules) ").split(", ")
resultat = proposer_recette(ingredients)
print(resultat)