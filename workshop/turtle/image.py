from tkinter import Tk, Label
from PIL import Image, ImageTk, ImageSequence

window = Tk()
window.title("Animated GIF")

gif = Image.open("turtle.gif")

frames = [
    ImageTk.PhotoImage(frame.copy())
    for frame in ImageSequence.Iterator(gif)
]

label = Label(window)
label.pack()

frame_index = 0

def play_gif():
    global frame_index

    label.config(image=frames[frame_index])

    frame_index = (frame_index + 1) % len(frames)

    window.after(100, play_gif)

play_gif()

window.mainloop()