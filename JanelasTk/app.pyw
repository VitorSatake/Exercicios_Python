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
        janela2 = tk.Toplevel()
        janela2.geometry("400x200")
        janela2.title("Nova Janela")
        janela2Label = ttk.Label(janela2, text="Segunda Janela")
        janela2Label.grid(row=0, column=0)
        janela2Button = ttk.Button(
            janela2,
            text="Fechar",
            command=janela2.destroy
        )
        janela2Button.grid(row=1, column=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()