# Passo a passo

# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

pyautogui.PAUSE = 0.5

# abrir o navegador (operaGX)
pyautogui.press("win")
pyautogui.write("opera")
time.sleep(0.5)
pyautogui.press("enter")

# entrar no link 
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")



# Passo 2: Fazer login
time.sleep(0.5)
# selecionar o campo de email
pyautogui.press('tab')
# escrever o seu email
pyautogui.write("emaildeteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

# Passo 4: Cadastrar um produto
pyautogui.PAUSE = 0.1
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=743, y=242)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
