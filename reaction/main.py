from tkinter import *
from random import randint
from time import time

window = Tk()               # Создаём окно
window.geometry("300x300+1000+200")  # Задаём размеры


flag = Label(window, text="Нажмите на кнопку для старта...")
flag.pack(pady=20)

button = Button(window, text="", width=10, height=2, bg="red")
button.pack(pady=10)


window.mainloop() # Запуск окна
