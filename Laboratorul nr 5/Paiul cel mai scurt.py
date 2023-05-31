from tkinter import *
from random import randint
window = Tk()

window.title('Paiul cel mai scurt')
window.geometry("500x200")
window.config(bg="white")


start_label = Label(window, text="In joc sunt 10 paie,"
                                 " ai grijă sa nu tragi cel scurt", font=("Helvetica", 14), bg="white")
start_label.pack(pady=20)


def get_match():
    pick_number = randint(0, 9)
    if pick_number == 0:
        label.config(text="A-ți tras paiul cel mai scurt! "
                          "Jocul se va stinge automat:(", font=14);
        window.after(2000, window.destroy)

    else:
        label.config(text="A-ți tras paiul lung! :)");



button = Button(window, text="Apasă", command=get_match)
button.pack(pady=10)


label = Label(window, text="", font=("Helvetica", 18), bg="white")
label.pack(pady=20)
window.mainloop()