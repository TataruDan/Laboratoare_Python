#Import the required Libraries
from tkinter import *
from tkinter import ttk
from random import randint

window = Tk()
window.geometry("750x250")
window.title("Magic 8 Ball")
window.config(bg="white")

title = Label(window, text="MYSTIC 8 BALL", font=("Courier 30 bold"))
title.pack()

label = Label(window, text="Pune intrebarea", font=("Courier 22 bold"))
label.pack()

entry= Entry(window, width= 40)
entry.focus_set()
entry.pack()

outputs = ["Este sigur","Este incontestabil",
           "Fără îndoială","Da - cu siguranţă",
           "Puteţi să vă bazaţi pe ea",
           "După cum văd eu lucrurile, da",
           "Cel mai probabil","Perspective bune",
           "Punct de semne pentru DA","Da",
           "Răspuns neclar, încercați din nou"
           ,"Adresati-va din nou mai tarziu",
           "Mai binu nu-ti spun acum",
           "Nu se poate prezice acum",
           "Se concentreaza si intreaba din nou",
           "Nu cred","Raspunsul meu - NU",
           "Sursele mele spun ca nu",
           "Perspectivele nu sunt atit de bune",
           "Foarte dubios"]


def validate():

        question = entry.get()
        if question == '':
            message = "Nu ati introdus nimic."
            output_label.config(text=message)
        elif question.isdigit():
            message = "Nu inteleg mesajul introdus. Modifica."
            output_label.config(text=message)
        elif not question.endswith("?"):
            message = "Daca aceasta este intrebare, ai uitat ?"
            output_label.config(text=message)
        elif not " " in question:
            message = "Nu o intrebare dintr-un cuvint"
            output_label.config(text=message)
        else:
            pick_number = randint(0, len(outputs))
            output_label.configure(text=outputs[pick_number])


def delay():
    message = "Mesajul se proceseaza. Asteptati."
    output_label.config(text=message)
    window.after(2000, validate)


ttk.Button(window, text= "Primeste raspuns !",width= 20, command= delay).pack(pady=20)

output_label = Label(window, text="", font=("Helvetica", 18), bg="white")
output_label.pack(pady=20)

window.mainloop()