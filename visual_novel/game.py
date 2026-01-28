from tkinter import *

window = Tk() # Создаём окно
window.title(" Беконечное лето 2.0 ") # Название окна
window.geometry("600x300")  # Размеры окна

game = {
    "сцена 1": {
        "текст": "Ты пришёл на урок по программировнию.",
        "ответы": [
            ("Уйти", "попытка уйти"),
            ("Остаться", "печаль")
        ]
    },
    "попытка уйти": {
        "текст" : "Ты попытался уйти, но учитель тебя заметил и закрыл дверь.",
        "ответы" :  [
            ("Остаться и учиться...", "печаль")
        ]
    },
    "печаль" : {
        "текст" : "Ты остался и долго писал код, твои пальцы устали и ты попал во временную петлю...",
        "ответы" : [
            ("Временную петлю???...", "печаль"),
        ]
    }
}

def show_scene(scene_name):
    for widget in window.winfo_children():  
        widget.destroy()        # Удаляем все старые кнопки и текст
    
    scene = game[scene_name] # Загрузить нужную нам сцену

    text = Label(window, text=scene["текст"], wraplength=400)
    text.pack()                  # Рисуем новый текст

    for knopka in scene["ответы"]:      ## Рисуем новые кнопки
        button = Button(window, text=knopka[0], command=lambda x=knopka[1]: show_scene(x))
        button.pack()


show_scene("сцена 1")       # Запускаем первую сцену
window.mainloop() # Запуск приложения
