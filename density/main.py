import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

from random import randint

def main():
    print("🔢 Введите числа по одному в строке.")
    print("🛑 Для завершения введите пустую строку или 'q' и нажмите Enter.")
    print("-" * 55)

    data = []
    while True:
        try:
            line = input("> ").strip()
            if line.lower() in ("", "q", "quit"):
                break
            data.append(float(line))
        except ValueError:
            print("⚠️ Это не число. Попробуйте снова.")
        except EOFError:
            break
    

    if len(data) < 3:
        print("❌ Нужно минимум 3 числа, чтобы построить осмысленное распределение.")
        return

    # Запрашиваем ширину интервала
    bin_input = input("📏 Введите ширину интервала (по умолчанию 0.2): ").strip()
    bin_width = float(bin_input) if bin_input else 0.2

    # Создаём массив границ интервалов с заданным шагом
    min_val, max_val = min(data), max(data)
    start = np.floor(min_val / bin_width) * bin_width
    stop  = np.ceil(max_val / bin_width) * bin_width + bin_width
    bins = np.arange(start, stop, bin_width)

    # --- Построение графика ---
    plt.figure(figsize=(10, 6))
    
    # 1. Гистограмма с заданными интервалами
    # density=True нормирует площадь гистограммы до 1, чтобы она совпадала по масштабу с плавной кривой
    n, bins_out, patches = plt.hist(data, bins=bins, density=True,
                                    alpha=0.6, color='skyblue', edgecolor='black',
                                    linewidth=1.2, label='Гистограмма')

    # 2. Плавная кривая распределения (KDE)
    kde = gaussian_kde(data)
    x_smooth = np.linspace(min_val - 2*bin_width, max_val + 2*bin_width, 500)
    plt.plot(x_smooth, kde(x_smooth), color='crimson', linewidth=2.5, 
             label='Плавная оценка плотности (KDE)')

    # Среднее значение для наглядности
    mean_val = np.mean(data)
    plt.axvline(mean_val, color='green', linestyle='--', linewidth=1.5, 
                label=f'Среднее: {mean_val:.2f}')

    plt.title("Распределение введённых значений", fontsize=16, pad=15)
    plt.xlabel("Значение", fontsize=12)
    plt.ylabel("Плотность вероятности", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(fontsize=11)
    plt.tight_layout()
    plt.show()

main()
