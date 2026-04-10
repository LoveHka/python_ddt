import socket           # Для интернета
import threading        # Многопоточность
import tkinter as tk    # Интерфейс

HOST = "192.168.31.232" # Адрес компьютера
PORT = 7000             # Адрес программы

sock = socket.socket()  # Создаем устройство для подключения
sock.connect((HOST, PORT))  # Подключаемся к серверу

root = tk.Tk()              # Главное окно
root.title("Чат ДДТ !!!")   # Название программы
root.configure(bg="#2f2f2f")

text = tk.Text(root, height=30, width=100, font=("", 14))  # Добавляем окошко с текстом
text.pack()                         # Кладем его на главное окно

frame = tk.Frame(root)          # Контейнер для ввода
frame.pack()                    # Кладем контейнер в окно

entry = tk.Entry(frame, width=70, font=("", 18))   # Создаем поле для ввода
entry.pack(side="left")             # Кладем в контейнер слева направо

def send():             # Функция для отправки сообщения
    msg = entry.get() + "\n"    # берем данные из ввода
    sock.sendall(msg.encode())  # Отправляем сообщение на сервер
    entry.delete(0, tk.END) # Полностью очищаем ввод

btn = tk.Button(frame, text="Отправить", command=send) # Кнопка отправки
btn.pack(side="left")       # Кладем вслед за полем ввода

root.bind("<Return>", lambda event: btn.invoke())

def recive():   # Функция для получения сообщений
    while True: # Бесконечго делаем
        try:    # Пробуем получить сообщение -----
            data = sock.recv(1024)   # Получить сообщение
            if not data:            # Если оно пустое или с ошибками
                break               # Значит разрываем соединение


            message = data.decode() # Раскодируем информацию

            text.insert(tk.END, message) # Вставляем сообщение в конец текста
            text.see(tk.END) # Прокручиваем текст в самый низ

        except: # Если случилась ошибка, отключаемся ----
            text.insert(tk.END, "УПС! СЕРВЕР потерялся...")
            text.see(tk.END)
            break

threading.Thread(target=recive, daemon=True).start()
# Слушаем сообщения в отдельном потоке
root.mainloop()
# Запускаем главный цикл
