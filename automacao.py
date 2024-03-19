# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui 
import pandas as pd
import time

arquivo = pd.read_csv("produtos.csv")

# Definindo tempo de espera entre os comandos
pyautogui.PAUSE = 0.4

# Abrir sistema
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# Caso o sistema em questão seja o chrome, os clicks são necessários para a seleção do perfil
# pyautogui.click(x=632, y=522)
# pyautogui.click(x=632, y=522)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Esperar carregamento da pagina
time.sleep(3)

# Fazer login no sistema
pyautogui.click(x=444, y=407)
pyautogui.write("email@email.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.click(x=715, y=568)

for linha in arquivo.index:
    pyautogui.click(x=447, y=289) # primeiroBOHA000251  Hashtag  campo feito por click para evitar erros
    pyautogui.write(str(arquivo.loc[linha, "codigo"]))
    pyautogui.press("tab")
    # Repetir as duas linhas acima para todos os campos
    pyautogui.write(str(arquivo.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(arquivo.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(arquivo.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(arquivo.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(arquivo.loc[linha, "custo"]))
    pyautogui.press("tab")

    if not pd.isna(arquivo.loc[linha, "obs"]):
        pyautogui.write(str(arquivo.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    