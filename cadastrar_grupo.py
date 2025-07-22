import pyautogui
from time import sleep
import telafinal2

with open ("job.avl", "r") as arquivo:
    for linha in arquivo:
        valores = linha.strip().split(',')
        uni = valores[0]

        pyautogui.rightClick(210,412, duration=1.5) #clicar com o botao direito
        pyautogui.click(233,423, duration=1.5) #clicar em new
        pyautogui.write(uni) #copia o part original como alv name nome do grupo
        pyautogui.click(1131,756, duration=1.5) #clicar em criar avl name
        sleep(3.5)
        pyautogui.click(634,253, duration=2) # clica para colocar o primeiro part
        pyautogui.write(uni) # digitar part 1
        pyautogui.press('enter')

        del valores[0]
        a = 0
        for valor in valores:
            pyautogui.click(x=638,y=a+274,  duration=2)
            pyautogui.write(valor)
            pyautogui.press('enter')
            a+=20           

        pyautogui.click(1531,981, duration=2)
        pyautogui.click(1909,139, duration=2)
        print('linha processada')
telafinal2.janela2.mainloop()       
