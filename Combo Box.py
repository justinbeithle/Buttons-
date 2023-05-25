#import class library
import tkinter as tk
from tkinter import ttk # <--- used to style tkinter widgets  

#created an item object that is inserted into the function 
def on_select(event): 

    selected_item = event.widget.get()
    print("Selected Item", selected_item)

#Creates the window box 
root = tk.Tk()
root.title("Combobox Example")

#Create an array of items(statics)
items = ["Item 1", "Item 2", "Item 3", "Item 4","Item 5"]

#Tie values in items array to combo box 
combo_box = ttk.Combobox(root, values=items) 

#Bind selected event to the function
combo_box.bind("<<ComboboxSelected>>", on_select)

combo_box.pack() 

#Has it so the window remains open(loop)
root.mainloop()
 