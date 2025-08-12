import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# -*- coding: utf-8 -*-
"""bot.py

Este script é um exemplo de como usar o Selenium para testar uma aplicação web.
Ele abre uma página, verifica o título, clica em um botão e valida o conteúdo da próxima tela.

Certifique-se de ter o Selenium e o WebDriver Manager instalados:
pip install selenium webdriver-manager
"""

# Configuração do Chrome para rodar em modo headless (sem interface gráfica)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# Inicialização do driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
# Teste básico de navegação com Selenium
try:
    # 1. Abrir a página inicial
    driver.get('http://localhost:8000')

    # 2. Esperar a página carregar (usar explicit waits em código real)
    time.sleep(2)

    # 3. Verificar se o título está correto
    assert "Título esperado" in driver.title, "Título da página não bate"

    # 4. Verificar um elemento na tela inicial, por exemplo, um botão
    botao = driver.find_element(By.ID, 'id_do_botao_inicial')
    assert botao.is_displayed(), "Botão inicial não está visível"

    # 5. Clicar no botão e ir para próxima tela
    botao.click()
    time.sleep(2)

    # 6. Verificar se apareceu algo esperado na tela seguinte
    texto = driver.find_element(By.XPATH, '//h1')
    assert "Texto esperado" in texto.text, "Texto da tela seguinte não bate"

    print("Testes rodaram com sucesso!")

except Exception as e:
    print(f"Erro nos testes: {e}")

finally:
    driver.quit()
