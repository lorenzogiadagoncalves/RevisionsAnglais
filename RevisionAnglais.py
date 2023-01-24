import random

verbeList = [
#   ["EN_Présent","EN_Prétérite","EN_ParticipePassé","FR_Infinitif"],
    ["win","won","won","gagner"],
    ["beat","beat","beaten","battre"],
    ["become","became","become","devenir"],
    ["come","came","come","venir"],
    ["run","ran","run","courrir"],
    ["awake","awoke","awoken","se réveiller"],
    ["be","was/were","been","être"],
    ["bear","bore","borne","supporter"],
    ["begin","began","begun","commencer"],
    ["bite","bot","bitten","mordre"]
]

vocabularyList = [
#   ["MotEN","MotFR"],
    ["gap year","année sabbatique"],
    ["reward","récompense"],
    ["travel","voyager"],
    ["les pays bas","the netherlands"],
    ["second amendment rights","les droits relatifs au port d'armes"],
]

def randVerb():
        nb = random.randint(1,len(verbeList))
        nbform = random.randint(1,4)
        if nbform == 1:
            verbe = (verbeList[nb][0]+" _____ "+" _____ "+" _____ ")
        elif nbform == 2:
            verbe =  (" _____ "+verbeList[nb][1]+" _____ "+" _____ ")
        elif nbform == 3:
            verbe =  (" _____ "+" _____ "+verbeList[nb][2]+" _____ ")
        else:
            verbe =  (" _____ "+" _____ "+" _____ "+verbeList[nb][3])
        print("")
        return [verbe,verbeList[nb]]

def randVoc():
    nb = random.randint(1,len(vocabularyList))
    

print("Pour stopper le programme, entrer la commande \"stop\"")

choice = None
while True:
    print("Que voulez vous travailler ?")
    choice = input("Verbes, Vocabulaire")
    if choice.lower() == "verbe":
        while True:
            verbe, correct = randVerb()
            userInput = input(verbe).lower()
            if correct == userInput.split(" "):
                print("Great Job !")
            elif userInput == "stop":
                print("Stopping...")
                break
            else:
                print("Wrong, the right answer is : "+str(correct))
        
        
    elif choice.lower == "vocabulaire":
        while True:
            
            userInput = input(verbe).lower()
            if correct == userInput.split(""):
                print("Great Job !")
            elif userInput == "stop":
                print("Stopping...")
                break
            else:
                print("Wrong, the right answer is : "+str(correct))