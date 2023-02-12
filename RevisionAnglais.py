import random
import time

from tkinter import *
from tkinter.ttk import *


verbeList = [
#   ["EN_Présent","EN_Prétérite","EN_ParticipePassé","FR_Infinitif"],
    ["have","had","had","avoir"],
    ["go","went","gone","aller"],
    ["begin","began","begun","commencer"],
    ["drink","drank","drunk","boire"],
    ["swim","swam","swum","nager"],
    ["drive","drove","driven","conduire"],
    ["ride","rode","riden","chevaucher"],
    ["write","wrote","written","écrire"],
    ["feel","felt","felt","ressentir"],
    ["learn","learnt","learnt","apprendre"],
]

vocabularyList = [
#   ["MotEN","MotFR"],
    ["gap year","année sabbatique"],
    ["reward","récompense"],
    ["travel","voyager"],
    ["les pays bas","the netherlands"],
    ["second amendment rights","les droits relatifs au port d'armes"]
]

#Choisis un verbe au hasard parmis la liste verbeList et le renvois avec sa correction
def randVerb():
        nb = random.randint(0,len(verbeList)-1)
        nbform = random.randint(1,4)
        if nbform == 1:
            verbe = (verbeList[nb][0]+" _____ "+" _____ "+" _____ "+"\n")
        elif nbform == 2:
            verbe =  (" _____ "+verbeList[nb][1]+" _____ "+" _____ "+"\n")
        elif nbform == 3:
            verbe =  (" _____ "+" _____ "+verbeList[nb][2]+" _____ "+"\n")
        else:
            verbe =  (" _____ "+" _____ "+" _____ "+verbeList[nb][3]+"\n")
        return [verbe,verbeList[nb]]

#Choisis un mot de vocabulaire au hasard parmis la liste vocabularyList et le renvois avec sa correction
def randVoc():
    nb = random.randint(0,len(vocabularyList)-1)
    nbForm = random.randint(0,1)
    word = vocabularyList[nb][nbForm]
    correctWord = vocabularyList[nb][abs(nbForm-1)]
    return word, correctWord
    

print("Pour retourner en arrière ou stopper le programme, entrer la commande \"!stop\"")

for i in range(1,1):
    print("Que voulez vous travailler ?")
    choice = input("Verbes, Vocabulaire\n")
    if choice.lower() in ["verbe","verbes"]:
        while True:
            verbe, correct = randVerb()
            userInput = input(verbe).lower()
            if correct == userInput.split(" "):
                print("Great Job !")
            elif userInput == "!stop":
                print("Stopping...")
                break
            else:
                print("Wrong, the right answer is : "+str(correct))
                
    if choice.lower() in ["vocabulaire","voc","vocabulary"]:
        while True:
            vocWord, correct = randVoc()
            userInput = input(vocWord).lower()
            if correct == userInput:
                print("Great Job !")
            elif userInput == "!stop":
                print("Stopping...")
                break
            else:
                print("Wrong, the right answer is : "+str(correct))
    
    if choice == "!stop":
            print("Stopping...")
            break

# FINAL :

window = Tk()
window.title("Revisions Anglais")
window.attributes("-fullscreen", False)

runningProgram = False

correct = None

WidgetList = []

#Verbes
prst = Entry(window, width=10)
pret = Entry(window, width=10)
partp = Entry(window, width=10)
french = Entry(window, width=10)

#Boutons
def ExitBtn():
    if runningProgram:
        window.destroy()
    else:
        TitleScreen()
def SubmitBtn():
    try:

        if correct == [prst.get(), pret.get(), partp.get(), french.get()]:
            ResultScreen("Great Job !")
        else:
            ResultScreen("Wrong, the right answer is "+ correct[0] + " / "+correct[1] + " / " + correct[2] + " / "+correct[3])
    except:
        print("Error, Missing Verb")
def ClearScreen():
    for widget in window.winfo_children():
        widget.destroy()
    Button(window, text="Exit", command=ExitBtn).place(rely=0.05, relx=0.05)
    return

def TitleScreen():
    runningProgram = False
    ClearScreen()

    WidgetList.append(Label(window, text="Welcome !", font=100))
    WidgetList.append(Label(window, text="What do you want to learn today ?", font=70))

    selected = IntVar()

    WidgetList.append(Radiobutton(window, text='Verb', value=1, variable=selected))
    WidgetList.append(Radiobutton(window, text='Vocabulary', value=2, variable=selected))

    def ChoiceBtn():
        # Starting Session
        if selected.get() == 1:
            print("1")
            VerbScreen()

        elif selected.get() == 2:
            print("2")
            VocScreen()
        else:
            print("0")

    WidgetList.append(Button(window, text="Let's start !", command=ChoiceBtn))

    # Affichage
    MainScreen = [0.4, 0.6]
    nbBoucle = 0
    for i in WidgetList:
        nbBoucle = nbBoucle + 1
        co = MainScreen[0] + (MainScreen[1] - MainScreen[0]) / WidgetList.__len__() * nbBoucle
        i.place(rely=co, relx=0.5, anchor=CENTER)
    WidgetList.clear()
def VerbScreen():
    runningProgram = True
    ClearScreen()

    verbe, correct = randVerb()

    Label(window, text=verbe.lower(), font=100).place(rely=0.5, relx=0.5, anchor=CENTER)
    prst.place(rely=0.6, relx=0.4, anchor=CENTER)
    pret.place(rely=0.6, relx=0.4667, anchor=CENTER)
    partp.place(rely=0.6, relx=0.5333, anchor=CENTER)
    french.place(rely=0.6, relx=0.6, anchor=CENTER)
    Button(window, text="Submit", command=SubmitBtn).place(rely=0.7, relx=0.5, anchor=CENTER)

def VocScreen():
    runningProgram = True
    ClearScreen()
    Label(window, text="Voc1", font=100).place(rely=0.5, relx=0.5, anchor=CENTER)
def ResultScreen(str):
    runningProgram = True
    ClearScreen()
    Label(window, text=str, font=100).place(rely=0.5, relx=0.5, anchor=CENTER)


TitleScreen()
window.mainloop()