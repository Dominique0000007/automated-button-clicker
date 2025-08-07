import pyautogui
import webbrowser
import time
webbrowser.open("http://127.0.1:5500/Tcc/test/index.html")
time.sleep(5)
pyautogui.FAILSAFE = True  # Ativa o recurso de segurança do PyAutoGUI
pyautogui.PAUSE = 1  # Pausa de 1 segundo entre os comandos
x, y = 600, 400
pyautogui.moveTo(x, y, duration=2)
time.sleep(1)
time.clicks(100000)
print("Botão clicado!")
input("Pressione Enter para encerrar.")
