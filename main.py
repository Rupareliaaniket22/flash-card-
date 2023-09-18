from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
import pandas
import random
to_read={}
current_card = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("./data/french_words.csv")
    to_read=original_data.read_csv("./data/french_words.csv")
else:
    to_read = data.to_dict(orient="records")



# ------------------------------------------------working---------------------------------------------------
def next_card():
    global current_card,flip_timer
    current_card=random.choice(to_read)
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_bg, image=image)
    canvas.itemconfig(language_text, text="french", fill="black")
    canvas.itemconfig(language_word, text=current_card["French"], fill="black")
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(language_text, text="English", fill="White")
    canvas.itemconfig(language_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_bg,image=bg_image)

def is_known():
    to_read.remove(current_card)
    data1=pandas.DataFrame(to_read)
    data1.to_csv("./data/words_to_learn.csv",index=False)
    next_card()

# ------------------------------------------------ui---------------------------------------------------
window = Tk()
window.title("flashy")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)
flip_timer=window.after(3000, func=flip_card)
image = PhotoImage(file="./images/card_front.png")
bg_image = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=image.width(), height=image.height())
canvas_bg = canvas.create_image(400, 263, image=image)
language_text = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"), fill="black")
language_word = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=0, padx=20, pady=20, columnspan=2)

# ------------------------------------------------Buttons---------------------------------------------------
known_image = PhotoImage(file="./images/right.png")
known_button = Button(image=known_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
known_button.grid(row=2, column=0)

unknown_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,command=next_card)
unknown_button.grid(row=2, column=1)
next_card()
window.mainloop()
