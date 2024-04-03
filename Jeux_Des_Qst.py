import random
import time

nbr_partie_joué = 0
bonne_reponse = 0

def pourcent():
    
    gages = [
    "Faire 10 pompes.",
    "Faire 20 sauts en place.",
    "Faire un compliment à la personne à sa gauche.",
    "Raconter une blague drôle.",
    "Faire une grimace amusante.",
    "Écrire un petit poème sur le thème de la nature.",
    "Faire une danse de quelques secondes.",
    "Faire un câlin à quelqu'un.",
    "Dire 'je t'aime' à un membre de la famille.",
    "Imiter un animal pendant 30 secondes.",
    "Faire une révérence comme dans un spectacle.",
    "Dire quelque chose que vous appréciez chez chaque personne présente.",
    "Faire une imitation de personnage célèbre.",
    "Faire une roue arrière sur une jambe pendant quelques secondes.",
    "Siffler une chanson de votre choix.",
    "Faire une pose de yoga simple.",
    "Dessiner quelque chose en moins de 2 minutes.",
    "Faire une danse de la victoire.",
    "Faire une grimace de sourire pendant 10 secondes.",
    "Se présenter en utilisant un accent différent.",
]
        
    res_gages = ''.join(random.choices(gages))
    
    pourcentage = (bonne_reponse / nbr_partie_joué ) * 100
    
    if pourcentage < 50:
    
        print("tu as un gage !!!")
        
        time.sleep(1)
        
        print("ton gages sera donnée dans :")
        
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('Gage donné')
        
        print(res_gages)
        
        oui_or_non = str(input("A tu réaliser ton gage ? ( o = oui ) et ( n = non )"))

    if oui_or_non == 'o':
        print("Bien jouer")
        
    else:
        print("Tu es vraiment nul")

def decompte():
    print("tu es prêts")
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('go')

questions_reponses_facile = {
    "Quelle est la capitale de la France ?": "paris",
    "Qui a peint la Mona Lisa ?": "de-vinci",
    "Combien y a-t-il de continents sur Terre ?": "5",
    "Quelle est la couleur du ciel par temps clair ?": "bleu",
    "Comment s'appelle l'astre lumineux autour duquel la Terre tourne ?": "lune",
    "Combien de doigts avons-nous sur une main ?": "5",
    "Quel est le premier mois de l'année ?": "janvier",
    "Quel est l'animal national de l'Australie ?": "kangourou",
    "Quel est le fruit jaune souvent associé à la notion de potassium ?": "banane",
    "Comment s'appelle le petit du lion ?": "lionceau",
}

questions_reponses_moyen =  {
    "Qui est le meilleur ami de Mickey Mouse ?": "pluto",
    "Quel est l'animal qui porte une carapace sur son dos ?": "tortue",
    "Quel est le nom du personnage principal dans 'La Reine des Neiges' ?": "elsa",
    "Combien y a-t-il de pattes sur une araignée ?": "huit",
    "Comment s'appelle l'oiseau qui apporte les bébés dans les histoires ?": "cigogne",
    "Quelle est la couleur du soleil ?": "jaune",
    "Quel est le nom du poisson clown dans le film 'Le Monde de Nemo' ?": "nemo",
    "Combien de jours y a-t-il dans une semaine ?": "sept",
    "Comment s'appelle le célèbre petit ours mangeur de miel ?": "winnie l'ourson",
}

questions_reponses_difficile = {
    "Combien de planètes y a-t-il dans notre système solaire ?": "8",
    "Quelle est la capitale du Japon ?": "tokyo",
    "Combien de pattes a un insecte ?": "6",
    "Quel est le plus grand mammifère terrestre ?": "elephant",
    "Combien de côtés a un pentagone ?": "5",
    "Qui a écrit 'Le Petit Prince' ?": "a. de saint-exupery",
    "Qui a découvert l'Amérique ?": "c.colomb",
    "Quelle est la capitale de l'Australie ?": "canberra",
}

