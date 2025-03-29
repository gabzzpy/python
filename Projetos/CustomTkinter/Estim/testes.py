from tkinter import Tk
from tkinterhtml import HtmlFrame

# Criação da janela principal
janela = Tk()
janela.title("Teste tkinterhtml")
janela.geometry("800x600")

# Criar o frame HTML
html_frame = HtmlFrame(janela)
html_frame.pack(fill="both", expand=True)

# Adicionar conteúdo HTML
html_frame.set_content("<h1>Olá, tkinterhtml está funcionando!</h1><p>Teste de exibição HTML.</p>")

# Executar a aplicação
janela.mainloop()
