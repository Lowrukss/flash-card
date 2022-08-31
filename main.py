import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
current_card = {}
language_dict = {}


# ---------------------------- buttons  ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(language_dict)
    canvas.itemconfig(language_text, text="Spanish", fill="black")
    canvas.itemconfig(language_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language_text, text="Polish", fill="white")
    canvas.itemconfig(language_word, text=current_card["Polish"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def word_remove():
    language_dict.remove(current_card)
    next_card()
    data = pandas.DataFrame(language_dict)
    data.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #
try:
    data_file = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/spanish_words.csv")
    language_dict = original_data.to_dict(orient="records")
else:
    language_dict = pandas.DataFrame.to_dict(data_file, orient="records")

window = Tk()
window.title("Flash Cards Spanish")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0, width=800, height=526)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
language_text = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
language_word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.update()
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, padx=50, pady=50, highlightthickness=0, command=word_remove)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, padx=50, pady=50, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
