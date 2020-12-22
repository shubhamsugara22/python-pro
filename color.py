import tkinter
import random

colours = ["Red", "Blue", "Green", "Orange", "Pink",
           "Black", "Yellow", "White", "Purple", "Brown"]

score = 0

timeleft = 30

# fucntion that will start game


def startGame(event):

    if timeleft == 30:

        countdown()

    nextColour()

# function that will choose text and colour


def nextColour():

    global score
    global timeleft
    # check if a game is active
    if timeleft > 0:

        # make the entry box active
        e.focus_set()
# if colour typed is equal to colour of text
        if e.get().lower() == colours[1].lower():

            score += 1
# clear the text entry box
        e.delete(0, tkinter.END)

        random.shuffle(colours)

        label.config(fg=str(colours[1]), text=str(colours[0]))

        scoreLabel.config(text="Score :" + str(score))

# countdown timer function


def countdown():

    global timeleft

    if timeleft > 0:

        timeleft -= 1

        timeLabel.config(text="Time left:" + str(timeleft))

        timeLabel.after(1000, countdown)


# create GUI window
root = tkinter.Tk()
# set the title
root.title("COLORGAME")
# set the size
root.geometry("375x200")

# add the instruction labels
instructions = tkinter.Label(
    root, text="Type in colour of the words , and not words in text! ", font=('Helvetica', 12))

instructions.pack()

# add a score Label
scoreLabel = tkinter.Label(
    root, text="Press enter to start", font=('Helvetica', 12))

scoreLabel.pack()

# add a timeleft label
timeLabel = tkinter.Label(root, text="Time left :" +
                          str(timeleft), font=('Helvetica ', 12))

timeLabel.pack()

# add albel for displaying colours
label = tkinter.Label(root, font=('Helvetica', 60))

label.pack()
# add a text entry box for writting colour
e = tkinter.Entry(root)

# run the startgame function when enter key is pressed
root.bind('<Return>', startGame)
e.pack()
# set focus on entry box
e.focus_set()

# start he GUI
root.mainloop()
