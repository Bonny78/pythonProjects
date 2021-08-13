from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME ="Arial"
current_card ={}
to_learn ={}

#----------------Reading file----------
#if there no words to learn.csv then we catch a FileNOtFoundError
try:
    file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_file = pandas.read_csv("data/french_words.csv")
    to_learn = original_file.to_dict(orient="records")
else:
    to_learn = file.to_dict(orient="records")

print(to_learn)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) #cancels the wait time unless you land on a card and wait
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(old_image, image=card_front_img)
    flip_timer= window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(old_image, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data=pandas.DataFrame(to_learn)
    data.to_csv("data\words_to_learn.csv", index=False) # index False removes the index numbers from csv file
    next_card()

# ------------ UI SetUp------------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# create canvas
canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
#adding front card image
old_image = canvas.create_image(400, 263, image=card_front_img)
#adding text to the flash
title_text = canvas.create_text(400, 150,text="", fill="black", font=(FONT_NAME, 40, "italic"))
word_text =canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

right_button_img = PhotoImage(file="./images/right.png")
wrong_button_img = PhotoImage(file="./images/wrong.png")

#create buttons
right_button= Button(image=right_button_img, highlightthickness = 0, command=is_known)
right_button.grid(row=1, column=1)

#wrong button
wrong_button = Button(image=wrong_button_img, highlightthickness = 0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()



window.mainloop()