question_adulte_facile = {
    "Quel est le nom de l'océan qui se trouve à l'est des États-Unis ?": "atlantique",
    "Quel est le principal ingrédient de la pizza Margherita ?": "mozzarella",
    "Qui a écrit 'Roméo et Juliette' ?": "shakespeare",
    "Quel est le plus grand organe du corps humain ?": "peau",
    "Combien de jours y a-t-il dans une année bissextile ?": "366",
    "Quel est le symbole chimique de l'élément oxygène ?": "O",
    "Dans quel pays se trouve la tour de Pise ?": "italie",
    "Qui a peint 'La Joconde' ?": "de vinci",
    "Quel est le nom de l'animal national de l'Australie ?": "kangourou",
    "Quel est le premier mois de l'année civile ?": "janvier",
}

question_adulte_moyen = {
    "Quel est le nom de la plus haute montagne du monde ?": "everset",
    "Qui a écrit le livre '1984' ?": "orwell",
    "Quelle est la capitale de l'Australie ?": "canberra",
    "Quel est le nom de l'organe responsable de la filtration du sang dans le corps humain ?": "rein",
    "Quel est l'auteur de la théorie de la relativité restreinte ?": "albert einstein",
    "Quel est le plus grand désert du monde ?": "antarctique",
    "Qui a peint 'La Nuit étoilée' ?": "vincent van gogh",
    "Quel est l'élément chimique le plus abondant dans l'univers ?": "hydrogène",
    "Quel est le nom du premier homme à avoir marché sur la lune ?": "neil armstrong",
    "Quel est le principal constituant de l'atmosphère terrestre ?": "azote",
}

question_adulte_difficile = {
    "Qui est le seul président américain à avoir renoncé à son mandat ?": "richard nixon",
    "Quelle est la formule chimique de l'hexafluorure de soufre ?": "SF6",
    "Quel est le nom du plus grand lac d'eau douce du monde par superficie ?": "lac superieur",
    "Quel est le nom de l'empereur romain qui a régné le plus longtemps ?": "auguste",
    "Quel est le nom de la mission spatiale qui a posé le premier homme sur la Lune ?": "apollo 11",
    "Quelle est la hauteur exacte de la statue de la Liberté, du sol à la pointe de la flamme ?": "93",
    "Qui a inventé le microscope ?": "jansenn",
    "Combien de symphonies a composées Ludwig van Beethoven ?": "9",
    "Quelle est la vitesse de la lumière en mètres par seconde ?": "300 000 000",
    "Quelle est la formule chimique de l'anhydride sulfurique ?": "SO3",
}

print("Bienvenue dans le jeux des questions avec des gages")

time.sleep(1)

md_jeux = str(input("Veut tu jouer a le version enfant (e) ou adulte (a) ou survie (s) ? : "))

time.sleep(1)

while md_jeux not in ["e", "a", "s"]:
    print("Choix incorrect")
    md_jeux = str(input("Veut tu jouer a le version enfant (e) ou adulte (a) ou survie (s) ? : "))
    
