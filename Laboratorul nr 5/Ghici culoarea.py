import tkinter
import random


colours = ['Rosu', 'Albastru', 'Verde', 'Roz', 'Negru',
           'Galben', 'Oranj', 'Alb', 'Violet', 'Brun']
score = 0

timeleft = 30


def startGame(event):
    if timeleft == 30:
        countdown()

    nextColour()

def nextColour():

    global score
    global timeleft

    if timeleft > 0:

        e.focus_set()

        if e.get().lower() == colours[1].lower():
            score += 1

        e.delete(0, tkinter.END)

        random.shuffle(colours)

        label.config(fg=str(colours[1]), text=str(colours[0]))


        scoreLabel.config(text="Scor: " + str(score))



def countdown():
    global timeleft

    if timeleft > 0:

        timeleft -= 1

        timeLabel.config(text="Timp rămas: "
                              + str(timeleft))

        timeLabel.after(1000, countdown)



root = tkinter.Tk()

root.title("Ghici culoarea")

root.geometry("375x200")

instructions = tkinter.Label(root, text="Introdu culoarea "
                                        "la cuvint, dar nu textul cuvintului!", font=('Helvetica', 12))

instructions.pack()

scoreLabel = tkinter.Label(root, text="Start",
                           font=('Helvetica', 12))

scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Timp rămas: " +
                                     str(timeleft), font=('Helvetica', 12))

timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()


e = tkinter.Entry(root)

root.bind('<Return>', startGame)
e.pack()
e.focus_set()

root.mainloop()