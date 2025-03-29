import tkinter as tk
from tkinter import font

def fazer_login():
    print("Login bem-sucedido!")  # Aqui seria chamada a função de login

# Configuração da janela principal
janela = tk.Tk()
janela.title("Gerenciamento de Biblioteca")
janela.geometry("400x300")
janela.configure(bg="#f0f0f5")

# Configuração de fontes personalizadas
titulo_fonte = font.Font(family="Helvetica", size=18, weight="bold")
label_fonte = font.Font(family="Helvetica", size=12)
botao_fonte = font.Font(family="Helvetica", size=12, weight="bold")

# Título
titulo_label = tk.Label(janela, text="Login na Biblioteca", font=titulo_fonte, bg="#f0f0f5", fg="#333333")
titulo_label.pack(pady=20)

# Campo de Usuário
usuario_label = tk.Label(janela, text="Usuário:", font=label_fonte, bg="#f0f0f5")
usuario_label.pack(anchor="w", padx=50)
usuario_entry = tk.Entry(janela, font=label_fonte, width=25, bd=2, relief="solid")
usuario_entry.pack(pady=5)

# Campo de Senha
senha_label = tk.Label(janela, text="Senha:", font=label_fonte, bg="#f0f0f5")
senha_label.pack(anchor="w", padx=50)
senha_entry = tk.Entry(janela, font=label_fonte, show="*", width=25, bd=2, relief="solid")
senha_entry.pack(pady=5)

# Botão de Login
login_botao = tk.Button(
    janela, 
    text="Entrar", 
    font=botao_fonte, 
    command=fazer_login, 
    bg="#4CAF50", 
    fg="white", 
    activebackground="#45a049", 
    bd=0, 
    padx=10, 
    pady=5
)
login_botao.pack(pady=20)

# Efeito de foco nos campos de entrada
def on_focus_in(event):
    event.widget.config(bg="#e6f7ff")

def on_focus_out(event):
    event.widget.config(bg="white")

usuario_entry.bind("<FocusIn>", on_focus_in)
usuario_entry.bind("<FocusOut>", on_focus_out)
senha_entry.bind("<FocusIn>", on_focus_in)
senha_entry.bind("<FocusOut>", on_focus_out)

janela.mainloop()
