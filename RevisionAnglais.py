import random

verbeList = [
#   ["EN_Présent","EN_Prétérite","EN_ParticipePassé","FR_Infinitif"],
    ["blow","blew","blown","souffler"],
    ["break","broke","broken","casser"],
    ["choose","chose","chosen","choisir"],
    ["do","did","done","faire"],
    ["draw","drew","drawn","dessiner"],
    ["drink","drank","drunk","boire"],
    ["drive","drove","driven","conduire"],
    ["eat","ate","eaten","manger"],
    ["fall","fell","fallen","tomber"],
    ["fly","flew","flown","voler"]
]

vocabularyList = [
#   ["MotEN","MotFR"],
    ["gap year","année sabbatique"],
    ["reward","récompense"],
    ["travel","voyager"],
    ["les pays bas","the netherlands"],
    ["second amendment rights","les droits relatifs au port d'armes"],
]

getOtherNb = {0:1}

def randVerb():
        nb = random.randint(0,len(verbeList)-1)
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
    nb = random.randint(0,len(vocabularyList)-1)
    nbForm = random.randint(0,1)
    word = vocabularyList[nb][nbForm]
    correctWord = vocabularyList[nb][getOtherNb[nbForm]]
    return # [mot, correct]
    

print("Pour stopper le programme, entrer la commande \"stop\"")

choice = None
while True:
    print("Que voulez vous travailler ?")
    choice = input("Verbes, Vocabulaire\n")
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
                
    if choice.lower == "vocabulaire":
        while True:
            vocWord, correct = randVoc()
            userInput = input(vocWord).lower()
            if correct == userInput:
                print("Great Job !")
            elif userInput == "stop":
                print("Stopping...")
                break
            else:
                print("Wrong, the right answer is : "+str(correct))
    
    if choice == "stop":
            print("Stopping...")
            break
