#Import class library 
import tkinter as tk 

#Defining fuinction for when button is clicked
def button_click():
    print("button clicked")

#Root forms the background of the screen(Root Window)git 
root = tk.Tk()
root.title("button example")

#created button object and set three argument (Object Orientated Programming!)
button = tk.Button(root, text="You Wont", command = button_click)
button.pack()

root.mainloop()
