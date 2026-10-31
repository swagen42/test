import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("хуй")
        self.root.resizable(False, False)
        
        # Переменная для хранения выражения
        self.expression = ""
        self.input_text = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Поле ввода
        input_frame = tk.Frame(self.root, width=312, height=50, bd=0,
                          highlightbackground="black", highlightcolor="black",
                          highlightthickness=1)
        input_frame.pack(side=tk.TOP)
        
        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'),
                            textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)
        
        # Кнопки
        buttons_frame = tk.Frame(self.root, width=312, height=272, bg="grey")
        buttons_frame.pack()
        
        # Расположение кнопок
        buttons = [
            'C', '(', ')', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', ''
        ]
        
        row = 0
        col = 0
        for button in buttons:
            if button == '=':
                btn = tk.Button(buttons_frame, text=button, fg="black", width=10, height=3,
                              bd=0, bg="#eee", cursor="hand2",
                              command=self.btn_equal_clicked)
                btn.grid(row=row, column=col, columnspan=2, padx=1, pady=1)
                col += 2
            elif button == '':
                col += 1
            else:
                btn = tk.Button(buttons_frame, text=button, fg="black", width=10, height=3,
                      bd=0, bg="#fff", cursor="hand2")
                if button == 'C':
                    btn.config(command=self.btn_clear_clicked)
                else:
                    btn.config(command=lambda x=button: self.btn_click(x))
                btn.grid(row=row, column=col, padx=1, pady=1)
                col += 1
                if col > 3:
                    col = 0
                    row += 1
    
    def btn_click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)
    
    def btn_clear_clicked(self):
        self.expression = ""
        self.input_text.set("")
    
    def btn_equal_clicked(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
##            messagebox.showerror("вы 100%", "капитальный красавчик")
##            
            messagebox.showerror("вы 100%", "ЕБАНАТ")
            self.expression = ""
            self.input_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
