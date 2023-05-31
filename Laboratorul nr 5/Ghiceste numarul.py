import tkinter as tk
from random import randrange

window = tk.Tk()
window.title("Ghiceste numărul")

lblInst = tk.Label(window, text = "Ghiceste numarul care este cuprins intre 0 si 9")
lblLine0 = tk.Label(window, text = "*********************************************************************")
lblNoGuess = tk.Label(window, text = "Nr. de incercari: 0")
lblMaxGuess = tk.Label(window, text = "Max numar de incercari: 3")
lblLine1 = tk.Label(window, text = "*********************************************************************")
lblLogs = tk.Label(window, text="Monitorizare")
lblLine2 = tk.Label(window, text = "*********************************************************************")

buttons = []
for index in range(0, 10):
    button = tk.Button(window, text=index, command=lambda index=index : process(index), state=tk.DISABLED)
    buttons.append(button)


btnStartGameList = []
for index in range(0, 1):
    btnStartGame = tk.Button(window, text="Start Joaca", command=lambda : startgame(index))
    btnStartGameList.append(btnStartGame)

lblInst.grid(row=0, column=0, columnspan=5)
lblLine0.grid(row=1, column=0, columnspan=5)
lblNoGuess.grid(row=2, column=0, columnspan=3)
lblMaxGuess.grid(row=2, column=3, columnspan=2)
lblLine1.grid(row=3, column=0, columnspan=5)
lblLogs.grid(row=4, column=0, columnspan=5)  # row 4 - 8 is reserved for showing logs

lblLine2.grid(row=9, column=0, columnspan=5)


for row in range(0, 2):
    for col in range(0, 5):
        i = row * 5 + col  # convert 2d index to 1d. 5= total number of columns
        buttons[i].grid(row=row+10, column=col)

btnStartGameList[0].grid(row=13, column=0, columnspan=5)

guess = 0
totalNumberOfGuesses = 0
secretNumber = randrange(10)
print(secretNumber)
lblLogs = []
guess_row = 4

def init():
    global buttons, guess, totalNumberOfGuesses, secretNumber, lblNoGuess, lblLogs, guess_row
    guess = 0
    totalNumberOfGuesses = 0
    secretNumber = randrange(10)
    print(secretNumber)
    lblNoGuess["text"] = "Numarul de incercari: 0"
    guess_row = 4

    # remove all logs on init
    for lblLog in lblLogs:
        lblLog.grid_forget()
    lblLogs = []


def process(i):
    global totalNumberOfGuesses, buttons, guess_row
    guess = i

    totalNumberOfGuesses += 1
    lblNoGuess["text"] = "Cate ori ati ghicit: " + str(totalNumberOfGuesses)

    # check if guess match secret number
    if guess == secretNumber:
        lbl = tk.Label(window, text="A-ti ghicit numărul, felicitări! :) ", fg="green")
        lbl.grid(row=guess_row, column=0, columnspan=5)
        lblLogs.append(lbl)
        guess_row += 1

        for b in buttons:
            b["state"] = tk.DISABLED
    else:
        # give player some hints
        if guess > secretNumber:
            lbl = tk.Label(window, text="Numarul secret este mai mic decât numărul introdus :)", fg="red")
            lbl.grid(row=guess_row, column=0, columnspan=5)
            lblLogs.append(lbl)
            guess_row += 1
        else:
            lbl = tk.Label(window, text="Numarul secret este mai mare decât numărul introdus :)", fg="red")
            lbl.grid(row=guess_row, column=0, columnspan=5)
            lblLogs.append(lbl)
            guess_row += 1

    if totalNumberOfGuesses == 3:
        if guess != secretNumber:
            lbl = tk.Label(window, text="A-ți epuizat numărul de incercări, ati pierdut :)", fg="red")
            lbl.grid(row=guess_row, column=0, columnspan=5)
            lblLogs.append(lbl)
            guess_row += 1

        for b in buttons:
            b["state"] = tk.DISABLED

    buttons[i]["state"] = tk.DISABLED


status = "none"


def startgame(i):
    global status
    for b in buttons:
        b["state"] = tk.NORMAL

    if status == "none":
        status = "started"
        btnStartGameList[i]["text"] = "Restart Joacă"
    else:
        status = "restarted"
        init()
    print("Joaca a inceput")


window.mainloop()