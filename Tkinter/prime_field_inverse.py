import tkinter as tk
import math

window = tk.Tk()
window.title("Prime Field Inverse Calculator")
window.geometry("400x225")
window.configure(background="white")

def is_primefield(order):
    for i in range(2, order):
        if order % i == 0:
            return False
    return True

def inverse(element, field_order):
    for i in range(2, field_order):
        if (i * element) % field_order == 1:
            return i
    return 0

def calculate_inverse():
    element = int(element_entry.get())
    field_order = int(field_entry.get())
    if is_primefield(field_order) == False:
        result_text = "It's not a prime field!"
    else:
        inv = inverse(element, field_order)
        result_text = "Inverse of {element} in GF({order}) is {inv}".format(element=element, order = field_order, inv = inv)
    result_label.configure(text=result_text)

header_label = tk.Label(window, text="A Simple Calculator for Finding Inverse in Prime Field")
header_label.pack()

element_frame = tk.Frame(window)
element_frame.pack(side=tk.TOP)
element_label = tk.Label(element_frame, text="element")
element_label.pack(side=tk.LEFT)
element_entry = tk.Entry(element_frame)
element_entry.pack(side=tk.LEFT)

field_frame = tk.Frame(window)
field_frame.pack(side=tk.TOP)
field_label = tk.Label(field_frame, text="field order")
field_label.pack(side=tk.LEFT)
field_entry = tk.Entry(field_frame)
field_entry.pack(side=tk.LEFT)

calculate_btn = tk.Button(window, text="Go", command=calculate_inverse)
calculate_btn.pack()

result_label = tk.Label(window, text = '')
result_label.pack()

window.mainloop()