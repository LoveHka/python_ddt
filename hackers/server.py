import socket
import threading
import tkinter as tk

from pyexpat.errors import messages

HOST = "192.168.31.232"
PORT = 7000

# ---- SOCKET ------
sock = socket.socket()
sock.connect((HOST, PORT))

# --- ИНтерфейс ---
root = tk.Tk()
root.title("Chat DDT")

text = tk.Text(root, height=40, width=100)
text.pack()

frame = tk.Frame(root)
frame.pack()

entry = tk.Entry(frame, width = 80)

entry.pack(side="left")

def send():
    msg = entry.get() + "\n"
    if msg:
        sock.sendall(msg.encode())
        entry.delete(0, tk.END)


btn = tk.Button(frame, text="Отправить", command=send)
btn.pack(side="left")

def recive():
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break

            message = data.decode()

            text.insert(tk.END, message)

            text.see(tk.END)
        except:
            break

threading.Thread(target=recive, daemon=True).start()

root.mainloop()
