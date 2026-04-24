import tkinter as tk
import random
import time


# =================================================================
# БЛОК 1: ДВИЖОК СИСТЕМЫ (НЕ РЕДАКТИРОВАТЬ)
# =================================================================
class MazeEngine:
    def __init__(self, mode_dynamic=False):
        self.size = 15  # Увеличили масштаб для красоты
        self.cell_size = 40
        self.dynamic = mode_dynamic
        self.root = tk.Tk()
        self.root.title("Advanced Maze Runner 2.0")

        self.canvas = tk.Canvas(self.root, width=self.size * self.cell_size,
                                height=self.size * self.cell_size, bg="#ecf0f1")
        self.canvas.pack()

        self.maze = [[1 for _ in range(self.size)] for _ in range(self.size)]
        self.robot_pos = [0, 0]
        self.exit_pos = [self.size - 1, self.size - 1]

        self._generate_real_maze(0, 0)
        self.maze[self.exit_pos[0]][self.exit_pos[1]] = 0  # Гарантируем выход
        self.draw_maze()

        self.robot_img = self.canvas.create_oval(8, 8, 32, 32, fill="#3498db", outline="#2980b9", width=2)

    def _generate_real_maze(self, r, c):
        """Генерация лабиринта методом DFS (глубинный поиск)"""
        self.maze[r][c] = 0
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.size and 0 <= nc < self.size and self.maze[nr][nc] == 1:
                self.maze[r + dr // 2][c + dc // 2] = 0  # Ломаем стену между клетками
                self._generate_real_maze(nr, nc)

    def draw_maze(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.maze[r][c] == 1:
                    self.canvas.create_rectangle(c * self.cell_size, r * self.cell_size,
                                                 (c + 1) * self.cell_size, (r + 1) * self.cell_size,
                                                 fill="#2c3e50", outline="#34495e")
                if [r, c] == self.exit_pos:
                    self.canvas.create_text(c * self.cell_size + 20, r * self.cell_size + 20,
                                            text="🏁", font=("Arial", 16))

    def move_robot(self, direction):
        r, c = self.robot_pos
        move_map = {"вверх": (-1, 0), "вниз": (1, 0), "влево": (0, -1), "вправо": (0, 1)}
        dr, dc = move_map.get(direction.lower(), (0, 0))
        new_r, new_c = r + dr, c + dc

        if 0 <= new_r < self.size and 0 <= new_c < self.size and self.maze[new_r][new_c] == 0:
            self.robot_pos = [new_r, new_c]
            self.canvas.coords(self.robot_img, new_c * self.cell_size + 8, new_r * self.cell_size + 8,
                               (new_c + 1) * self.cell_size - 8, (new_r + 1) * self.cell_size - 8)
            self.root.update()
            return True
        return False

    def get_sensors(self):
        r, c = self.robot_pos
        check = lambda dr, dc: self.maze[r + dr][c + dc] if 0 <= r + dr < self.size and 0 <= c + dc < self.size else 1
        return {"вверх": check(-1, 0), "вниз": check(1, 0), "влево": check(0, -1), "вправо": check(0, 1)}

    def run_manual(self, commands):
        self.root.after(500, lambda: self._execute_manual(commands))
        self.root.mainloop()

    def _execute_manual(self, commands):
        for cmd in commands:
            if not self.move_robot(cmd): break
            time.sleep(0.2)
        self._check_finish()

    def run_ai(self, logic_func):
        self.root.after(500, lambda: self._execute_ai(logic_func))
        self.root.mainloop()

    def _execute_ai(self, logic_func):
        steps = 0
        while self.robot_pos != self.exit_pos and steps < 300:
            cmd = logic_func(self.get_sensors())
            if not self.move_robot(cmd): break
            steps += 1
            time.sleep(0.1)
        self._check_finish()

    def _check_finish(self):
        if self.robot_pos == self.exit_pos:
            self.canvas.create_text(self.size * self.cell_size / 2, self.size * self.cell_size / 2,
                                    text="MISSION COMPLETE", fill="#f1c40f", font=("Courier", 24, "bold"))
        else:
            print("Робот заглох...")


# =================================================================
# БЛОК 2: ЗОНА УЧЕНИКА (РЕДАКТИРОВАТЬ ТУТ)
# =================================================================

# 1. Выбери режим: False (статичный путь) или True (алгоритм для нового лабиринта)
DYNAMIC_MODE = True
#
# # ВАРИАНТ А: Ручной список команд
# manual_commands = [
#     "вправо", "вниз", "вправо", "вправо", "вниз"  # И так далее до самого конца...
# ]


"""АЛГОРИТМ РОБОТА ПИСАТЬ ЗДЕСЬ!!!"""
# ВАРИАНТ Б: Алгоритм (для тех, кто хочет сделать "умного" робота)
def ai_logic(sensors):
    # sensors["вправо"] == 0 значит путь свободен. 1 - стена.
    # Попробуй написать условия, чтобы робот не бился в стены!

    if sensors["вправо"] == 0:
        return "вправо"
    elif sensors["вниз"] == 0:
        return "вниз"
    elif sensors["вверх"] == 0:
        return "вверх"
    else:
        return "влево"



engine = MazeEngine(mode_dynamic=DYNAMIC_MODE)
if DYNAMIC_MODE:
    engine.run_ai(ai_logic)
else:
    engine.run_manual(manual_commands)