if md_jeux == 'e':
    
    print("Il y a 3 modes de jeux : ( 1 = facile) ( 2 = moyen) ( 3 = difficile )")

    time.sleep(1)

    print("Si tu as moins de 50 pourcent de bonne réponse = gage")
    
    time.sleep(1)
    
    qst = int(input("Combien de question veut tu faires ? : "))
    
    time.sleep(1)
    
    mdj = int(input("Tu veux jouer niveau : Facile(1); Moyen(2) ou Difficile(3) : "))
    
    while nbr_partie_joué < qst:
        
        if mdj == 1:
            
            decompte()
            
            question = random.choice(list(questions_reponses_facile.keys()))

            print(question)
            reponse_utilisateur = input("Votre réponse : ")

            time.sleep(1)
            
            if reponse_utilisateur == questions_reponses_facile[question]:
                print("Bonne réponse !")
                bonne_reponse += 1
            else:
                print(f"Mauvaise réponse. La réponse correcte est : {questions_reponses_facile[question]}")
            
            nbr_partie_joué += 1  
            
        if mdj == 2:
            
            decompte()

            question = random.choice(list(questions_reponses_moyen.keys()))

            print(question)
            reponse_utilisateur = input("Votre réponse : ")
            
            time.sleep(1)
            
            if reponse_utilisateur == questions_reponses_moyen[question]:
                print("Bonne réponse !")
                bonne_reponse += 1
            else:
                print(f"Mauvaise réponse. La réponse correcte est : {questions_reponses_moyen[question]}")
            
            nbr_partie_joué += 1
            
        if mdj == 3:
            
            decompte()
            
            question = random.choice(list(questions_reponses_difficile.keys()))

            print(question)
            reponse_utilisateur = input("Votre réponse : ")

            time.sleep(1)
            
            if reponse_utilisateur == questions_reponses_difficile[question]:
                print("Bonne réponse !")
                bonne_reponse += 1
            else:
                print(f"Mauvaise réponse. La réponse correcte est : {questions_reponses_difficile[question]}")
                
            nbr_partie_joué += 1

        else:
            print("Choix incorrect")
            
    pourcent()

if md_jeux == "a":
    
    print("Il y a 3 modes de jeux : ( 1 = facile) ( 2 = moyen) ( 3 = difficile )")

    time.sleep(1)

    print("Si tu as moins de 50 pourcent de bonne réponse = gage")
    
    time.sleep(1)
    
    qst = int(input("Combien de question veut tu faires ? : "))

    mdj = int(input("Tu veux jouer niveau : Facile(1); Moyen(2) ou Difficile(3) : "))

    while nbr_partie_joué < qst:
        
        if mdj == 1:
            
            decompte()

            question = random.choice(list(question_adulte_facile.keys()))

            print(question)
            reponse_utilisateur = input("Votre réponse : ")

            time.sleep(1)
            
            if reponse_utilisateur == question_adulte_facile[question]:
                print("Bonne réponse !")
                bonne_reponse += 1
            else:
                print(f"Mauvaise réponse. La réponse correcte est : {question_adulte_facile[question]}")
            
            nbr_partie_joué += 1  
            
        if mdj == 2:
            
            decompte()

            question = random.choice(list(question_adulte_moyen.keys()))

            print(question)
            reponse_utilisateur = input("Votre réponse : ")
            
            time.sleep(1)
            
            if reponse_utilisateur == question_adulte_moyen[question]:
                print("Bonne réponse !")
                bonne_reponse += 1
            else:
                print(f"Mauvaise réponse. La réponse correcte est : {question_adulte_moyen[question]}")
                
            nbr_partie_joué += 1
            
        if mdj == 3:
            
            decompte()
            
            question = random.choice(list(question_adulte_difficile.keys()))

            print(question)
            reponse_utilisateur = input("Votre réponse : ")

            time.sleep(1)
            
            if reponse_utilisateur == question_adulte_difficile[question]:
                print("Bonne réponse !")
                bonne_reponse += 1
            else:
                print(f"Mauvaise réponse. La réponse correcte est : {question_adulte_difficile[question]}")
            
            nbr_partie_joué += 1  
        else:
            print("Choix incorrect")
            
    pourcent() 

