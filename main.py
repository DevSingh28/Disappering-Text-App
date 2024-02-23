from tkinter import *

disappear_timer = None


def start_typing(event=None):
    global disappear_timer
    if disappear_timer is not None:
        window.after_cancel(disappear_timer)
    disappear_timer = window.after(5000, disappear_text)


def disappear_text():
    inp.delete('1.0', END)


window = Tk()
window.title("Text Disappearing App")
window.config(padx=20, pady=20)

canvas = Canvas(width=300, height=280)
photo = PhotoImage(file="img.png")
canvas.create_image(152, 150, image=photo)
canvas.pack()

label1 = Label(text="Start Writing", fg='purple', font=("Comic Sans MS", 24, "bold"))
label1.pack()

label2 = Label(text="Text will Disappear if you stopped typing for more than 5sec.", font=("Comic Sans MS", 10, "italic"))
label2.pack()

inp = Text(width=40, height=10)
inp.focus()
inp.pack()

inp.bind("<KeyRelease>", start_typing)

window.mainloop()
