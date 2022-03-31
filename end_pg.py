from tkinter import *
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")  # the backend of matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
import global_var
from PIL import ImageTk, Image

ws = Tk()
ws.geometry('600x600')
ws.title('PythonGuides')
ws['bg'] = '#ffbf00'

f = ("Times bold", 14)


def nextPage():
    ws.destroy()
    import exercise_one_pg


def homePage():
    ws.destroy()
    import home_pg

def homePage():
    ws.destroy()
    import home_pg

Label(
    ws,
    text=global_var.rom_value_text,
    font=f,
    padx=20,
    pady=30,
    bg='#ffbf00'
).place(x=150, y=40)

Label(
    ws,
    text=global_var.rom_phrase,
    font=f,
    padx=20,
    pady=50,
    bg='#ffbf00'
).place(x=50, y = 400)

Button(
    ws,
    text="Restart",
    font=f,
    command=global_var.exercise_one
).pack(fill=X, expand=TRUE,anchor = 's', side=LEFT)


Button(
    ws,
    text="Home Page",
    font=f,
    command=homePage
).pack(fill=X, expand=TRUE,anchor = 's', side=LEFT)

img = Image.open("euler.png")
img = img.resize((300,300), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
label1 = Label(image=img)
label1.image = img
label1.place(x=150,y=100)
#
# Label(ws, image = img).place(x=50,y = 100)

#-------- trying to graph live ----------
# f = Figure(figsize=(5, 5), dpi=100)
# a = f.add_subplot(111)  # means there is only one chart
# a.plot(global_var.x_data, global_var.y_data)
#
# canvas = FigureCanvasTkAgg(f)
# canvas.draw()
# canvas.get_tk_widget().place(x = 50, y = 100, width = 200, height = 300)

ws.mainloop()