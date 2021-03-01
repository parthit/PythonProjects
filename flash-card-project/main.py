BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
import pandas
import time

to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pandas.read_csv("data/french_words.csv")
    to_learn = og_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

# This is how I did it without using the dictionary data structure
# def get_random_french_word():
#     dfile = pandas.read_csv("data/french_words.csv")
#     word = dfile['French'][random.randint(0, 100)]
#     front_card.itemconfig(french_word, text=word)
#     front_card.itemconfig(language, text='French')

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()

def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language, text='French',fill='black')
    canvas.itemconfig(word, text=current_card['French'],fill='black')
    canvas.itemconfig(background, image=card_front_image)
    flip_timer = window.after(ms=3000,func=flip_card)


def flip_card():
    print(current_card)
    canvas.itemconfig(language, text='English',fill='white')
    canvas.itemconfig(word, text=current_card['English'],fill='white')
    canvas.itemconfig(background, image=card_back_image)



#_______THIS PART WAS FOR USER INTERFACE_______#
window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(ms=3000,func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400, 263, image=card_front_image)
language = canvas.create_text(400, 150, text='', font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text='', font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# card_back_image = PhotoImage(file="images/card_back.png")
# card_back = Button(image=card_back_image, highlightthickness=0)
# card_back.config(bg=BACKGROUND_COLOR)
# card_back.grid(row=0, column=1)

cross_image = PhotoImage(file="images/wrong.png")
cross = Button(image=cross_image, highlightthickness=0, command=next_word)
cross.grid(row=1, column=0)

tick_image = PhotoImage(file="images/right.png")
tick = Button(image=tick_image, highlightthickness=0, command=is_known)
tick.grid(row=1, column=1)

next_word()

window.mainloop()