import random

# Changer les verbes ici, attention à bien garder la forme : ["Présent","Prétérite","Participe Passé","Français"] pour chaques listes
verbeList = [
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
    
]

def randVerb():
        nb = random.randint(1,len(verbeList))
        form = random.randint(1,4)
        print("")
        return [Verbform(form,nb),verbeList[nb]]
            
def Verbform(nbForm,nb):
      if nbForm == 1:
          return (verbeList[nb][0]+" _____ "+" _____ "+" _____ ")
      elif nbForm == 2:
          return (" _____ "+verbeList[nb][1]+" _____ "+" _____ ")
      elif nbForm == 3:
          return (" _____ "+" _____ "+verbeList[nb][2]+" _____ ")
      else:
          return (" _____ "+" _____ "+" _____ "+verbeList[nb][3])
 
print("Pour stopper le programme, entrer la commande \"stop\"")

while True:
    verb, correct = randVerb()
    userInput = input(verb).lower()
    if correct == userInput.split(" "):
        print("Great Job !")
    elif userInput == "stop":
        print("Stopping...")
        break
    else:
        print("Wrong, the right answer is : "+str(correct))