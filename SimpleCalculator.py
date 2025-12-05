import tkinter as tk #importing class

root = tk.Tk() #creating interface
root.title('My Calculator')
root.config(bg = '#2e3440')
root.geometry("500x500")
root_t = tk.Label(root, text = 'CALCULATOR', font = ('Times New Roman', 30, 'bold'), bg = '#2e3440', fg = '#88c0d0')
root_t.grid(row = 0, column = 0, pady = 15, padx = 150)

Number1 = tk.Label(root, text = 'Enter first number:', font = ('Arial', 17), bg = '#3b4252', fg = 'white') #asking for 1st number
Number1.grid(row = 1, column = 0)
n1 = tk.Entry(root, width = 15) #accepting first entry
n1.grid(row = 2, column = 0)
n1.config(bg = '#e5e9f0', fg = 'black')

Number2 = tk.Label(root, text = 'Enter second number:', font = ('Arial', 17), bg = '#3b4252', fg = 'white') #asking for 2nd number
Number2.grid(row = 4, column = 0)
n2 = tk.Entry(root, width = 15) #accepting second entry
n2.grid(row = 5, column = 0)
n2.config(bg = '#e5e9f0', fg = 'black')

result_text = tk.StringVar() #initialising result
result_label = tk.Label(root, textvariable = result_text, font = ('Arial', 17), bg = '#2e3440', fg = '#faeb07') #displaying result
result_label.grid(row = 7, column = 0)

def add(): #addition operation
    try:
        f = float(n1.get())
        s = float(n2.get())
        sum = f + s
        result_text.set(f'Result: {sum}')
    except ValueError:
        result_text.set('ERROR!')

add_button = tk.Button(root, text = 'Add', width = 10, command = add) #1st operation button
add_button.grid(row = 9, column = 0)
add_button.config(font = ('Arial', 15, 'bold'), bg = '#5e81ac', fg = 'black')

def subtract(): #subtraction operation
    try:
        f = float(n1.get())
        s = float(n2.get())
        difference = f - s
        result_text.set(f'Result: {difference}')
    except ValueError:
        result_text.set('ERROR!')

subtract_button = tk.Button(root, text = 'Subtract', width = 10, command = subtract) #2nd operation button
subtract_button.grid(row = 10, column = 0)
subtract_button.config(font = ('Arial', 15, 'bold'), bg = '#5e81ac', fg = 'black')

def division(): #division operation
    try:
        f = float(n1.get())
        s = float(n2.get())
        if s == 0:
            result_text.set('ERROR: Cannot divide by zero!')
        else:
            division = f / s
            result_text.set(f'Result: {division}')
    except ValueError:
        result_text.set('ERROR!')

division_button = tk.Button(root, text = 'Divide', width = 10, command = division) #3rd operation button
division_button.grid(row = 11, column = 0)
division_button.config(font = ('Arial', 15, 'bold'), bg = '#5e81ac', fg = 'black')

def multiply(): #multiplication operation
    try:
        f = float(n1.get())
        s = float(n2.get())
        multiply = f * s
        result_text.set(f'Result: {multiply}')
    except ValueError:
        result_text.set('ERROR!')

multiply_button = tk.Button(root, text = 'Multiply', width = 10, command = multiply) #4th operation button
multiply_button.grid(row = 12, column = 0)
multiply_button.config(font = ('Arial', 15, 'bold'), bg = '#5e81ac', fg = 'black')

def power():
    try:
        f = float(n1.get())
        s = float(n2.get())
        power = f ** s
        result_text.set(f'Result: {power}')
    except ValueError:
        result_text.set('ERROR!')

power_button = tk.Button(root, text = 'Exponential', width = 10, command = power)
power_button.grid(row = 13, column = 0)
power_button.config(font = ('Arial', 15, 'bold'), bg = '#5e81ac', fg = 'black')

def average():
    try:
        f = float(n1.get())
        s = float(n2.get())
        avg = (f + s) / 2
        result_text.set(f'Result: {avg}')
    except ValueError:
        result_text.set('ERROR!')

average_button = tk.Button(root, text = 'Average', width = 10, command = average)
average_button.grid(row = 14, column = 0)
average_button.config(font = ('Arial', 15, 'bold'), bg = '#5e81ac', fg = 'black')

def clear(): #clear operation
    n1.delete(0, tk.END)
    n2.delete(0, tk.END)
    result_text.set('Result: ')

clear_button = tk.Button(root, text = 'Clear', width = 10, command = clear) #clear operation button
clear_button.grid(row = 15, column = 0)
clear_button.config(font = ('Arial', 15, 'bold'), bg = '#FF6B6B', fg = 'black')

root.mainloop()