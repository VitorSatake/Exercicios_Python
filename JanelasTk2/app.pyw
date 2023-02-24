import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")

        # Label

        ttk.Label(
            self,
            text="Tela Inicial",
            font=("Arial", 28, "bold")
        ).pack(expand=True)

        # Button de Abrir nova janela

        ttk.Button(
            self,
            text="Abrir Nova Janela",
            command=self.abrirJanela
        ).pack(expand=True)

    # Funçaõ para criar nova janela

    def abrirJanela(self):
        NovaJanela()

class NovaJanela(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.title("Nova Janela")

        self.lblTitulo = ttk.Label(
            self,
            font=("Arial", 28, "bold"),
            text="Segunda Janela"
        )
        self.lblTitulo.pack(expand=True)

        ttk.Button(
            self,
            text="Fechar",
            command=self.destroy
        ).pack(expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()