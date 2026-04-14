# 🐱 Визуальный Тамагочи для детей — показываем ООП в действии!
# Запусти: python oop_visualize.py

import tkinter as tk
from tkinter import ttk
import random


# ============================================
# 📦 КЛАСС — это чертёж нашего питомца
# ============================================
class Cat:
    """Класс Cat — чертёж, по которому создаётся наш котик-тамагочи"""

    def __init__(self, name):
        # 🔧 self.xxx — это свойства (параметры) объекта
        self.name = name         # имя котика
        self.health = 100        # ❤️ здоровье
        self.hunger = 100        # 🍖 сытость
        self.happiness = 100     # 😊 счастье
        self.energy = 100        # ⚡ энергия
        self.is_sleeping = False # спит или нет
        self.message = f"Привет! Я {self.name}! 🐱"

    def feed(self):
        """Метод feed() — покормить котика"""
        if self.is_sleeping:
            self.message = f"💤 {self.name} спит, не буди!"
            return
        self.hunger = min(100, self.hunger + 25)
        self.health = min(100, self.health + 5)
        self.message = f"🍖 {self.name} покушал! Ням-ням!"

    def play(self):
        """Метод play() — поиграть с котиком"""
        if self.is_sleeping:
            self.message = f"💤 {self.name} спит, тссс!"
            return
        if self.energy < 10:
            self.message = f"😫 {self.name} слишком устал для игр!"
            return
        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 15)
        self.hunger = max(0, self.hunger - 10)
        self.message = f"🎾 {self.name} играет! Весело!"

    def sleep(self):
        """Метод sleep() — уложить котика спать"""
        if self.is_sleeping:
            self.message = f"💤 {self.name} и так спит!"
            return
        self.is_sleeping = True
        self.message = f"😴 {self.name} засыпает..."

    def wake_up(self):
        """Метод wake_up() — разбудить котика"""
        self.is_sleeping = False
        self.message = f"😊 {self.name} проснулся!"

    def live(self):
        """Метод live() — жизнь идёт, параметры немного падают"""
        if self.is_sleeping:
            # Пока спит — восстанавливает энергию
            self.energy = min(100, self.energy + 5)
            self.health = min(100, self.health + 2)
            if self.energy >= 100:
                self.wake_up()
                self.message = f"😊 {self.name} выспался и проснулся!"
        else:
            self.hunger = max(0, self.hunger - 3)
            self.happiness = max(0, self.happiness - 2)
            self.energy = max(0, self.energy - 2)
            # Если что-то на нуле — здоровье падает
            if self.hunger <= 0 or self.happiness <= 0:
                self.health = max(0, self.health - 3)

        if self.health <= 0:
            exit()

    def get_mood(self):
        """Метод get_mood() — какое настроение у котика?"""
        avg = (self.health + self.hunger + self.happiness + self.energy) / 4
        if self.is_sleeping:
            return "sleeping"
        if avg >= 80:
            return "happy"
        if avg >= 50:
            return "normal"
        if avg >= 25:
            return "sad"
        return "critical"