if md_jeux == 's':
    
    time.sleep(1)
    
    version = int(input("Version enfant (1) ou adulte (2) : "))
    
    if version == '1':
    
        mauvaise_rep = 0
        
        print("Ce mode de jeux consiste à avoir le plus grand nombre de bonne réponse sans se tromper")
        
        time.sleep(1)
        
        print("Il y a 3 modes de jeux : ( 1 = facile) ( 2 = moyen) ( 3 = difficile )")
        
        time.sleep(1)
        
        mdj = int(input("Tu veux jouer niveau : Facile(1); Moyen(2) ou Difficile(3) : "))
        
        while mauvaise_rep != 1:
            
            if mdj not in ['1', '2', '3']:
                print("Choix incorrect")
            
            if mdj == 1:
                
                decompte()
                
                question = random.choice(list(questions_reponses_facile.keys()))

                print(question)
                reponse_utilisateur = input("Votre réponse : ")

                time.sleep(1)
                
                if reponse_utilisateur == questions_reponses_facile[question]:
                    print("Bonne réponse !")
                    bonne_reponse += 1
                else:
                    print(f"Mauvaise réponse. La réponse correcte est : {questions_reponses_facile[question]}")
                    mauvaise_rep += 1 
                    print("Dommage !!!") 
                
            if mdj == 2:
                
                decompte()

                question = random.choice(list(questions_reponses_moyen.keys()))

                print(question)
                reponse_utilisateur = input("Votre réponse : ")
                
                time.sleep(1)
                
                if reponse_utilisateur == questions_reponses_moyen[question]:
                    print("Bonne réponse !")
                    bonne_reponse += 1
                else:
                    print(f"Mauvaise réponse. La réponse correcte est : {questions_reponses_moyen[question]}")
                    mauvaise_rep += 1
                    print("Dommage !!!") 
                
            if mdj == 3:
                
                decompte()
                
                question = random.choice(list(questions_reponses_difficile.keys()))

                print(question)
                reponse_utilisateur = input("Votre réponse : ")

                time.sleep(1)
                
                if reponse_utilisateur == questions_reponses_difficile[question]:
                    print("Bonne réponse !")
                    bonne_reponse += 1
                else:
                    print(f"Mauvaise réponse. La réponse correcte est : {questions_reponses_difficile[question]}")
                    mauvaise_rep += 1
                    print("Dommage !!!")  
                
    elif version == '2':
    
        mauvaise_rep = 0
        
        print("Ce mode de jeux consiste à avoir le plus grand nombre de bonne réponse sans se tromper")
        
        time.sleep(1)
        
        print("Il y a 3 modes de jeux : ( 1 = facile) ( 2 = moyen) ( 3 = difficile )")
        
        time.sleep(1)
        
        mdj = int(input("Tu veux jouer niveau : Facile(1); Moyen(2) ou Difficile(3) : "))
        
        while mauvaise_rep != 1:
            
            if mdj == 1:
                
                decompte()
                
                question = random.choice(list(question_adulte_facile.keys()))

                print(question)
                reponse_utilisateur = input("Votre réponse : ")

                time.sleep(1)
                
                if reponse_utilisateur == question_adulte_facile[question]:
                    print("Bonne réponse !")
                    bonne_reponse += 1
                else:
                    print(f"Mauvaise réponse. La réponse correcte est : {question_adulte_facile[question]}")
                    mauvaise_rep += 1 
                    print("Dommage !!!") 
                
            if mdj == 2:
                
                decompte()

                question = random.choice(list(question_adulte_moyen.keys()))

                print(question)
                reponse_utilisateur = input("Votre réponse : ")
                
                time.sleep(1)
                
                if reponse_utilisateur == question_adulte_moyen[question]:
                    print("Bonne réponse !")
                    bonne_reponse += 1
                else:
                    print(f"Mauvaise réponse. La réponse correcte est : {question_adulte_moyen[question]}")
                    mauvaise_rep += 1
                    print("Dommage !!!")  
                
            if mdj == 3:
                
                decompte()
                
                question = random.choice(list(question_adulte_difficile.keys()))

                print(question)
                reponse_utilisateur = input("Votre réponse : ")

                time.sleep(1)
                
                if reponse_utilisateur == question_adulte_difficile[question]:
                    print("Bonne réponse !")
                    bonne_reponse += 1
                else:
                    print(f"Mauvaise réponse. La réponse correcte est : {question_adulte_difficile[question]}")
                    mauvaise_rep += 1
                    print("Dommage !!!")  
            
            else:
                print("Choix incorrect")
    
time.sleep(1)

print('Nombre de bonne réponse = ',bonne_reponse)
