#/-/-/-/-/-/-/-/-/-/-/
#Nona Tentativa
#/-/-/-/-/-/-/-/-/-/-/

import pyautogui
import webbrowser
import time
webbrowser.open("http://127.0.1:5500/Tcc/test/index.html")
time.sleep(100) # Espera 100 segundos para abrir o navegador
# Espera o navegador carregar
time.sleep(5) # Espera 5 segundos para o navegador carregar
# Move o mouse para a posição do botão e clica
# Ajuste as coordenadas (x, y) conforme necessário
# As coordenadas (600, 400) são um exemplo, você deve substituir pelos valores corretos
pyautogui.FAILSAFE = True  # Ativa o recurso de segurança do PyAutoGUI
pyautogui.PAUSE = 1  # Pausa de 1 segundo entre os comandos
# Move o mouse para a posição do botão e clica
# Ajuste as coordenadas (x, y) conforme necessário
# As coordenadas (600, 400) são um exemplo, você deve substituir pelos valores corretos
pyautogui.FAILSAFE = True  # Ativa o recurso de segurança do PyAutoGUI
pyautogui.PAUSE = 1  # Pausa de 1 segundo entre os comandos
# Move o mouse para a posição do botão e clica
# Ajuste as coordenadas (x, y) conforme necessário
# As coordenadas (600, 400) são um exemplo, você deve substituir pelos valores corretos
x, y = 600, 400
pyautogui.moveTo(x, y, duration=2)
time.sleep(1)   # Espera 1 segundo antes de clicar
time.clicks(100000)  # Clica com o botão esquerdo do mouse
# Clica no botão
pyautogui.click()
# Exibe uma mensagem de confirmação
print("Botão clicado!")
# Impede o terminal de fechar
input("Pressione Enter para encerrar.")