import tkinter as tk

#cria janela2
janela = tk.Tk()
janela.title("CADASTRO AVL")
janela.geometry("400x500") #tamanho da tela

#janela por cima
janela.attributes("-topmost", True)

#cor fundo verde
janela.configure(bg='green')

#Cria um label com a msg estilizada
mensagem = tk.Label(janela, text="TODOS OS GRUPOS AVLS\nFORAM CADASTRADOS", font=("Arial", 18, "bold"), bg='green', fg='white')
mensagem.pack(expand=True)

janela.mainloop()   