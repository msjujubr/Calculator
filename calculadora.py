import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Rudoilfo")

        self.resultado = tk.Entry(master, width=16, font=('Arial', 24), borderwidth=2, relief='ridge')
        self.resultado.grid(row=0, column=0, columnspan=4)

        self.criar_botoes()

        # Listener para teclado
        master.bind("<Key>", self.on_key_press)

    def criar_botoes(self):
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in botoes:
            botao = tk.Button(self.master, text=text, width=5, height=2,
                              command=lambda t=text: self.on_button_click(t))
            botao.grid(row=row, column=col)

    # callback para botões e teclado
    def on_button_click(self, char):
        if char == '=':
            try:
                resultado = eval(self.resultado.get())
                self.resultado.delete(0, tk.END)
                self.resultado.insert(0, str(resultado))
            except Exception:
                messagebox.showerror("Erro", "Operação inválida")
                self.resultado.delete(0, tk.END)
        else:
            self.resultado.insert(tk.END, char)

    # listener para teclado
    def on_key_press(self, event):
        char = event.char

        # Se pressionar Enter
        if event.keysym == "Return":
            self.on_button_click("=")
            return

        # Se pressionar '='
        if char == "=":
            self.on_button_click("=")
            return

        # Se for número, operador ou ponto
        if char in "0123456789+-*/.":
            self.on_button_click(char)

if __name__ == "__main__":
    interface = tk.Tk()
    calculadora = Calculadora(interface)
    interface.mainloop()
