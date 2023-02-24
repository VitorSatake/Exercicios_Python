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
        ).pack(fill="x", padx=5, pady=50)

        # Campo para enviar dados

        self.txtVarDados = tk.StringVar()
        txtDados = ttk.Entry(
            self,
            textvariable=self.txtVarDados,
            font=("Arial", 10)
        )
        txtDados.pack(fill="x", side="left", expand=True, padx=5)


        # Button de Abrir nova janela

        ttk.Button(
            self,
            text="Abrir Nova Janela",
            command=self.abrirJanela
        ).pack(fill="x", side="left", expand=True, padx=5, ipady=5)

    # Funçaõ para criar nova janela

    def abrirJanela(self):
        novaJanela = NovaJanela()
        novaJanela.txtLable.set(self.txtVarDados.get())

class NovaJanela(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.title("Nova Janela")

        self.txtLable = tk.StringVar()

        self.lblTitulo = ttk.Label(
            self,
            font=("Arial", 28, "bold"),
            textvariable=self.txtLable
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