import tkinter as tk

root = tk.Tk()
root.title('Calculator')
root.geometry('400x500')
root.resizable(False, False)
root.config(bg = '#2e3440')

# Variables to track calculation
current_num = ''
operation = ''
first_num = None

# Entry / Display
entry_button = tk.Entry(root, font = ('Arial', 24), bd = 5, relief = 'sunken', justify = 'right', bg = '#e5e9f0', fg = 'black')
entry_button.grid(row = 0, column = 0, columnspan = 4, padx = 15, pady = 10, ipadx = 5, ipady = 15, sticky = 'nsew')

# Helper Functions
def number(num): # We will accept one digit and then concatenate it with next digit to form a number.
    current = entry_button.get()
    entry_button.delete(0, tk.END)
    entry_button.insert(0, current + str(num))

def operations(op):
    global first_num, operation, current_num # Keep track of the calculator's state across different button clicks.
    current_num = entry_button.get()
    if current_num:
        first_num = float(current_num) # Converting string to number
        operation = op
        entry_button.delete(0, tk.END)

def calculation():
    global first_num, operation, current_num
    try:
        second_num = float(entry_button.get())
        if operation == '+':
            ans = first_num + second_num
        elif operation == '-':
            ans = first_num - second_num
        elif operation == 'x':
            ans = first_num * second_num
        elif operation == '/':
            if second_num == 0:
                entry_button.delete(0, tk.END)
                entry_button.insert(0, 'Error!')
            else:
                ans = first_num / second_num
        else:
            return
        entry_button.delete(0, tk.END)
        entry_button.insert(0, str(ans))
        first_num = ans
    except:
        entry_button.delete(0, tk.END)
        entry_button.insert(0, 'Error!')

# 1st Row
def percent():
    try:
        n1 = float(entry_button.get())
        ans = n1 / 100
        entry_button.delete(0, tk.END)
        entry_button.insert(0, str(ans))
    except:
        entry_button.delete(0, tk.END)
        entry_button.insert(0, 'Error!')

