import tkinter as tk
from tkinter import ttk
import os

# ==========================================================
# 🖼️ НАСТРОЙКИ ИЗОБРАЖЕНИЙ (ВСТАВЬТЕ СВОИ ПУТИ СЮДА!)
# ==========================================================
# Убедитесь, что файлы имеют формат .gif или .png
IMAGE_FILES = {
    "happy": "happy_cat.gif",  # Обычное состояние
    "sad": "sad_cat.gif",  # Сытость < 30
    "ghost": "ghost_cat.gif"  # Сытость <= 0
}


# ==========================================================
# КЛАСС ПИТОМЦА
# ==========================================================
class VirtualPet:
    def __init__(self):
        self.имя = "Кеша"
        self.здоровье = 100
        self.счастье = 50
        self.сытость = 80

        # Загружаем изображения сразу, чтобы они не пропали из памяти
        self.images = {}
        self.current_state = "happy"  # Текущее состояние для отображения

        for state, filename in IMAGE_FILES.items():
            if os.path.exists(filename):
                try:
                    # PhotoImage должен быть сохранен в переменную объекта, иначе исчезнет
                    self.images[state] = tk.PhotoImage(file=filename)
                except Exception as e:
                    print(f"Ошибка загрузки {filename}: {e}")
                    self.images[state] = None
            else:
                print(f"Файл не найден: {filename}")
                self.images[state] = None

    def кнопка_покормить(self):
        """Покормить питомца"""
        self.сытость = min(100, self.сытость + 20)
        self.здоровье = min(100, self.здоровье + 2)
        return "Ням-ням! +20 к сытости"

    def кнопка_поиграть(self):
        """Поиграть"""
        self.счастье = min(100, self.счастье + 15)
        self.сытость -= 10
        return "Уиии! Как весело!"

    # Эта инструкция выполняется раз в секунду
    def жить_одну_секунду(self):
        self.сытость -= 2
        self.счастье -= 1

        # Логика смены состояния (вида)
        if self.сытость <= 0:
            self.здоровье = max(0, self.здоровье - 5)
            self.current_state = "ghost"
        elif self.сытость < 30:
            self.current_state = "sad"
        else:
            self.current_state = "happy"

        # Ограничиваем значения максимумом 100
        self.счастье = min(100, self.счастье)
        self.сытость = min(100, self.сытость)
        self.здоровье = min(100, self.здоровье)


# ==========================================================
# ДВИЖОК
# ==========================================================
class PetApp:
    def __init__(self, root, pet_instance):
        self.pet = pet_instance
        self.root = root
        self.is_running = True
        self.root.title(f"Tamagotchi: {getattr(self.pet, 'имя', 'Pet')}")
        self.root.geometry("400x600")

        self.stats_bars = {}
        self.setup_ui()
        self.update_loop()

    def setup_ui(self):
        self.main_container = tk.Frame(self.root)
        self.main_container.pack(expand=True, fill="both")

        # --- Иконка питомца ---
        # Пробуем поставить картинку, если нет - ставим эмодзи
        initial_img = self.pet.images.get(self.pet.current_state)

        if initial_img:
            self.lbl_icon = tk.Label(self.main_container, image=initial_img)
            self.lbl_icon.image = initial_img  # Сохраняем ссылку!
        else:
            self.lbl_icon = tk.Label(self.main_container, text="🐱", font=("Arial", 80))

        self.lbl_icon.pack(pady=20)
        down = tk.Frame(self.main_container)
        down.pack(fill="x", padx=40)



        # --- Полоски характеристик ---
        stats_frame = tk.Frame(down)
        stats_frame.pack(side="left", fill="x", padx=40)

        for attr, value in vars(self.pet).items():
            # Пропускаем служебные поля и картинки
            if isinstance(value, (int, float)) and attr not in ["images"]:
                tk.Label(stats_frame, text=attr.capitalize(), font=("Arial", 10, "bold")).pack(anchor="w")
                progress = ttk.Progressbar(stats_frame, length=200, mode='determinate')
                progress.pack(fill="x", pady=(0, 10))
                self.stats_bars[attr] = progress

        # --- Лог сообщений ---
        self.log = tk.Label(down, text="Привет! Я твой питомец.", fg="blue",
                            font=("Arial", 10, "italic"))
        self.log.pack(side="left")

        # --- Кнопки действий ---
        buttons_frame = tk.Frame(down)
        buttons_frame.pack(side="left")

        for method_name in dir(self.pet):
            if method_name.startswith("кнопка_"):
                pretty_name = method_name.replace("кнопка_", "").replace("_", " ").capitalize()
                btn = tk.Button(
                    buttons_frame, text=pretty_name, width=20, height=2,
                    command=lambda m=method_name: self.run_action(m)
                )
                btn.pack(pady=5)

    def run_action(self, method_name):
        if not self.is_running: return
        method = getattr(self.pet, method_name)
        message = method()
        if message: self.log.config(text=message)
        self.refresh_ui()

    def show_game_over(self):
        self.is_running = False
        for widget in self.root.winfo_children():
            widget.destroy()

        lbl = tk.Label(
            self.root,
            text="Питомец расстроился\nи ушел...",
            font=("Arial", 18, "bold"),
            fg="red",
            justify="center"
        )
        lbl.pack(expand=True)

    def refresh_ui(self):
        if not self.is_running: return

        # Проверка здоровья
        if getattr(self.pet, "здоровье", 100) <= 0:
            self.show_game_over()
            return

        # Обновляем картинку
        new_img = self.pet.images.get(self.pet.current_state)
        if new_img:
            self.lbl_icon.config(image=new_img)
            self.lbl_icon.image = new_img  # Важно: сохраняем ссылку на новую картинку
        else:
            # Если картинки нет, показываем эмодзи по состоянию
            emoji_map = {"happy": "🐱", "sad": "😿", "ghost": "👻"}
            self.lbl_icon.config(text=emoji_map.get(self.pet.current_state, "❓"), font=("Arial", 80))

        # Обновляем полоски
        for attr, bar in self.stats_bars.items():
            val = getattr(self.pet, attr)
            bar['value'] = val

    def update_loop(self):
        if self.is_running:
            if hasattr(self.pet, 'жить_одну_секунду'):
                self.pet.жить_одну_секунду()
            self.refresh_ui()
            self.root.after(1000, self.update_loop)


if __name__ == "__main__":
    root = tk.Tk()
    my_pet = VirtualPet()
    app = PetApp(root, my_pet)
    root.mainloop()
