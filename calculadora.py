import tkinter as tk
from tkinter import messagebox

class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.entry = tk.Entry(root, width=20, font=('Arial', 16), bd=5, insertwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=6)

        # Adiciona botões numéricos e operadores
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'CE'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16), bd=8, command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Adiciona o botão "Sair"
        tk.Button(root, text="Sair", padx=20, pady=20, font=('Arial', 16), bd=8, command=root.destroy).grid(row=5, column=0, columnspan=6)

        # Configuração para lidar com a entrada do teclado
        self.root.bind('<Key>', self.key_press)

    def button_click(self, value):
        if value == "=":
            self.calculate_result()
        elif value == "CE":
            self.clear_entry()
        else:
            self.entry.insert(tk.END, value)

    def key_press(self, event):
        key = event.char

        if key in '0123456789':
            self.entry.insert(tk.END, key)
        elif key == '+':
            self.entry.insert(tk.END, '+')
        elif key == '-':
            self.entry.insert(tk.END, '-')
        elif key == '*':
            self.entry.insert(tk.END, '*')
        elif key == '/':
            self.entry.insert(tk.END, '/')
        elif key == '.':
            self.entry.insert(tk.END, '.')
        elif key == '\r':
            self.calculate_result()
        elif key == '\x08':  # Código para a tecla Backspace
            self.backspace()

    def calculate_result(self):
        current_expression = self.entry.get()
        try:
            result = eval(current_expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except:
            messagebox.showerror("Erro", "Expressão inválida")

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def backspace(self):
        current_text = self.entry.get()
        new_text = current_text[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, new_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()
