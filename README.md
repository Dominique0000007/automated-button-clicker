````markdown
# Mouse Auto Click Bot

Automação simples em Python usando PyAutoGUI para mover o cursor do mouse e clicar em botões numa interface gráfica. Ideal para testes básicos de UI e demonstrações de automação para Quality Assurance (QA).

---

## Funcionalidades

- Abre uma página HTML local no navegador  
- Move o mouse até as coordenadas do botão (configurável)  
- Clica no botão, que dispara um alerta na página  
- Movimento do cursor visível e controlado com duração para simular interação humana

---

## Pré-requisitos

- Python 3.x instalado  
- Biblioteca PyAutoGUI instalada (`pip install pyautogui`)  
- Navegador padrão configurado para abrir arquivos HTML locais

---

## Como usar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
````

2. Configure o caminho do arquivo HTML no script Python:

```python
webbrowser.open('file:///C:/caminho/para/seu/index.html')
```

3. Ajuste as coordenadas do botão no script (`x, y`) para a posição correta na sua tela.

4. Execute o script:

```bash
python bot_click.py
```

---

## Dicas para QA

* Use a função `pyautogui.position()` para identificar coordenadas do mouse na tela.
* Evite mover o mouse manualmente durante a execução para não atrapalhar a automação.
* Execute o script com permissões adequadas (ex: administrador no Windows) para evitar bloqueios.

---

## Próximos passos

* Implementar reconhecimento de botão por imagem (visão computacional)
* Automatizar testes mais complexos com Selenium e PyAutoGUI combinados
* Criar logs detalhados para monitoramento das ações do bot

---

## Autor

Lara Souza — Técnico em Desenvolvimento de Sistemas
Contato: \[[seu-email@exemplo.com](mailto:seu-email@exemplo.com)]

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

