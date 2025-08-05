#import pyautogui
#import webbrowser
#import time

#webbrowser.open('file:///caminho/para/seu/index.html')
#time.sleep(5)

#x, y = 600, 400
#pyautogui.moveTo(x, y, duration=1)
#pyautogui.click()

#print("Botão clicado!")

#/-/-/-/-/-/-/-/-/-/-/
#Segunda  tentativa
#/-/-/-/-/-/-/-/-/-/-/

#import pyautogui
#import webbrowser
#import time

# Abre o arquivo HTML no navegador padrão (ajuste o caminho!)
#webbrowser.open('file:///caminho/para/seu/index.html')

# Espera a página abrir
#time.sleep(5)

# Coordenadas do botão (ajuste pro seu caso!)
#x, y = 600, 400

# Move o mouse lentamente até o botão (durante 2 segundos)
#pyautogui.moveTo(x, y, duration=2)

# Pausa 1 segundo (tipo um clique humano)
#time.sleep(1)

# Clica no botão
#pyautogui.click()

#print("Botão clicado!")

#/-/-/-/-/-/-/-/-/-/
#Terceira Tentativa
#/-/-/-/-/-/-/-/-/-/

#import pyautogui
#import webbrowser
#import time

# Abre o arquivo HTML
#webbrowser.open('file:///caminho/para/seu/index.html')

# Espera o navegador abrir
#time.sleep(5)

# Move o mouse para um ponto bem longe primeiro
#pyautogui.moveTo(100, 100, duration=1)

# Agora move até o botão com calma
#pyautogui.moveTo(600, 400, duration=3)

# Espera e clica
#time.sleep(1)
#pyautogui.click()

#print("Botão clicado!")

#/-/-/-/-/-/-/-/-/
#Quarta tentativa
#/-/-/-/-/-/-/-/-/


#import pyautogui
#import webbrowser
#import time

# Abre o HTML (troca o caminho)
#webbrowser.open('file:///C:/caminho/para/seu/index.html')

# Espera abrir
#time.sleep(5)

# Move o cursor lentamente pra você ver
#x, y = 600, 400
#pyautogui.moveTo(x, y, duration=2)

# Clica
#pyautogui.click()

#print("Botão clicado!")

# Impede o terminal de fechar
#input("Pressione Enter para encerrar.")

#/-/-/-/-/-/-/-/-/-/-/
#Quinta Tentativa
#/-/-/-/-/-/-/-/-/-/-/

#import pyautogui
#import time

#print("Preparando pra dançar...")

# Espera 3 segundos pra dar tempo de você ver
#time.sleep(3)

# Coordenadas de teste (canto superior esquerdo da tela)
#pyautogui.moveTo(100, 100, duration=2)
#pyautogui.moveTo(800, 300, duration=2)

#print("Show de movimentos finalizado.")
#input("Pressione Enter para sair.")

#/-/-/-/-/-/-/-/-/-/-/
#Sexta Tentativa
#/-/-/-/-/-/-/-/-/-/-/

#import pyautogui
#import math
#import time

# Centro do círculo
#cx, cy = 800, 500
#raio = 100

#print("Desenhando um círculo com o cursor em 3 segundos...")
#time.sleep(3)

#for i in range(360):
    #x = cx + raio * math.cos(math.radians(i))
    #y = cy + raio * math.sin(math.radians(i))
    #pyautogui.moveTo(x, y, duration=0.01)

#print("Show concluído.")

#Funcionou,moveu um pouco o cursor.
#Logo,o problema estava no tempo e nas cordenadas.