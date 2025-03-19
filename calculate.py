import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        label_result.config(text=f"ผลลัพธ์: {result}")
    except Exception as e:
        label_result.config(text="ผิดพลาก")

window = tk.Tk()
window.title("เครื่องคิดเลข")

entry = tk.Entry(window, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons =[
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, column) in buttons:
    if text == '=':
        button = tk.Button(window, text=text, width=10, height=2, command=calculate)
    elif text =="C":
        button = tk.Button(window, text=text, width=10, height=2, command=lambda: entry.delete(0, tk.END))
    else:
        button = tk.Button(window, text=text, width=10, height=2, command=lambda t=text: entry.insert(tk.END, t))

    button.grid(row=row, column=column)

label_result = tk.Label(window, text="ผลลัพธ์: ", height=2)
label_result.grid(row=5, column=0, columnspan=4)

window.mainloop()