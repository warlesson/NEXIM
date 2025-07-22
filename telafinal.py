import tkinter as tk

#cria janela
janela = tk.Tk()
janela.title("Cadastro Finalizado")
janela.geometry("400x200") #tamanho da tela

#janela por cima
janela.attributes("-topmost", True)

#cor fundo verde
janela.configure(bg='green')

#Cria um label com a msg estilizada
mensagem = tk.Label(janela, text="TODOS OS PART NUMBER\nFORAM CADASTRADOS", font=("Arial", 18, "bold"), bg='green', fg='white')
mensagem.pack(expand=True)


