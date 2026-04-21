import tkinter as tk
from tkinter import ttk
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5

    def feed(self):
        self.hunger += 2
        self.happiness -= 1

    def play(self):
        self.hunger -= 1
        self.happiness += 2

    def tick(self):
        self.hunger -= 1
        self.happiness -= 1

def make_tab(notebook, pet):
    frame = tk.Frame(notebook)
    label = tk.Label(frame)
    label.pack(pady=10)

    def update():
        pet.tick()
        label.config(text=f"""
        Имя: \t{pet.name}
        Голод: \t{pet.hunger}
        Счастье: \t{pet.happiness}
""")
        frame.after(2000, update)

    def feed():
        pet.feed()
        update()
    def play():
        pet.play()
        update()

    tk.Button(frame, text="Кормить", command=feed).pack()
    tk.Button(frame, text="Играть", command=play).pack()

    notebook.add(frame, text = pet.name)

    update()

root = tk.Tk()
root.title("Тамагочи")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

make_tab(notebook, Pet("Мурка"))
make_tab(notebook, Pet("ОЛЕГ"))

root.mainloop()
