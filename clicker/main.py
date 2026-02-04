from tkinter import *

root = Tk()
root.geometry("800x400")
root.title("Кликер типа да")
######################
money = 0               # Деньги
house = 0               # Количество домов
helicopter = 0          # Количество вертолётов

def addMoney():
    global money
    money += 2       # Добавляем две монетки
    text.configure(text=f"{money} $")
def buyHouse():         # Покупка дома
    global house, money
    if money >= 100:
        house += 1
        money -= 100
def buyHelicopter():
    global helicopter, money
    if money >= 1000:
        money -= 1000
        helicopter += 1
def update():
    global money
    money += house * 1 + helicopter * 5
    text.configure(text=f"{money} $")
    information.configure(text=f"""
    Вертолётов: {helicopter}
    Домов:      {house}
    
    Заработок в секунду: {house * 1 + helicopter * 5}
""")

    root.after(1000, update)

###################
tools = Frame(root, bg="lightblue")
tools.pack(side="left", fill="y", pady=5, padx=5)

gameplay = Frame(root, bg="red")
gameplay.pack(expand = True, fill="both", pady=5, padx=5)

score = Frame(gameplay, bg="pink")
score.pack(fill="both", pady=5, padx=5)

text = Label(score, text="MONEY", font=("", 22))
text.pack(pady=5, padx=5)
but = Button(score, width=10, height=2, bg="black", command=addMoney)
but.pack(pady=5, padx=5)

info = Frame(gameplay, bg="yellow")
info.pack(expand=True, fill="both", pady=5, padx=5)

information = Label(info, text="У вас пока нет ничего...", font=("", 22))
information.pack(anchor="nw", padx=5, pady=5)

red_button = Button(tools, text="Дом\n100$", bg = "brown", height=3, width=10, font=("", 16), command=buyHouse)
blue_button = Button(tools,text="Вертолёт\n1000$", bg = "violet", height=3, width=10, font=("", 16), command=buyHelicopter)

red_button.pack(pady=5, padx=5)
blue_button.pack(pady=5, padx=5)

update()

mainloop()
