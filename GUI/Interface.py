from tkinter import *
from PIL import Image
from PIL import ImageTk

root = Tk()
root.title('Audio Synthesizer')
root.minsize(480, 400)
root.configure(background='gray')

title = Label(root, text="Audio Synthesizer", width=500, bg="black", fg="white", padx=20, pady=20, font=("Roboto", 20))
title.pack()

frequency = Label(root, text="Frequency (fs):", bg="gray", fg="white", padx=20, pady=20, font=("Roboto", 12)).place(x=50, y=100)
# frequency_input_area = Entry(root, width=40).place(x=40, y=150)
frame = Frame(root, borderwidth=2, relief=SUNKEN)
entry = Entry(frame, borderwidth=8, relief=FLAT)
entry.pack()
frame.place(x=220, y=110)

array = Label(root, text="Array :", bg="gray", fg="white", padx=20, pady=20, font=("Roboto", 12)).place(x=50, y=200)
# frequency_input_area = Entry(root, width=40).place(x=40, y=150)
frame2 = Frame(root, borderwidth=2, relief=SUNKEN, width=300)
entry2 = Entry(frame2, borderwidth=8, relief=FLAT)
entry2.pack()
frame2.place(x=220, y=210)

w = Button ( root, width="30", text="Play", bg="green", fg="white", padx=10, pady=10, font=("Roboto", 12)).place(x=60, y=320)

root.mainloop()