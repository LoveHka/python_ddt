from tkinter import *
import json

root = Tk()
root.geometry("800x400")
root.title("Кликер типа да")
######################
money = 0  # Деньги

items = {
    "Легковушка" : {
        "цена" : 40,
        "доход" : 5
    },
    "Автобус" : {
        "цена" : 80,
        "доход" : 12
    }
}

inventory = {
    "Легковушка" : 0,
    "Автобус" : 0
}

def SaveGame():
    data = {
        "money": money,
        "inventory": inventory
    }
    filename = inputin.get()
    if filename: # Если имя не пустое (то есть полльзователь что-то ввел)
        json.dump(data, open(f"{filename}.json", "w", encoding="utf-8"))    #Сохраняем
def LoadGame():
    global money, inventory
    filename = inputin.get()
    if filename:
        data = json.load(open(f"{filename}.json", "r", encoding="utf-8"))
        money = data["money"] # Сохраняем в деньги значение из файла
        inventory = data["inventory"] # Сохраняем в Инвентарь значение из файла

def addMoney():
    global money
    money += 2  # Добавляем две монетки
    text.configure(text=f"{money} $")

def BuySomething(something):
    global money, inventory
    if money >= items[something]["цена"]:
        inventory[something] += 1 # Увеличивем количество предмета в инвенторе
        money -= items[something]["цена"] # Уменьшаем количество денег

def update():
    global money

    for i in inventory:
        money += inventory[i] * items[i]['доход'] # Добавляем доход от каждого предмета

    text.configure(text=f"{money} $")   # Обновим инфу о денежках

    to_show = "Вы уже приобрели:\n" # временная строка
    for i in inventory:
        if inventory[i] > 0:
            to_show += f"{i}: {inventory[i]} \n" # Добавляем Название: количество

    information.configure(text=to_show) # Показываем всё на экране

    root.after(1000, update)


###################
tools = Frame(root, bg="lightblue")
tools.pack(side="left", fill="y", pady=5, padx=5)

gameplay = Frame(root, bg="red")
gameplay.pack(expand=True, fill="both", pady=5, padx=5)

score = Frame(gameplay, bg="pink")
score.pack(fill="both", pady=5, padx=5)

text = Label(score, text="MONEY", bg="pink", font=("", 22))
text.pack(pady=5, padx=5)
but = Button(score, width=20, height=4, text="CLICK!", bg="red", command=addMoney)
but.pack(pady=5, padx=5)

info = Frame(gameplay, bg="yellow")
info.pack(expand=True, fill="both", pady=5, padx=5)

information = Label(info, bg="yellow", text="У вас пока нет ничего...", font=("", 22))
information.pack(anchor="nw", padx=5, pady=5)

buttons = [] # Сюда положим все-все кнопки для покупки
for item in items:
    btn = Button(tools,
                 text=f"{item}\n{items[item]['цена']}$ / + {items[item]['доход']}$",
                 width=20, height=2,
                 command=lambda x=item: BuySomething(x))
    btn.pack(pady=5, padx=5)
    buttons.append(btn)
# Для загрузки файлов ( И выгрузки )
loading = Frame(gameplay)
loading.pack(padx=5,pady=5)

inputin = Entry(loading)
inputin.pack(side="left", padx=5,pady=5, expand = True)

save = Button(loading, text="Сохранить", command=SaveGame)
save.pack(side="left", pady=5,padx=5)
load = Button(loading, text="Загрузить", command=LoadGame)
load.pack(side="left", pady=5,padx=5)

update()

mainloop()
