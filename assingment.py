import tkinter as tk
import playsound as p
from tkinter import *
from tkinter import ttk

def playsound(event):
    print(event)
    p.playsound("dog-barking-70772.mp3",block=False)

def playsound2(event):
    print(event)
    p.playsound("Cats-loud-meow-sound-clips.mp3",block=False)

def playsound3(event):
    print(event)
    p.playsound("075176_duck-quack-40345.mp3",block=False)

def playsound4(event):
    print(event)
    p.playsound("mooing-cow-122255.mp3",block=False)

def playsound5(event):
    print(event)
    p.playsound("chicken-talk-30453.mp3",block=False)


win = tk.Tk()
win.geometry("500x200")
win.attributes('-topmost',True)

dog = PhotoImage(file = "dog.png" )
label1 = tk.Label(win, image = dog)

l1 =  tk.Button(win,text="dog")
l1.bind("<Button>",playsound)

cat = PhotoImage(file = "cat.png")
label2 = tk.Label(win, image = cat)
l2 =  tk.Button(win,text="cat")
l2.bind("<Button>",playsound2)

duck = PhotoImage(file = "duck.png")
label3 = tk.Label(win, image = duck )
l3 =  tk.Button(win,text="duck")
l3.bind("<Button>",playsound3)

cow = PhotoImage(file = "cow.png")
label4 = tk.Label(win, image = cow)
l4 =  tk.Button(win,text="cow")
l4.bind("<Button>",playsound4)

chicken = PhotoImage(file = "chicken.png")
label5 = tk.Label(win, image = chicken)
l5 =  tk.Button(win,text="chicken")
l5.bind("<Button>",playsound5)

l1.place(x = 30, y = 145)
l2.place(x = 130, y = 145)
l3.place(x = 230, y = 145)
l4.place(x = 330, y = 145)
l5.place(x = 430, y = 145)
label1.place(x = 25, y = 50, height =  100, width = 100)
label2.place(x = 130, y = 50, height =  100, width = 100)
label3.place(x = 230, y = 50, height =  100, width = 100)
label4.place(x = 330, y = 50, height =  100, width = 100)
label5.place( x = 430, y = 50, height =  100, width = 100)

win.mainloop()
