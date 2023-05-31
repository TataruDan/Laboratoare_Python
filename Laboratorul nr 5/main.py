from tkinter import *
from random import randint
from tkinter import ttk
window = Tk()

window.title('Piatra - Hartie - Foarfeca')
window.geometry("500x450")
window.config(bg="white")


rock = PhotoImage(file='images/rock.png')
paper = PhotoImage(file="images/paper.png")
scissors = PhotoImage(file="images/scissors.png")


image_list = [rock, paper, scissors]

pick_number = randint(0,2)

img_start = Label(window, image=image_list[pick_number])
img_start.pack(pady=20)


def spin():
    score = 0
    pick_number = randint(0, 2)
    img_start.config(image=image_list[pick_number])

    if user_choice.get() == "Piatra":
        user_choice_value = 0
    elif user_choice.get() == "Hartie":
        user_choice_value = 1
    elif user_choice.get() == "Foarfeca":
        user_choice_value = 2


    if user_choice_value == 0:
        if pick_number ==  0:
            label.config(text="Egalitate")
        elif pick_number == 1:
            label.config(text="Hartia acopera Piatra" + "\n" + "A-ti pierdut")
        elif pick_number == 2:
            score += 1
            label.config(text="Piatra strica Foarfeca" + "\n" + "A-ti castigat")

    if user_choice_value == 1:
        if pick_number == 0:
            label.config(text="Hartia acopera Piatra" + "\n" + "A-ti castigat")
        elif pick_number == 1:
            label.config(text="Egalitate")
        elif pick_number == 2:
            label.config(text="Foarfeca taie hartia" + "\n" + "A-ti pierdut")

    if user_choice_value == 2:
        if pick_number ==  0:
            label.config(text="Piatra strica foarfeca" + "\n" + "Ati pierdut")
        elif pick_number == 1:
            label.config(text="Foarfeca taie hartia" + "\n" + "A-ti castigat")
        elif pick_number == 2:
            label.config(text="Egalitate")


user_choice = ttk.Combobox(window, value=("Piatra","Hartie","Foarfeca"))
user_choice.current(0)
user_choice.pack(pady=20)
button = Button(window, text="Apasă", command=spin)
button.pack(pady=10)


label = Label(window, text="", font=("Helvetica", 18), bg="white")
label.pack(pady=20)
window.mainloop()