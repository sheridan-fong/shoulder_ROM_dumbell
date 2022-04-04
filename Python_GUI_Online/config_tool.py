from tkinter import *

root = Tk()
root.title('Codemy.com')
root.geometry("400x400")

def something():
    my_label.config(text = "this is the new text!!")

global my_label
my_label = Label(root, text="this is my text", font=("Helvetica", 12))
my_label.pack(pady=10)

my_button = Button(root, text = "Click me", command=something)
my_button.pack(pady=10)