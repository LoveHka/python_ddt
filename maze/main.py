import tkinter as tk
import random
import time

# =================================================================
# БЛОК 1: ДВИЖОК СИСТЕМЫ (НЕ РЕДАКТИРОВАТЬ)
# =================================================================
class MazeEngine:
    def __init__(self, mode_dynamic=False):
        self.size = 10  # Размер поля 10x10
        self.cell_size = 50
        self.dynamic = mode_dynamic
        self.root = tk.Tk()
        self.root.title("Robot Maze Runner v1.0")
        
        self.canvas = tk.Canvas(self.root, width=self.size*self.cell_size, 
                                height=self.size*self.cell_size, bg="white")
        self.canvas.pack()
        
        self.maze = []
        self.robot_pos = [0, 0]
        self.exit_pos = [self.size-1, self.size-1]
        self.generate_maze()
        self.draw_maze()
        self.robot_img = self.canvas.create_oval(5, 5, 45, 45, fill="royalblue")

    def generate_maze(self):
        # Простая генерация: 0 - пусто, 1 - стена
        self.maze = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for r in range(self.size):
            for c in range(self.size):
                if random.random() < 0.25: # 25% шанс появления стены
                    self.maze[r][c] = 1
        self.maze[0][0] = 0 # Старт всегда свободен
        self.maze[self.exit_pos[0]][self.exit_pos[1]] = 0 # Выход свободен

    def draw_maze(self):
        for r in range(self.size):
            for c in range(self.size):
                color = "white"
                if self.maze[r][c] == 1: color = "#2c3e50" # Стена
                if [r, c] == self.exit_pos: color = "#27ae60" # Финиш
                self.canvas.create_rectangle(c*self.cell_size, r*self.cell_size,
                                             (c+1)*self.cell_size, (r+1)*self.cell_size,
                                             fill=color, outline="#ecf0f1")

    def move_robot(self, direction):
        r, c = self.robot_pos
        new_r, new_c = r, c
        
        if direction == "вверх": new_r -= 1
        elif direction == "вниз": new_r += 1
        elif direction == "влево": new_c -= 1
        elif direction == "вправо": new_c += 1
        
        # Проверка границ и стен
        if 0 <= new_r < self.size and 0 <= new_c < self.size:
            if self.maze[new_r][new_c] == 0:
                self.robot_pos = [new_r, new_c]
                self.canvas.coords(self.robot_img, 
                                   new_c*self.cell_size+5, new_r*self.cell_size+5,
                                   (new_c+1)*self.cell_size-5, (new_r+1)*self.cell_size-5)
                self.root.update()
                return True
        return False

    def get_sensors(self):
        """Возвращает информацию о соседних клетках для Алгоритма"""
        r, c = self.robot_pos
        return {
            "вверх": self.maze[r-1][c] if r > 0 else 1,
            "вниз": self.maze[r+1][c] if r < self.size-1 else 1,
            "влево": self.maze[r][c-1] if c > 0 else 1,
            "вправо": self.maze[r][c+1] if c < self.size-1 else 1
        }

    def run_manual(self, commands):
        time.sleep(1)
        for cmd in commands:
            success = self.move_robot(cmd.lower())
            if not success:
                print(f"Робот ударился или застрял на команде: {cmd}")
                break
            time.sleep(0.3)
        self.check_win()

    def run_ai(self, logic_func):
        time.sleep(1)
        steps = 0
        while self.robot_pos != self.exit_pos and steps < 100:
            sensors = self.get_sensors()
            next_step = logic_func(sensors)
            if not self.move_robot(next_step):
                print("Алгоритм выбрал неверный путь!")
                break
            steps += 1
            time.sleep(0.2)
        self.check_win()

    def check_win(self):
        if self.robot_pos == self.exit_pos:
            print("ПОБЕДА! Робот нашел выход.")
            self.canvas.create_text(self.size*self.cell_size/2, self.size*self.cell_size/2, 
                                   text="ВЫХОД НАЙДЕН!", fill="gold", font=("Arial", 30, "bold"))
        else:
            print("Робот не добрался до финиша.")
        self.root.mainloop()

# =================================================================
# БЛОК 2: ЗОНА УЧЕНИКА (РЕДАКТИРОВАТЬ ТУТ)
# =================================================================

# 1. Выбери режим: False - статичный лабиринт, True - меняющийся (умный режим)
DYNAMIC_MODE = False

# ВАРИАНТ А: Если режим DYNAMIC_MODE = False
# Просто напиши список команд: "вверх", "вниз", "влево", "вправо"
manual_commands = [
    "вправо", "вправо", "вниз", "вниз", "вправо", 
    "вниз", "вниз", "вправо", "вправо", "вниз"
]

# ВАРИАНТ Б: Если режим DYNAMIC_MODE = True
# Напиши логику. sensors - это словарь, где 0 - путь свободен, 1 - стена.
def ai_logic(sensors):
    # Пример простой логики: если справа свободно - идем направо, иначе вниз
    if sensors["вправо"] == 0:
        return "вправо"
    else:
        return "вниз"


# Запуск системы
if __name__ == "__main__":
    engine = MazeEngine(mode_dynamic=DYNAMIC_MODE)
    
    if DYNAMIC_MODE:
        engine.run_ai(ai_logic)
    else:
        engine.run_manual(manual_commands)
