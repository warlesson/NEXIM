import pyautogui
import os
from time import sleep
from datetime import datetime
import telafinal3
contador = 1

with open ("job.avl", "r") as arquivo:
    for linha in arquivo:
        valores = linha.strip().split(',')
        uni = valores[0]

        pyautogui.doubleClick(780,730, duration=1.5) #clicar em part number
        pyautogui.hotkey('ctrl', 'a') # seleciona o que esta no campo de procura
        pyautogui.press('backspace') # apagar qualquer coisa na area de procura
        pyautogui.write(uni) #copia o part original como alv name nome do grupo
        pyautogui.click(273,760, duration=1.5) #clicar no part
        pyautogui.rightClick(273,760, duration=0.5) #clicar com o direito
        # função criar pasta e tirar print
        # Captura a tela
        screenshot = pyautogui.screenshot(region=(1626, 503, 290, 310))
                # Gerar o nome da pasta (exemplo: pasta1, pasta2, etc)
        pasta_nome = f"PASTA_{contador}_{uni}"
        contador += 1
                # Caminho completo para a pasta
        area_de_trabalho = os.path.expanduser("~/Desktop/AVL/")
        caminho_pasta = os.path.join(area_de_trabalho, pasta_nome)
                # Cria a pasta, se não existir
        os.makedirs(caminho_pasta, exist_ok=True)
                # Caminho completo para o arquivo de imagem
        caminho_imagem = os.path.join(caminho_pasta, f"{uni}.png")
                # Salva a captura de tela
        screenshot.save(caminho_imagem)
        print(f"Imagem salva em: {caminho_imagem}")

        sleep(3.5)
        pyautogui.click(290,377, duration=2) #clicar em edit part info
        pyautogui.click(1107,552, duration=1.5) #clica em part avl
        pyautogui.hotkey('ctrl', 'a') # seleciona tudo do NA
        pyautogui.press('backspace') # apagar qualquer coisa na area de procura
        pyautogui.write(uni) # COPIA O PART IRIGINAL
        pyautogui.click(880,747, duration=1.5) # CLICAR PARA ESCOLHER SAME PART NUMBER
        pyautogui.click(880,817, duration=1.5) #clicar em OK SAME PART NUMBER
        pyautogui.click(876,802, duration=1.5) #clicar em OK para associar
        
        print('linha processada')
telafinal3.janela3.mainloop() 