import pyautogui
from time import sleep


with open ("Pratica/job.avl", "r") as arquivo:
    for linha in arquivo:
        valores = linha.strip().split(',')
        uni = valores[0]

        del valores[0]
        for valor in valores:
            pyautogui.click(237,267, duration=1) #clicar para digitar part
            pyautogui.hotkey('ctrl', 'a') # seleciona o que esta no campo de procura
            pyautogui.press('backspace') # apagar qualquer coisa na area de procura
            pyautogui.write(valor) # copia o part original
            pyautogui.rightClick(139,428, duration=1) # clica com o botao direito no part original coordenadas 140,449          139,428
            pyautogui.click(172,557, duration=1) # clica para deletar coordenadas 176,574               172,557
            pyautogui.press('enter')

        
        print('linha processada')

