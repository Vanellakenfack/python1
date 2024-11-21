import random
import time

# Questions par catégorie
questions = {
    "science": {
        "Quelle est la formule chimique de l'eau ?": "H2O",
        "Quel est l'élément chimique avec le symbole O ?": "Oxygène",
    },
    "histoire": {
        "Qui a écrit 'De la démocratie en Amérique' ?": "Alexis de Tocqueville",
        "En quelle année a eu lieu la Révolution française ?": "1789",
    },
    "culture": {
        "Qui a peint la Mona Lisa ?": "Leonard de Vinci",
        "Quel est le plus grand océan du monde ?": "Pacifique",
    },
}

# Récompenses
recompenses = {
    3: "Bravo ! Vous êtes un expert !",
    5: "Impressionnant ! Vous devriez envisager de participer à un quiz !",
    7: "Génial ! Vous êtes un véritable champion !",
}

def choisir_categorie():
    print("Choisissez une catégorie :")
    for category in questions.keys():
        print(f"- {category}")
    choix = input("Votre choix : ")
    return choix if choix in questions else "science"

def poser_questions(categorie):
    score = 0
    bonnes_reponses_consecutives = 0
    nombre_de_vies = 3

    for question, reponse in questions[categorie].items():
        print("\n" + question)
        start_time = time.time()
        user_input = input("Votre réponse (ou tapez 'quit' pour quitter) : ")

        if user_input.lower() == 'quit':
            print("Merci d'avoir joué !")
            break

        elapsed_time = time.time() - start_time

        # Vérifier la réponse
        if user_input.strip().lower() == reponse.lower():
            print("Correct !")
            score += 1
            bonnes_reponses_consecutives += 1
            
            # Vérification des récompenses
            if bonnes_reponses_consecutives in recompenses:
                print(recompenses[bonnes_reponses_consecutives])
        else:
            print(f"Incorrect. La bonne réponse est {reponse}.")
            bonnes_reponses_consecutives = 0
            nombre_de_vies -= 1
            print(f"Vies restantes : {nombre_de_vies}")
        
        # Vérifier si l'utilisateur a perdu toutes ses vies
        if nombre_de_vies == 0:
            print("Vous avez perdu toutes vos vies. Fin du jeu.")
            break

    print(f"Votre score final est {score}/{len(questions[categorie])}.")

# Main
categorie_choisie = choisir_categorie()
poser_questions(categorie_choisie)