
import tkinter as tk

#cria janela2
janela3 = tk.Tk()
janela3.title("Cadastro Finalizado")
janela3.geometry("400x200") #tamanho da tela

#janela por cima
janela3.attributes("-topmost", True)

#cor fundo verde
janela3.configure(bg='green')

#Cria um label com a msg estilizada
mensagem = tk.Label(janela3, text="TODOS OS GRUPOS AVLS\nFORAM ASSOCIADOS", font=("Arial", 18, "bold"), bg='green', fg='white')
mensagem.pack(expand=True)

