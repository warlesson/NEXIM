import pyautogui
from time import sleep
import telafinal

with open ("job.avl", "r") as arquivo:
    for linha in arquivo:
        valores = linha.strip().split(',')
        uni = valores[0]
        del valores[0]
        for valor in valores:
            pyautogui.click(100,267, duration=3) #clicar para digitar part
            pyautogui.hotkey('ctrl', 'a') # seleciona o que esta no campo de procura
            pyautogui.press('backspace') # apagar qualquer coisa na area de procura
            pyautogui.write(uni) # copia o part original
            pyautogui.rightClick(151,429, duration=1.5) # clica com o botao direito no part original    
                # OBS: TROCAR (141,453) (151,429)   
            pyautogui.click(185,536, duration=1.5) # clica em copy as  
                # OBS: TROCAR (203,557) (185,536) 
            pyautogui.hotkey('ctrl', 'a')    
            pyautogui.press('backspace') # apaga o que esta em copy as
            pyautogui.click(934,567, duration=1.5) #clica para digitar
            pyautogui.write(valor) # digita o part alternativo
            pyautogui.click(998,653, duration=1.5) # clica em ok para criar part 
        
        print('linha processada')
telafinal.janela.mainloop() 


