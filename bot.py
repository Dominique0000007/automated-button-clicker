import pyautogui
import webbrowser
import time

# Abre a página
webbrowser.open("http://127.0.0.1:5500/Tcc/test/index.html")
time.sleep(5)  # espera a página carregar

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

# Procura a posição do botão na tela
print("Procurando o botão na tela...")
posicao = pyautogui.locateOnScreen('botao.png', confidence=0.8)  # confiança 80%

if posicao is not None:
    print(f"Botão encontrado na posição: {posicao}")
    centro = pyautogui.center(posicao)
    pyautogui.moveTo(centro.x, centro.y, duration=1)
    pyautogui.click()
    print("Botão clicado!")
else:
    print("Botão NÃO encontrado na tela. Confere a imagem e a tela.")

input("Pressione Enter para encerrar.")
