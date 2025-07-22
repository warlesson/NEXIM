
import tkinter as tk

#cria janela2
janela2 = tk.Tk()
janela2.title("Cadastro Finalizado")
janela2.geometry("400x200") #tamanho da tela

#janela por cima
janela2.attributes("-topmost", True)

#cor fundo verde
janela2.configure(bg='green')

#Cria um label com a msg estilizada
mensagem = tk.Label(janela2, text="TODOS OS GRUPOS AVLS\nFORAM CADASTRADOS", font=("Arial", 18, "bold"), bg='green', fg='white')
mensagem.pack(expand=True)

