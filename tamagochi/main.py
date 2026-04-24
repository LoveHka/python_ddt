import tkinter as tk
from tkinter import ttk

# ==========================================================
# КЛАСС ПИТОМЦА
# ==========================================================

class VirtualPet:
    def __init__(self):
        # 1. Добавляем характеристики (Число = появится полоска)
        self.name = "Кеша"
        self.health = 100
        self.happiness = 50
        self.hunger = 80
        
        # Вид питомца ()
        self.icon = " :D "

    # 2. Добавляем действия (Название начинается с 'action_' = появится кнопка)
    def action_feed(self):
        """Покормить питомца"""
        self.hunger = min(100, self.hunger + 20)
        self.health = min(100, self.health + 2)
        return "Ням-ням! +20 к сытости"

    def action_play(self):
        """Поиграть"""
        if self.hunger > 10:  # Если 
            self.happiness = min(100, self.happiness + 15)
            self.hunger -= 10
            return "Уиии! Как весело!"
        else:
            return "Питомец слишком голоден для игр..."

    # Это действие выполняется раз в секунду
    def live_second(self):
        """Метод вызывается каждую секунду (логика жизни)"""
        self.hunger -= 2
        self.happiness -= 1
        
        if self.hunger <= 0:
            self.health -= 5
            self.icon = "end"
        elif self.hunger < 30:
            self.icon = "😿"
        else:
            self.icon = "🐱"

# ==========================================================
# ДАЛЬШЕ ЛУЧШЕ НИЧЕГО НЕ МЕНЯТЬ )))) 
#               ...хотя если очень хочется, то можно попробовать... 
# ==========================================================

class PetApp:
    def __init__(self, root, pet_instance):
        self.pet = pet_instance
        self.root = root
        self.root.title(f"Tamagotchi: {self.pet.name}")
        self.root.geometry("400x500")
        
        self.stats_vars = {}
        self.setup_ui()
        self.update_loop()

    def setup_ui(self):
        # Отображение иконки
        self.lbl_icon = tk.Label(self.root, text=self.pet.icon, font=("Arial", 80))
        self.lbl_icon.pack(pady=20)

        # Контейнер для стат
        stats_frame = tk.Frame(self.root)
        stats_frame.pack(fill="x", padx=20)

        # АВТОМАТИЧЕСКОЕ СОЗДАНИЕ ИНДИКАТОРОВ
        for attr, value in vars(self.pet).items():
            if isinstance(value, (int, float)) and attr != "icon":
                tk.Label(stats_frame, text=attr.capitalize()).pack(anchor="w")
                progress = ttk.Progressbar(stats_frame, length=200, mode='determinate')
                progress.pack(fill="x", pady=5)
                self.stats_vars[attr] = progress

        # Журнал событий
        self.log = tk.Label(self.root, text="Привет! Я твой питомец.", fg="blue")
        self.log.pack(pady=10)

        # АВТОМАТИЧЕСКОЕ СОЗДАНИЕ КНОПОК
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=20)

        for method_name in dir(self.pet):
            if method_name.startswith("action_"):
                btn_text = method_name.replace("action_", "").capitalize()
                btn = tk.Button(
                    buttons_frame, 
                    text=btn_text, 
                    width=15,
                    command=lambda m=method_name: self.run_action(m)
                )
                btn.pack(side="top", pady=2)

    def run_action(self, method_name):
        method = getattr(self.pet, method_name)
        message = method()
        self.log.config(text=message)
        self.refresh_ui()

    def refresh_ui(self):
        self.lbl_icon.config(text=self.pet.icon)
        for attr, progress in self.stats_vars.items():
            val = getattr(self.pet, attr)
            progress['value'] = val

    def update_loop(self):
        self.pet.live_second()
        self.refresh_ui()
        self.root.after(1000, self.update_loop)

root = tk.Tk()
my_pet = VirtualPet()
app = PetApp(root, my_pet)
root.mainloop()
