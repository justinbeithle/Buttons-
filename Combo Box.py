#import class library
import tkinter as tk
from tkinter import ttk # <--- used to style tkinter widgets  

#created an item object that is inserted into the function 
def on_select(event): 

    selected_item = event.widget.get()
    print("Selected Item", selected_item)

#
root = tk.Tk()
root.title("Combobox Example")

