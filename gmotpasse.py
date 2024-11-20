import random
lettre="ABCDEFGHIJKLMNOP"
nombre="123456789"
symboles="§$£%@#{}[]()"
caractere=lettre + lettre.lower()+nombre +symboles
caractere_no_symbols=lettre + lettre.lower() +nombre
while True:
    longueurmdp= int(input("entre la longueuur du mot de passe "))
    nombremdp=int(input("entrer le nombre de mot de passe "))
    caracteres_speciaux_ask=str(input("dois je mettre les caracteres speciaux"))
    if caracteres_speciaux_ask=='oui':
        for i in range(0,nombremdp):
            mdp=""
            for i in range (0,longueurmdp):
                cmdp=random.choice(caractere)
                mdp=mdp+cmdp 
                print("vtre mot de passe est ",mdp)
    elif caracteres_speciaux_ask=='non':
        for i in range(0,nombremdp):
            mdp=""
            for i in range (0,longueurmdp):
                cmdp=random.choice(caractere_no_symbols)
                mdp=mdp+cmdp
            print("vtre mot de passe est ",mdp)

    elif caracteres_speciaux_ask !='oui' or caracteres_speciaux_ask !='non':

     print( "ERREUR")