import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass
from abc import ABC, abstractmethod
import random
import math


# ==================== КЛАССЫ ДЛЯ ДЕМОНСТРАЦИИ ООП ====================

# 1. ИНКАПСУЛЯЦИЯ - скрываем внутренности, показываем только нужное
class Capsule:
    """Капсула здоровья - пример инкапсуляции"""
    def __init__(self, health=100):
        self.__health = health  # __ означает "скрыто!"
    
    def get_health(self):
        return self.__health
    
    def heal(self, amount):
        self.__health = min(100, self.__health + amount)
    
    def damage(self, amount):
        self.__health = max(0, self.__health - amount)


# 2. НАСЛЕДОВАНИЕ - дети наследуют от родителей
class Animal:
    """Родительский класс"""
    def __init__(self, name, emoji):
        self.name = name
        self.emoji = emoji
        self.hunger = 50
    
    def eat(self):
        self.hunger = max(0, self.hunger - 20)
    
    def get_info(self):
        return f"{self.emoji} {self.name} (сытость: {100 - self.hunger}%)"


class Cat(Animal):
    """Кот наследует от Animal"""
    def __init__(self, name):
        super().__init__(name, "🐱")
        self.purr_power = 10
    
    def purr(self):
        return f"{self.emoji} {self.name} мурчит: 'Муррр!' (сила: {self.purr_power})"


class Dog(Animal):
    """Собака наследует от Animal"""
    def __init__(self, name):
        super().__init__(name, "🐶")
        self.loyalty = 100
    
    def bark(self):
        return f"{self.emoji} {self.name} лает: 'Гав-гав!' (преданность: {self.loyalty}%)"


class Fox(Animal):
    """Лиса наследует от Animal"""
    def __init__(self, name):
        super().__init__(name, "🦊")
        self.cunning = 80
    
    def trick(self):
        return f"{self.emoji} {self.name} хитрит: 'Обману!' (хитрость: {self.cunning}%)"


# 3. ПОЛИМОРФИЗМ - одинаковые методы, разное поведение
class Sound(ABC):
    """Абстрактный класс для звуков"""
    @abstractmethod
    def make_sound(self):
        pass


class MeowSound(Sound):
    def make_sound(self):
        return "Мяу! Мяу!"


class BarkSound(Sound):
    def make_sound(self):
        return "Гав! Гав!"


class RoarSound(Sound):
    def make_sound(self):
        return "Р-р-р! Рёв!"


# ==================== ГЛАВНОЕ ПРИЛОЖЕНИЕ ====================

class OOPVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 ООП для Детей - Интерактивная Визуализация")
        self.root.geometry("1100x750")
        self.root.configure(bg="#f0f8ff")
        
        # Создаём персонажей
        self.cat = Cat("Мурзик")
        self.dog = Dog("Шарик")
        self.fox = Fox("Лисичка")
        self.animals = [self.cat, self.dog, self.fox]
        
        self.capsule = Capsule()
        
        self.current_tab = 0
        self.setup_ui()
        
    def setup_ui(self):
        """Настраиваем интерфейс"""
        # Заголовок
        title_frame = tk.Frame(self.root, bg="#4a90d9", height=60)
        title_frame.pack(fill="x", padx=0, pady=0)
        
        title = tk.Label(
            title_frame,
            text="🎓 Принципы ООП для Детей",
            font=("Arial", 24, "bold"),
            bg="#4a90d9",
            fg="white"
        )
        title.pack(pady=10)
        
        # Вкладки
        tab_frame = tk.Frame(self.root, bg="#f0f8ff")
        tab_frame.pack(fill="x", padx=20, pady=10)
        
        tabs = [
            ("📦 Инкапсуляция", 0),
            ("👨‍👧‍👦 Наследование", 1),
            ("🎭 Полиморфизм", 2),
            ("🎮 Игра", 3)
        ]
        
        self.tab_buttons = []
        for text, idx in tabs:
            btn = tk.Button(
                tab_frame,
                text=text,
                font=("Arial", 14, "bold"),
                bg="#e0e0e0",
                relief="raised",
                bd=3,
                command=lambda i=idx: self.show_tab(i)
            )
            btn.pack(side="left", padx=5, pady=5, fill="x", expand=True)
            self.tab_buttons.append(btn)
        
        # Контейнер для контента
        self.content_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.show_tab(0)
        
    def show_tab(self, tab_index):
        """Показываем выбранную вкладку"""
        self.current_tab = tab_index
        
        # Обновляем стиль кнопок
        for i, btn in enumerate(self.tab_buttons):
            if i == tab_index:
                btn.configure(bg="#4a90d9", fg="white")
            else:
                btn.configure(bg="#e0e0e0", fg="black")
        
        # Очищаем контент
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Показываем нужный контент
        if tab_index == 0:
            self.show_encapsulation()
        elif tab_index == 1:
            self.show_inheritance()
        elif tab_index == 2:
            self.show_polymorphism()
        elif tab_index == 3:
            self.show_game()
            
    def show_encapsulation(self):
        """Вкладка инкапсуляции"""
        # Заголовок
        tk.Label(
            self.content_frame,
            text="📦 ИНКАПСУЛЯЦИЯ - Прячем секретное!",
            font=("Arial", 20, "bold"),
            bg="#f0f8ff",
            fg="#333"
        ).pack(pady=5)
        
        tk.Label(
            self.content_frame,
            text="Как в сейфе: данные внутри защищены, но можно использовать кнопки!",
            font=("Arial", 12),
            bg="#f0f8ff",
            fg="#666"
        ).pack(pady=5)
        
        # Фрейм с капсулой
        capsule_frame = tk.Frame(self.content_frame, bg="#fff", relief="raised", bd=3)
        capsule_frame.pack(fill="both", expand=True, pady=10)
        
        # Визуализация капсулы
        canvas = tk.Canvas(capsule_frame, width=300, height=200, bg="#e8f4f8", highlightthickness=0)
        canvas.pack(side="left", padx=20, pady=20)
        
        # Рисуем капсулу
        self.draw_capsule(canvas)
        
        # Панель управления
        control_frame = tk.Frame(capsule_frame, bg="#fff")
        control_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)
        
        self.health_label = tk.Label(
            control_frame,
            text=f"❤️ Здоровье: {self.capsule.get_health()}",
            font=("Arial", 18, "bold"),
            bg="#fff",
            fg="#e74c3c"
        )
        self.health_label.pack(pady=20)
        
        # Прогресс-бар
        self.health_bar = ttk.Progressbar(
            control_frame,
            orient="horizontal",
            length=250,
            mode="determinate"
        )
        self.health_bar["value"] = self.capsule.get_health()
        self.health_bar.pack(pady=10)
        
        buttons_frame = tk.Frame(control_frame, bg="#fff")
        buttons_frame.pack(pady=20)
        
        tk.Button(
            buttons_frame,
            text="💊 Лечить (+20)",
            font=("Arial", 12, "bold"),
            bg="#2ecc71",
            fg="white",
            relief="raised",
            bd=3,
            command=lambda: self.update_health("heal")
        ).pack(side="left", padx=10)
        
        tk.Button(
            buttons_frame,
            text="💔 Повредить (-20)",
            font=("Arial", 12, "bold"),
            bg="#e74c3c",
            fg="white",
            relief="raised",
            bd=3,
            command=lambda: self.update_health("damage")
        ).pack(side="left", padx=10)
        
        # Объяснение
        info_frame = tk.Frame(self.content_frame, bg="#fff3cd", relief="raised", bd=2)
        info_frame.pack(fill="x", pady=10)
        
        tk.Label(
            info_frame,
            text="💡 Здоровье (__health) скрыто! Мы не можем изменить его напрямую.\n"
                 "Мы используем специальные методы heal() и damage() - это как кнопки на пульте!",
            font=("Arial", 11),
            bg="#fff3cd",
            fg="#856404",
            justify="left"
        ).pack(padx=10, pady=10)
        
        # Попробуем взломать
        hack_frame = tk.Frame(self.content_frame, bg="#f8d7da", relief="raised", bd=2)
        hack_frame.pack(fill="x", pady=5)
        
        tk.Label(
            hack_frame,
            text="🔒 Попробуй прочитать секретное поле __health напрямую:",
            font=("Arial", 11, "bold"),
            bg="#f8d7da",
            fg="#721c24"
        ).pack(padx=10, pady=5)
        
        tk.Button(
            hack_frame,
            text="🔑 Попробовать: capsule.__health",
            font=("Arial", 11),
            bg="#dc3545",
            fg="white",
            command=self.try_hack
        ).pack(pady=5)
        
        self.hack_result = tk.Label(hack_frame, text="", font=("Arial", 11, "bold"), bg="#f8d7da")
        self.hack_result.pack(pady=5)
        
    def draw_capsule(self, canvas):
        """Рисуем красивую капсулу"""
        # Тень
        canvas.create_oval(60, 100, 240, 190, fill="#d0d0d0", outline="")
        
        # Основная форма
        canvas.create_oval(50, 20, 250, 180, fill="#e74c3c", outline="#c0392b", width=3)
        
        # Блик
        canvas.create_oval(80, 30, 150, 100, fill="#ff6b6b", outline="")
        
        # Сердечко
        canvas.create_text(150, 100, text="❤️", font=("Arial", 50))
        
    def update_health(self, action):
        """Обновляем здоровье"""
        if action == "heal":
            self.capsule.heal(20)
        else:
            self.capsule.damage(20)
        
        health = self.capsule.get_health()
        self.health_label.config(text=f"❤️ Здоровье: {health}")
        self.health_bar["value"] = health
        
    def try_hack(self):
        """Пытаемся прочитать скрытое поле"""
        try:
            # Это вызовет ошибку!
            _ = self.capsule.__health
            self.hack_result.config(text="❌ Не должно работать!", fg="red")
        except AttributeError:
            self.hack_result.config(
                text="✅ Ошибка! Python не даёт прочитать __health напрямую! Инкапсуляция работает!",
                fg="green"
            )
            
    def show_inheritance(self):
        """Вкладка наследования"""
        tk.Label(
            self.content_frame,
            text="👨‍👧‍👦 НАСЛЕДОВАНИЕ - Дети похожи на родителей!",
            font=("Arial", 20, "bold"),
            bg="#f0f8ff",
            fg="#333"
        ).pack(pady=5)
        
        tk.Label(
            self.content_frame,
            text="Все животные наследуют от Animal: имя, эмодзи и голод. Но каждый добавляет своё!",
            font=("Arial", 12),
            bg="#f0f8ff",
            fg="#666"
        ).pack(pady=5)
        
        # Дерево наследования
        tree_frame = tk.Frame(self.content_frame, bg="#fff", relief="raised", bd=3)
        tree_frame.pack(fill="both", expand=True, pady=10)
        
        canvas = tk.Canvas(tree_frame, bg="#e8f4f8", height=200, highlightthickness=0)
        canvas.pack(fill="x", padx=20, pady=10)
        
        self.draw_inheritance_tree(canvas)
        
        # Карточки животных
        animals_frame = tk.Frame(self.content_frame, bg="#f0f8ff")
        animals_frame.pack(fill="both", expand=True, pady=10)
        
        self.animal_cards = {}
        for idx, animal in enumerate(self.animals):
            card = tk.Frame(animals_frame, bg="#fff", relief="raised", bd=2)
            card.grid(row=0, column=idx, padx=10, pady=10, sticky="nsew")
            animals_frame.columnconfigure(idx, weight=1)

            self.animal_cards[animal.name] = card  # Добавляем в словарь!

            tk.Label(
                card,
                text=animal.emoji,
                font=("Arial", 40),
                bg="#fff"
            ).pack(pady=5)
            
            tk.Label(
                card,
                text=animal.name,
                font=("Arial", 16, "bold"),
                bg="#fff"
            ).pack()
            
            tk.Label(
                card,
                text=f"Наследует от: Animal",
                font=("Arial", 9),
                bg="#fff",
                fg="#666"
            ).pack()
            
            hunger_label = tk.Label(
                card,
                text=f"Сытость: {100 - animal.hunger}%",
                font=("Arial", 12, "bold"),
                bg="#fff"
            )
            hunger_label.pack(pady=5)
            
            tk.Button(
                card,
                text="🍖 Покормить",
                font=("Arial", 11, "bold"),
                bg="#2ecc71",
                fg="white",
                command=lambda a=animal, l=hunger_label: self.feed_animal(a, l)
            ).pack(pady=5)
            
            # Уникальная способность
            if isinstance(animal, Cat):
                btn_text = "🎵 Мурчать"
            elif isinstance(animal, Dog):
                btn_text = "🔊 Лаять"
            else:
                btn_text = "🎪 Хитрить"
            
            result_label = tk.Label(card, text="", font=("Arial", 10), bg="#fff", fg="#333")
            result_label.pack(pady=5)
            
            tk.Button(
                card,
                text=btn_text,
                font=("Arial", 11),
                bg="#3498db",
                fg="white",
                command=lambda a=animal, l=result_label: self.show_ability(a, l)
            ).pack(pady=5)
        
    def draw_inheritance_tree(self, canvas):
        """Рисуем дерево наследования"""
        width = canvas.winfo_reqwidth() or 800
        
        # Animal (родитель)
        x_center = width // 2
        canvas.create_rectangle(x_center - 80, 20, x_center + 80, 70, fill="#3498db", outline="#2980b9", width=2)
        canvas.create_text(x_center, 45, text="🐾 Animal (Родитель)", fill="white", font=("Arial", 14, "bold"))
        
        # Линии к детям
        canvas.create_line(x_center, 70, x_center, 100, fill="#333", width=2)
        canvas.create_line(x_center - 200, 100, x_center + 200, 100, fill="#333", width=2)
        
        # Дети
        children = [
            (x_center - 200, "🐱 Cat", "#e74c3c"),
            (x_center, "🐶 Dog", "#f39c12"),
            (x_center + 200, "🦊 Fox", "#9b59b6")
        ]
        
        for x, name, color in children:
            canvas.create_line(x, 100, x, 130, fill="#333", width=2)
            canvas.create_rectangle(x - 60, 130, x + 60, 180, fill=color, outline="#333", width=2)
            canvas.create_text(x, 155, text=name, fill="white", font=("Arial", 12, "bold"))
        
    def feed_animal(self, animal, label):
        """Кормим животное"""
        animal.eat()
        label.config(text=f"Сытость: {100 - animal.hunger}%")
        
    def show_ability(self, animal, label):
        """Показываем способность животного"""
        if isinstance(animal, Cat):
            result = animal.purr()
        elif isinstance(animal, Dog):
            result = animal.bark()
        else:
            result = animal.trick()
        label.config(text=result)
        
    def show_polymorphism(self):
        """Вкладка полиморфизма"""
        tk.Label(
            self.content_frame,
            text="🎭 ПОЛИМОРФИЗМ - Одна команда, разный результат!",
            font=("Arial", 20, "bold"),
            bg="#f0f8ff",
            fg="#333"
        ).pack(pady=5)
        
        tk.Label(
            self.content_frame,
            text="make_sound() работает для всех, но каждый говорит по-своему!",
            font=("Arial", 12),
            bg="#f0f8ff",
            fg="#666"
        ).pack(pady=5)
        
        # Основная область
        main_frame = tk.Frame(self.content_frame, bg="#fff", relief="raised", bd=3)
        main_frame.pack(fill="both", expand=True, pady=10)
        
        # Область вывода
        self.sound_canvas = tk.Canvas(main_frame, bg="#e8f4f8", height=300, highlightthickness=0)
        self.sound_canvas.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Кнопки звуков
        buttons_frame = tk.Frame(self.content_frame, bg="#f0f8ff")
        buttons_frame.pack(fill="x", pady=10)
        
        sounds = [
            ("🐱 Кошка (Мяу)", "cat"),
            ("🐶 Собака (Гав)", "dog"),
            ("🦊 Лиса (Рёв)", "fox"),
            ("🎲 Все сразу!", "all")
        ]
        
        for text, animal_type in sounds:
            bg_color = "#e74c3c" if animal_type == "cat" else "#f39c12" if animal_type == "dog" else "#9b59b6" if animal_type == "fox" else "#2ecc71"
            
            tk.Button(
                buttons_frame,
                text=text,
                font=("Arial", 12, "bold"),
                bg=bg_color,
                fg="white",
                relief="raised",
                bd=3,
                command=lambda t=animal_type: self.play_sound(t)
            ).pack(side="left", padx=10, pady=10, fill="x", expand=True)
        
        # Объяснение
        info_frame = tk.Frame(self.content_frame, bg="#d1ecf1", relief="raised", bd=2)
        info_frame.pack(fill="x", pady=10)
        
        tk.Label(
            info_frame,
            text="💡 Полиморфизм = 'много форм'. Одинаковый метод make_sound(),\n"
                 "но кошка мяукает, собака лает, а лиса рычит!",
            font=("Arial", 11),
            bg="#d1ecf1",
            fg="#0c5460",
            justify="left"
        ).pack(padx=10, pady=10)
        
    def play_sound(self, animal_type):
        """Воспроизводим звук"""
        self.sound_canvas.delete("all")
        
        width = self.sound_canvas.winfo_reqwidth() or 800
        
        if animal_type == "all":
            # Все животные издают звуки
            sounds = [
                ("🐱 Мурзик", "Мяу! Мяу!", "#e74c3c", width // 4),
                ("🐶 Шарик", "Гав! Гав!", "#f39c12", width // 2),
                ("🦊 Лисичка", "Р-р-р! Рёв!", "#9b59b6", 3 * width // 4)
            ]
            
            for name, sound, color, x in sounds:
                # Облачко
                self.draw_speech_bubble(self.sound_canvas, x, 100, name, sound, color)
        else:
            animals = {"cat": self.cat, "dog": self.dog, "fox": self.fox}
            sounds_map = {"cat": "Мяу! Мяу!", "dog": "Гав! Гав!", "fox": "Р-р-р! Рёв!"}
            colors_map = {"cat": "#e74c3c", "dog": "#f39c12", "fox": "#9b59b6"}
            
            animal = animals[animal_type]
            sound = sounds_map[animal_type]
            color = colors_map[animal_type]
            
            self.draw_speech_bubble(self.sound_canvas, width // 2, 100, f"{animal.emoji} {animal.name}", sound, color)
            
    def draw_speech_bubble(self, canvas, x, y, name, sound, color):
        """Рисуем облачко с текстом"""
        # Облачко
        canvas.create_oval(x - 80, y - 40, x + 80, y + 40, fill=color, outline="#333", width=2)
        canvas.create_polygon(x - 20, y + 35, x, y + 60, x + 20, y + 35, fill=color, outline="#333", width=2)
        
        canvas.create_text(x, y - 15, text=name, fill="white", font=("Arial", 12, "bold"))
        canvas.create_text(x, y + 10, text=sound, fill="white", font=("Arial", 14, "bold"))
        
    def show_game(self):
        """Вкладка с мини-игрой"""
        tk.Label(
            self.content_frame,
            text="🎮 ИГРА - Проверь свои знания ООП!",
            font=("Arial", 20, "bold"),
            bg="#f0f8ff",
            fg="#333"
        ).pack(pady=5)
        
        self.score = 0
        self.question_index = 0
        
        self.questions = [
            {
                "question": "Что такое ИНКАПСУЛЯЦИЯ?",
                "options": [
                    "Прятать данные внутри класса",
                    "Создавать много классов",
                    "Копировать код"
                ],
                "correct": 0
            },
            {
                "question": "Что такое НАСЛЕДОВАНИЕ?",
                "options": [
                    "Получать деньги от бабушки",
                    "Дочерний класс берёт свойства родительского",
                    "Удалять классы"
                ],
                "correct": 1
            },
            {
                "question": "Что такое ПОЛИМОРФИЗМ?",
                "options": [
                    "Один метод - разный результат для разных объектов",
                    "Много классов в файле",
                    "Переименование переменных"
                ],
                "correct": 0
            },
            {
                "question": "Как скрыть поле в Python?",
                "options": [
                    "Написать secret_поле",
                    "Использовать __ перед именем",
                    "Спрятать за монитор"
                ],
                "correct": 1
            },
            {
                "question": "Что делает super()?",
                "options": [
                    "Делает супергероя",
                    "Вызывает метод родителя",
                    "Удаляет объект"
                ],
                "correct": 1
            }
        ]
        
        # Основная область
        game_frame = tk.Frame(self.content_frame, bg="#fff", relief="raised", bd=3)
        game_frame.pack(fill="both", expand=True, pady=10)
        
        # Счёт
        self.score_label = tk.Label(
            game_frame,
            text="⭐ Счёт: 0 / 0",
            font=("Arial", 16, "bold"),
            bg="#fff",
            fg="#f39c12"
        )
        self.score_label.pack(pady=10)
        
        # Вопрос
        self.question_label = tk.Label(
            game_frame,
            text="",
            font=("Arial", 16, "bold"),
            bg="#fff",
            fg="#333",
            wraplength=700,
            justify="center"
        )
        self.question_label.pack(pady=20)
        
        # Варианты ответов
        self.options_frame = tk.Frame(game_frame, bg="#fff")
        self.options_frame.pack(fill="both", expand=True, pady=10, padx=50)
        
        # Результат
        self.result_label = tk.Label(
            game_frame,
            text="",
            font=("Arial", 14, "bold"),
            bg="#fff"
        )
        self.result_label.pack(pady=10)
        
        # Кнопка далее
        self.next_button = tk.Button(
            game_frame,
            text="➡️ Далее",
            font=("Arial", 14, "bold"),
            bg="#3498db",
            fg="white",
            state="disabled",
            command=self.next_question
        )
        self.next_button.pack(pady=10)
        
        self.show_question()
        
    def show_question(self):
        """Показываем вопрос"""
        if self.question_index >= len(self.questions):
            self.show_final_result()
            return
        
        q = self.questions[self.question_index]
        self.question_label.config(text=f"❓ Вопрос {self.question_index + 1}: {q['question']}")
        
        # Очищаем старые кнопки
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        # Создаём кнопки ответов
        for idx, option in enumerate(q["options"]):
            btn = tk.Button(
                self.options_frame,
                text=f"{idx + 1}. {option}",
                font=("Arial", 13),
                bg="#e0e0e0",
                relief="raised",
                bd=2,
                command=lambda i=idx: self.check_answer(i)
            )
            btn.pack(fill="x", pady=5, padx=20)
        
        self.result_label.config(text="")
        self.next_button.config(state="disabled")
        
    def check_answer(self, selected):
        """Проверяем ответ"""
        q = self.questions[self.question_index]
        correct = q["correct"]
        
        if selected == correct:
            self.score += 1
            self.result_label.config(text="✅ Правильно! Молодец!", fg="green")
        else:
            self.result_label.config(
                text=f"❌ Неправильно. Правильный ответ: {q['options'][correct]}",
                fg="red"
            )
        
        self.score_label.config(text=f"⭐ Счёт: {self.score} / {self.question_index + 1}")
        self.next_button.config(state="normal")
        
        # Отключаем все кнопки
        for widget in self.options_frame.winfo_children():
            widget.config(state="disabled")
        
    def next_question(self):
        """Следующий вопрос"""
        self.question_index += 1
        self.show_question()
        
    def show_final_result(self):
        """Финальный результат"""
        total = len(self.questions)
        
        self.question_label.config(text="🎉 Игра окончена!")
        
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        if self.score == total:
            emoji = "🏆"
            message = "Ты гений ООП! Все правильно!"
        elif self.score >= total * 0.7:
            emoji = "🌟"
            message = "Отлично! Ты хорошо знаешь ООП!"
        else:
            emoji = "💪"
            message = "Попробуй ещё раз, у тебя получится!"
        
        tk.Label(
            self.options_frame,
            text=f"{emoji}\n{self.score}/{total} правильных ответов\n\n{message}",
            font=("Arial", 18, "bold"),
            bg="#fff",
            fg="#333",
            justify="center"
        ).pack(pady=20)
        
        self.next_button.config(text="🔄 Начать заново", command=self.restart_game)
        self.next_button.config(state="normal")
        
    def restart_game(self):
        """Перезапускаем игру"""
        self.score = 0
        self.question_index = 0
        self.score_label.config(text="⭐ Счёт: 0 / 0")
        self.next_button.config(text="➡️ Далее", command=self.next_question)
        self.show_question()


def main():
    root = tk.Tk()
    app = OOPVisualizer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
