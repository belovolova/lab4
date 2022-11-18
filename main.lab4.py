import tkinter as tk
import pygame
import random
from threading import Thread
import time


# 1 вариант
def task(A):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V',
               'W', 'X', 'Y']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    A = (random.choices(letters, k=3)) + (random.choices(numbers, k=2))
    random.shuffle(A)
    a = ''.join(A)
    return a


def clicked():
    lbl.result1.configure(text=task(A=0))
    lbl.result2.configure(text=task(A=0))
    lbl.result3.configure(text=task(A=0))


# анимация
def flashing():
    while True:
        btn.config(bg='mediumvioletred')
        time.sleep(0.1)
        btn.config(bg='violet')
        time.sleep(0.1)
        btn.config(bg='orchid')
        time.sleep(0.1)
        btn.config(bg='hotpink')
        time.sleep(0.1)


# интерфейс
window = tk.Tk()
window.geometry('1280x590')
bg = tk.PhotoImage(file='hello1.png')
w = tk.Label(window, image=bg)
w.place(x=0, y=0)

lbl = tk.Label(window, text="Hello Kitty", font=("Arial Bold", 40), bg="white", fg="mediumvioletred")
lbl.grid(column=1000, row=500)
lbl.place(x=500, y=40)

btn = tk.Button(window, text="LET'S GO", font=("Arial Bold", 30), bg="white", fg="black", command=clicked)
btn.grid(column=1, row=28)

lbl.result1 = tk.Label(window, text='      ...      ', font=("Arial Bold", 20), bg="white", fg="mediumvioletred")
lbl.result1.grid(column=2, row=2)
lbl.result1.place(x=800, y=180)

lbl.result2 = tk.Label(window, text='      ...      ', font=("Arial Bold", 20), bg="white", fg="mediumvioletred")
lbl.result2.grid(column=2, row=2)
lbl.result2.place(x=800, y=280)

lbl.result3 = tk.Label(window, text='      ...      ', font=("Arial Bold", 20), bg="white", fg="mediumvioletred")
lbl.result3.grid(column=2, row=2)
lbl.result3.place(x=800, y=380)

# музыка
music = 'музыка.фон.mp3'
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.play()

btn.pack()
Thread(target=flashing, args=[], daemon=True).start()
btn.place(x=340, y=250)

window.mainloop()
