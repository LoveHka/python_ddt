from tkinter import *
from random import randint
from time import time

window = Tk()               # Создаём окно
window.geometry("400x300+1000+200")  # Задаём размеры

start_time = 0  # Сюда мы потом запишем время начала теста на реакцию
button_time = 0 # Сюда мы запишем, во сколько мы нажали на кнопку после начала
reaction_time = 0   # Время реакции

def start_game():
    global start_time
    flag.configure(text="Жди...")
    window.after(randint(5000,10000), green_flag)
    start_time = 0
    button.configure(bg = "red", command=end_game)

def green_flag():
    global start_time, button_time
    button.configure(bg="green",)
    start_time = time() # Отмечаем время, когда кнопка стала зелёной

def end_game():
    global start_time, button_time, reaction_time
    if start_time == 0:
        flag.configure(text="Фальстарт!")
        button.configure(command=start_game)
        return
    button_time = time() # Отмечаем, когда кнопка была нажата
    reaction_time = button_time - start_time  # Узнаём время реакции
    result = str(reaction_time)[:5]
    flag.configure(text= f"Время реакции: {result} секунд" )
    button.configure(command=start_game)

flag = Label(
    window,
    text="Нажмите на кнопку для старта...",
    font=("Arial", 16)
             )
flag.pack(pady=20)

button = Button(window, text="", width=15, height=3, bg="red", command=start_game)
button.pack(pady=10)


window.mainloop() # Запуск окна
