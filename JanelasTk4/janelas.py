import tkinter as tk
from tkinter import ttk

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