percent_button = tk.Button(root, text = '%', font =('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = percent)
percent_button.grid(row = 1, column = 0, padx = 2, pady = 2, sticky = 'nsew')

def clear_entry():
    entry_button.delete(0, tk.END)

CE = tk.Button(root, text = 'CE', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = clear_entry)
CE.grid(row = 1, column = 1, padx = 2, pady = 2, sticky = 'nsew')

def clear():
    global first_num, operation, current_num
    entry_button.delete(0, tk.END)
    first_num = None
    operation = ''
    current_num = ''

C = tk.Button(root, text = 'C', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = clear)
C.grid(row = 1, column = 2, padx = 2, pady = 2, sticky = 'nsew')

def backspace():
    n1 = entry_button.get()
    entry_button.delete(0, tk.END)
    entry_button.insert(0, n1[:-1])

back = tk.Button(root, text = "←", font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = backspace)
back.grid(row = 1, column = 3, padx = 2, pady = 2, sticky = 'nsew')

# 2nd Row
def inv():
    try:
        n1 = float(entry_button.get())
        if n1 == 0:
            entry_button.delete(0, tk.END)
            entry_button.insert(0, 'Error!')
        else:
            ans = 1 / n1
            entry_button.delete(0, tk.END)
            entry_button.insert(0, str(n1))
    except:
        entry_button.delete(0, tk.END)
        entry_button.insert(0, 'Error!')

inverse = tk.Button(root, text = '1/x', font =('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = inv)
inverse.grid(row = 2, column = 0, padx = 2, pady = 2, sticky = 'nsew')

def sqr():
    try:
        n1 = float(entry_button.get())
        ans = n1**2
        entry_button.delete(0, tk.END)
        entry_button.insert(0, str(ans))
    except:
        entry_button.delete(0, tk.END)
        entry_button.insert(0, 'Error')

square = tk.Button(root, text = 'x²', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = sqr)
square.grid(row = 2, column = 1, padx = 2, pady = 2, sticky = 'nsew')

def sqr_root():
    try:
        n1 = float(entry_button.get())
        if n1 < 0:
            entry_button.delete(0, tk.END)
            entry_button.insert(0, 'Error')
        else:
            ans = n1 ** 0.5
            entry_button.delete(0, tk.END)
            entry_button.insert(0, str(ans))
    except:
        entry_button.delete(0, tk.END)
        entry_button.insert(0, 'Error')

sqrt = tk.Button(root, text = '√', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = sqr_root)
sqrt.grid(row = 2, column = 2, padx = 2, pady = 2, sticky = 'nsew')

division = tk.Button(root, text = '/', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = lambda: operations('/'))
division.grid(row = 2, column = 3, padx = 2, pady = 2, sticky = 'nsew')

# 3rd Row
no7 = tk.Button(root, text = '7', font =('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = lambda: number('7'))
no7.grid(row = 3, column = 0, padx = 2, pady = 2, sticky = 'nsew')

no8 = tk.Button(root, text = '8', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = lambda: number('8'))
no8.grid(row = 3, column = 1, padx = 2, pady = 2, sticky = 'nsew')

no9 = tk.Button(root, text = '9', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = lambda: number('9'))
no9.grid(row = 3, column = 2, padx = 2, pady = 2, sticky = 'nsew')

multiply = tk.Button(root, text = 'x', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = lambda: operations('x'))
multiply.grid(row = 3, column = 3, padx = 2, pady = 2, sticky = 'nsew')

# 4th Row
no4 = tk.Button(root, text = '4', font =('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = lambda: number('4'))
no4.grid(row = 4, column = 0, padx = 2, pady = 2, sticky = 'nsew')

no5 = tk.Button(root, text = '5', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = lambda: number('5'))
no5.grid(row = 4, column = 1, padx = 2, pady = 2, sticky = 'nsew')

no6 = tk.Button(root, text = '6', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = lambda: number('6'))
no6.grid(row = 4, column = 2, padx = 2, pady = 2, sticky = 'nsew')

minus = tk.Button(root, text = '-', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = lambda: operations('-'))
minus.grid(row = 4, column = 3, padx = 2, pady = 2, sticky = 'nsew')

# 5th Row
no1 = tk.Button(root, text = '1', font =('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = lambda: number('1'))
no1.grid(row = 5, column = 0, padx = 2, pady = 2, sticky = 'nsew')

no2 = tk.Button(root, text = '2', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = lambda: number('2'))
no2.grid(row = 5, column = 1, padx = 2, pady = 2, sticky = 'nsew')

no3 = tk.Button(root, text = '3', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = lambda: number('3'))
no3.grid(row = 5, column = 2, padx = 2, pady = 2, sticky = 'nsew')

plus = tk.Button(root, text = '+', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = lambda: operations('+'))
plus.grid(row = 5, column = 3, padx = 2, pady = 2, sticky = 'nsew')

# 6th Row
def toggle():
    try:
        n1 = float(entry_button.get())
        ans = -n1
        entry_button.delete(0, tk.END)
        entry_button.insert(0, str(ans))
    except:
        pass

plus_minus = tk.Button(root, text = '±', font =('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = toggle)
plus_minus.grid(row = 6, column = 0, padx = 2, pady = 2, sticky = 'nsew')

no0 = tk.Button(root, text = '0', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = lambda: number('0'))
no0.grid(row = 6, column = 1, padx = 2, pady = 2, sticky = 'nsew')

def full_stop():
    n1 = entry_button.get()
    if '.' not in n1:
        entry_button.insert(tk.END, '.')

dot = tk.Button(root, text = '.', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = full_stop)
dot.grid(row = 6, column = 2, padx = 2, pady = 2, sticky = 'nsew')

equal = tk.Button(root, text = '=', font = ('Arial', 16), width = 6, height = 2, bg = '#3b4252', command = calculation)
equal.grid(row = 6, column = 3, padx = 2, pady = 2, sticky = 'nsew')

# Grid Expansion
for i in range(7):
    root.rowconfigure(i, weight = 1)
for j in range(4):
    root.columnconfigure(j, weight = 1)
root.mainloop()
