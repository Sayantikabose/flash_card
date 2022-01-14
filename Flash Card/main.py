
import pandas
from tkinter import *
import random
BACKGROUND_COLOR = "#B1DDC6"
current_word={}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/german.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def generateword():
    global current_word,flipafter
    window.after_cancel(flipafter)
    current_word=random.choice(to_learn)
    gre=current_word["GERMAN"]
    canvas.itemconfig(card_word,text=gre,fill="black")
    canvas.itemconfig(card_title,text="German",fill="black") 
    canvas.itemconfig(cardbackground,image=card_front)
    window.after(3000,func=flip)

def flip():
    canvas.itemconfig(card_title,text="English",fill="white") 
    canvas.itemconfig(card_word,text=current_word["ENGLISH"]) 
    canvas.itemconfig(cardbackground,image=card_back)

def is_known():
    to_learn.remove(current_word)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    generateword()


window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flipafter=window.after(3000,func=flip)

canvas=Canvas(width=800,height=526,bg="white")

card_front = PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")
cardbackground=canvas.create_image(400,263,image=card_front)
card_title=canvas.create_text(400, 150, text="GERMAN", fill="black", font=('Ariel 40 italic'))
card_word=canvas.create_text(400, 263, text="WORD", fill="black", font=('Ariel 60 bold'))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=1) 
generateword()

rightimg=PhotoImage(file="images/right.png")
button1 = Button(image=rightimg, highlightthickness=0,command=generateword) 
button1.grid(row=2,column=0)

wrongimg=PhotoImage(file="images/wrong.png")
button2 = Button(image=wrongimg, highlightthickness=0,command=generateword) 
button2.grid(row=2,column=2)


generateword()


window.mainloop()