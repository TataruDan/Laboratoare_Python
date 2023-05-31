from tkinter import *
from random import randint
from tkinter import ttk

window = Tk()

window.title('Piatra - Hartie - Foarfeca')
window.geometry("500x450")
window.config(bg="white")


head = PhotoImage(file='images/head.png')
tail = PhotoImage(file="images/tail.png")
start_image = PhotoImage(file="images/img.png")


image_list = [head,tail]

pick_number = randint(0,1)

img_start = Label(window, image=start_image)
img_start.pack(pady=20)


def spin():
    pick_number = randint(0, 1)
    img_start.config(image=image_list[pick_number])

    if pick_number == 0:
        label.config(text="A căzut pajura")
    else:
        label.config(text="A căzut banul")


button = Button(window, text="Apasă", command=spin)
button.pack(pady=10)


label = Label(window, text="", font=("Helvetica", 18), bg="white")
label.pack(pady=20)
window.mainloop()