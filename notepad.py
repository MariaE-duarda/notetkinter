import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class BlocoDeNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloco de Notas")
        self.root.geometry("400x400")
        self.light_mode = tk.BooleanVar(value=True)
        self.light_mode.trace("w", self.alterar_tema)
        self.area_de_texto = tk.Text(self.root, font="Arial 12", wrap="word")
        self.area_de_texto.pack(fill="both", expand=True)
        self.criar_menu()

    def criar_menu(self):
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.menu_arquivo = tk.Menu(self.menu)
        self.menu.add_cascade(label="Arquivo", menu=self.menu_arquivo)
        self.menu_arquivo.add_command(label="Abrir", command=self.abrir_arquivo)
        self.menu_arquivo.add_command(label="Salvar", command=self.salvar_arquivo)
        self.menu_arquivo.add_separator()
        self.menu_arquivo.add_command(label="Sair", command=self.sair)
        self.menu_tema = tk.Menu(self.menu)
        self.menu.add_cascade(label="Tema", menu=self.menu_tema)
        self.menu_tema.add_radiobutton(label="Modo claro", variable=self.light_mode, value=True)
        self.menu_tema.add_radiobutton(label="Modo escuro", variable=self.light_mode, value=False)

    def abrir_arquivo(self):
        arquivo = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Todos os arquivos", "*.*"), ("Documentos de texto", "*.txt")])
        if arquivo:
            self.area_de_texto.delete(1.0, "end")
            for linha in arquivo:
                self.area_de_texto.insert("end", linha)
            arquivo.close()

    def salvar_arquivo(self):
        arquivo = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Todos os arquivos", "*.*"), ("Documentos de texto", "*.txt")])
        if arquivo:
            arquivo.write(self.area_de_texto.get(1.0, "end"))
            arquivo.close()

    def sair(self):
        if messagebox.askyesno("Sair", "Deseja realmente sair?"):
            self.root.destroy()

    def alterar_tema(self, *args):
        if self.light_mode.get():
            self.root.config(bg="white")
            self.area_de_texto.config(bg="white", fg="black")
        else:
            self.root.config(bg="gray19")
            self.area_de_texto.config(bg="gray19", fg="white")

root = tk.Tk()
bloco_de_notas = BlocoDeNotas(root)
root.mainloop()