# ============================================
# 🖥️ ГРАФИЧЕСКИЙ ИНТЕРФЕЙС (Tkinter)
# ============================================
class TamagotchiGUI:
    """Класс GUI — рисует окно, кнопки и обновляет картинку"""

    def __init__(self):
        # Создаём объект-котик из класса Cat
        self.cat = Cat("Барсик")

        # Главное окно
        self.root = tk.Tk()
        self.root.title("🐱 Тамагочи ")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        self._build_ui()
        # Таймер: каждые 2000 мс (2 сек) вызываем live()
        self.root.after(2000, self._game_tick)

    def _build_ui(self):
        """Строим весь интерфейс"""
        self._draw_header()
        self._draw_cat_face()
        self._draw_bars()
        self._draw_buttons()
        self._draw_message()
        self._draw_ood_panel()

    def _draw_header(self):
        """Шапка с именем котика"""
        header = tk.Label(
            self.root,
            text="🐱 Мой Тамагочи — ООП для детей!",
            font=("Arial", 16, "bold"),
            bg="#FFDAB9",
        )
        header.pack(fill="x", pady=(0, 5))

    def _draw_cat_face(self):
        """Рисуем мордочку котика (будет меняться)"""
        self.cat_face = tk.Label(
            self.root,
            text="😺",
            font=("Segoe UI Emoji", 80),
        )
        self.cat_face.pack(pady=10)

    def _draw_bars(self):
        """Рисуем 4 прогресс-бара"""
        frame = tk.Frame(self.root, bg="#FFE4C4", padx=15, pady=10)
        frame.pack(fill="x", padx=20)

        self.bars = {}  # храним ссылки на бары и лейблы
        params = [
            ("health", "❤️ Здоровье", "#FF4444"),
            ("hunger", "🍖 Сытость", "#FF8C00"),
            ("happiness", "😊 Счастье", "#FFD700"),
            ("energy", "⚡ Энергия", "#00AA00"),
        ]
        for attr, label, color in params:
            row = tk.Frame(frame, bg="#FFE4C4")
            row.pack(fill="x", pady=3)

            tk.Label(row, text=label, font=("Arial", 10), bg="#FFE4C4", width=14, anchor="w").pack(side="left")

            bar = ttk.Progressbar(row, orient="horizontal", length=250, mode="determinate")
            bar.pack(side="left", padx=5)

            val_label = tk.Label(row, text="100", font=("Arial", 9), bg="#FFE4C4", width=4)
            val_label.pack(side="left")

            self.bars[attr] = {"bar": bar, "label": val_label, "color": color}

    def _draw_buttons(self):
        """Кнопки действий"""
        btn_frame = tk.Frame(self.root, bg="#FFE4C4")
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame, text="🍖 Покормить", font=("Arial", 12), width=12, bg="#FF8C00", fg="white",
            command=self._on_feed,
        ).pack(side="left", padx=5)

        tk.Button(
            btn_frame, text="🎾 Поиграть", font=("Arial", 12), width=12, bg="#FFD700", fg="black",
            command=self._on_play,
        ).pack(side="left", padx=5)

        tk.Button(
            btn_frame, text="😴 Спать", font=("Arial", 12), width=12, bg="#4444FF", fg="white",
            command=self._on_sleep,
        ).pack(side="left", padx=5)

    def _draw_message(self):
        """Сообщение от котика"""
        self.msg_label = tk.Label(
            self.root, text=self.cat.message,
            font=("Arial", 12, "bold"), fg="#333", bg="#FFE4C4",
        )
        self.msg_label.pack(pady=5)

    def _draw_ood_panel(self):
        """Панель ООП — показывает self.xxx в реальном времени"""
        frame = tk.LabelFrame(
            self.root, text="📦 ООП — Что внутри объекта self?",
            font=("Arial", 11, "bold"), bg="#E8E8FF", fg="#333",
        )
        frame.pack(fill="x", padx=20, pady=10)

        self.ood_text = tk.Text(frame, font=("Consolas", 10), height=9, bg="#E8E8FF", fg="#222", bd=0)
        self.ood_text.pack(fill="x", padx=10, pady=5)

    def _update_bars(self):
        """Обновляем все прогресс-бары"""
        for attr, info in self.bars.items():
            value = getattr(self.cat, attr)
            info["bar"]["value"] = value
            info["label"].config(text=str(int(value)), fg=info["color"])

    def _update_cat_face(self):
        """Меняем эмодзи котика по настроению"""
        mood = self.cat.get_mood()
        faces = {
            "sleeping": "😴",
            "happy": "😺",
            "normal": "🐱",
            "sad": "😿",
            "critical": "🙀",
        }
        self.cat_face.config(text=faces[mood])

    def _update_message(self):
        self.msg_label.config(text=self.cat.message)

    def _update_ood_panel(self):
        """Показываем, что хранится внутри self — связь с ООП!"""
        last_method = getattr(self, "_last_method", "—")
        text = f"""# Объект: self = Cat("{self.cat.name}")
# Метод вызван: {last_method}

self.name       = "{self.cat.name}"
self.health     = {int(self.cat.health)}
self.hunger     = {int(self.cat.hunger)}
self.happiness  = {int(self.cat.happiness)}
self.energy     = {int(self.cat.energy)}
self.is_sleeping= {self.cat.is_sleeping}"""
        self.ood_text.delete("1.0", tk.END)
        self.ood_text.insert("1.0", text)

    def _refresh(self):
        """Обновить весь экран"""
        self._update_bars()
        self._update_cat_face()
        self._update_message()
        self._update_ood_panel()

    def _game_tick(self):
        """Каждые 2 секунды: кот живёт своей жизнью"""
        self.cat.live()
        self._last_method = "live() — таймер"
        self._refresh()
        self.root.after(2000, self._game_tick)

    # ---- Обработчики кнопок ----

    def _on_feed(self):
        self._last_method = "cat.feed()"
        self.cat.feed()
        self._refresh()

    def _on_play(self):
        self._last_method = "cat.play()"
        self.cat.play()
        self._refresh()

    def _on_sleep(self):
        if self.cat.is_sleeping:
            self._last_method = "cat.wake_up()"
            self.cat.wake_up()
        else:
            self._last_method = "cat.sleep()"
            self.cat.sleep()
        self._refresh()

    def run(self):
        """Запуск приложения"""
        self._refresh()
        self.root.mainloop()


# ============================================
# 🚀 ЗАПУСК!
# ============================================
if __name__ == "__main__":
    app = TamagotchiGUI()
    app.run()
