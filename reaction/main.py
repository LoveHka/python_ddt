from tkinter import *
from random import randint
from time import time, sleep

window = Tk()               # Создаём окно
window.geometry("400x300+1000+200")  # Задаём размеры

start_time = 0  # Сюда мы потом запишем время начала теста на реакцию
button_time = 0 # Сюда мы запишем, во сколько мы нажали на кнопку после начала

def start_game():
    global start_time, button_time
    flag.configure(text="...ЛЕСОПИЛКА...")
    sleep(randint(5000, 25000)/1000)
    button.configure(bg="green")

flag = Label(
    window,
    text="Нажмите на кнопку для старта...",
    font=("Arial", 16)
             )
flag.pack(pady=20)

button = Button(window, text="", width=10, height=2, bg="red", command=start_game)
button.pack(pady=10)


window.mainloop() # Запуск окна
