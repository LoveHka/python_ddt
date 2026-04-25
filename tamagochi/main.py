import tkinter as tk
from tkinter import ttk


#  🐱  😿  👻
#  🐶  😟  🦴
#  🤖  ⚙️  🔌
#  👽  🛸  ✨
#  🐉  🥚  🔥
#  🦄  ☁️  🌈
#  🐼  🎋  🐾
#  🦊  🌲  🍃
#  🐸  💧  🍄
#  🐧  ❄️  🧊

# ==========================================================
# КЛАСС ПИТОМЦА ( его Вам можно менять!!! )
# ==========================================================

class VirtualPet:
    def __init__(self):
        # 1. Характеристики (Число = появится полоска)
        self.имя = "Кеша"
        self.здоровье = 100
        self.счастье = 50
        self.сытость = 80

        # Вид питомца (эмодзи или текст)
        self.вид = "🐱"

    # 2. Действия (Название начинается с 'кнопка_' = появится кнопка)
    def кнопка_покормить(self):
        """Покормить питомца"""
        self.сытость = self.сытость + 20
        self.здоровье = self.здоровье + 2
        return "Ням-ням! +20 к сытости"

    def кнопка_поиграть(self):
        """Поиграть"""
        self.счастье = self.счастье + 15
        self.сытость -= 10
        return "Уиии! Как весело!"

    # Эта инструкция выполняется раз в секунду
    def жить_одну_секунду(self):
        self.сытость -= 2
        self.счастье -= 1

        if self.сытость <= 0:
            self.здоровье = self.здоровье - 5
            self.вид = "👻"
        elif self.сытость < 30:
            self.вид = "😿"
        else:
            self.вид = "🐱"

        # Если параметр больше 100, то не даем расти выше
        self.счастье = min(100, self.счастье)
        self.сытость = min(100, self.сытость)
        self.здоровье = min(100, self.здоровье)


# ==========================================================
# ДВИЖОК - Вот тут лучше ничего не менять )
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

        self.lbl_icon = tk.Label(self.main_container, text=self.pet.вид, font=("Arial", 80))
        self.lbl_icon.pack(pady=20)

        stats_frame = tk.Frame(self.main_container)
        stats_frame.pack(fill="x", padx=40)

        for attr, value in vars(self.pet).items():
            if isinstance(value, (int, float)) and attr != "вид":
                tk.Label(stats_frame, text=attr.capitalize(), font=("Arial", 10, "bold")).pack(anchor="w")
                progress = ttk.Progressbar(stats_frame, length=200, mode='determinate')
                progress.pack(fill="x", pady=(0, 10))
                self.stats_bars[attr] = progress

        self.log = tk.Label(self.main_container, text="Привет! Я твой питомец.", fg="blue",
                            font=("Arial", 10, "italic"))
        self.log.pack(pady=20)

        buttons_frame = tk.Frame(self.main_container)
        buttons_frame.pack(pady=10)

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

        # Проверка здоровья (скрытая логика)
        if getattr(self.pet, "здоровье", 100) <= 0:
            self.show_game_over()
            return

        self.lbl_icon.config(text=self.pet.вид)
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
