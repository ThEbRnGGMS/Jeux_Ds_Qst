import random
import time

def nbrPartie():
    print('tu as joué',nbr_partie_joué,'partie')

print("Bienvenue dans le jeux des questions avec des gages")

time.sleep(1)

print("Il y a 3 modes de jeux : ( 1 = facile) ( 2 = moyen) ( 3 = difficile )")

time.sleep(1)

print("Si tu as moins de 50 pourcent de bonne réponse = gage")

qst = int(input("Combien de question veut tu faires ? : "))

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
    
    res_gages = random.choices(gages)
    
    pourcentage = (nbr_partie_joué // bonne_reponse) * 100
    
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
        print('0')
        
        print(res_gages)
        
        oui_or_non = int(input("A tu réaliser ton gage ? ( o = oui ) et ( n = non )"))
        
        if oui_or_non == 'o':
            print("Bien jouer")
        
        else:
            print("Tu es vraiment nul")


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

mdj = int(input("Tu veux jouer niveau : Facile(1); Moyen(2) ou Difficile(3) : "))

time.sleep(1)

print("tu es prêts")
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('go')

while nbr_partie_joué < qst:
    
    if mdj == 1:

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
        
    nbrPartie()

time.sleep(1)

print('Nombre de bonne réponse = ',bonne_reponse)

pourcent()

time.sleep(1)

print("fin du jeux")
