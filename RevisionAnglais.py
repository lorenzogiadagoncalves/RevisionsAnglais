import random
import time

from tkinter import *
from tkinter.ttk import *

def getVerbeList():

    open(r"verbeList.txt", "a")
    with open(r"verbeList.txt", "r", encoding="utf-8") as f:
        verbeList = []
        for i in list(f.readlines()):
            verbeList.append(i.replace("\n", "").split(" : "))
    return verbeList

def getVocList():

    open(r"vocList.txt", "a")
    with open(r"vocList.txt", "r", encoding="utf-8") as f:
        vocList = []
        for i in list(f.readlines()):
            vocList.append(i.replace("\n", "").split(" : "))
    return vocList

#Choisis un verbe au hasard parmis la liste verbeList et le renvois avec sa correction
def randVerb():
        nb = random.randint(0,len(getVerbeList())-1)
        nbform = random.randint(1,4)
        if nbform == 1:
            verbe = (getVerbeList()[nb][0]+" _____ "+" _____ "+" _____ "+"\n")
        elif nbform == 2:
            verbe =  (" _____ "+getVerbeList()[nb][1]+" _____ "+" _____ "+"\n")
        elif nbform == 3:
            verbe =  (" _____ "+" _____ "+getVerbeList()[nb][2]+" _____ "+"\n")
        else:
            verbe =  (" _____ "+" _____ "+" _____ "+getVerbeList()[nb][3]+"\n")
        return [verbe,getVerbeList()[nb]]

#Choisis un mot de vocabulaire au hasard parmis la liste vocabularyList et le renvois avec sa correction
def randVoc():
    nb = random.randint(0,len(getVocList())-1)
    nbForm = random.randint(0,1)
    word = getVocList()[nb][nbForm]
    correctWord = getVocList()[nb][abs(nbForm-1)]
    return word, correctWord

# INTERFACE :

window = Tk()
window.title("Revisions Anglais")
window.geometry("1000x600")

runningProgram = False
correct = None
WidgetList = []

#Boutons
def ExitBtn():
    if runningProgram:
        window.destroy()
    else:
        TitleScreen()
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
            VerbScreen()

        elif selected.get() == 2:
            VocScreen()

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

    def SubmitBtn():
            if correct == [prst.get(), pret.get(), partp.get(), french.get()]:
                ResultScreen("Great Job !", "verbe")
            else:
                ResultScreen(
                    ("Wrong, the right answer is " + correct[0] + " / " + correct[1] + " / " + correct[2] + " / " +
                    correct[3]),"verbe")
    verbe, correct = randVerb()

    Label(window, text=verbe.lower(), font=100).place(rely=0.5, relx=0.5, anchor=CENTER)
    prst = Entry(window, width=10)
    pret = Entry(window, width=10)
    partp = Entry(window, width=10)
    french = Entry(window, width=10)
    Button(window, text="Submit", command=SubmitBtn).place(rely=0.7, relx=0.5, anchor=CENTER)

    prst.place(rely=0.6, relx=0.4, anchor=CENTER)
    pret.place(rely=0.6, relx=0.4667, anchor=CENTER)
    partp.place(rely=0.6, relx=0.5333, anchor=CENTER)
    french.place(rely=0.6, relx=0.6, anchor=CENTER)

def VocScreen():
    runningProgram = True
    ClearScreen()
    Label(window, text="Voc1", font=100).place(rely=0.5, relx=0.5, anchor=CENTER)
    def SubmitBtn():
            if correct == translated.get():
                ResultScreen("Great Job !", "verbe")
            else:
                ResultScreen(
                    ("Wrong, the right answer is " + correct),"voc")

    word, correct = randVoc()

    Label(window, text=word.lower(), font=100).place(rely=0.5, relx=0.5, anchor=CENTER)
    translated = Entry(window, width=10)
    Button(window, text="Submit", command=SubmitBtn).place(rely=0.7, relx=0.5, anchor=CENTER)

    translated.place(rely=0.6, relx=0.5, anchor=CENTER)
def ResultScreen(str, last):
    runningProgram = True
    ClearScreen()
    Label(window, text=str, font=100).place(rely=0.5, relx=0.5, anchor=CENTER)

    def retry():
        if last == "verbe":
            VerbScreen()
        else:
            VocScreen()

    Button(window, text="Retry", command=retry).place(rely=0.05, relx=0.85)


TitleScreen()
window.mainloop()