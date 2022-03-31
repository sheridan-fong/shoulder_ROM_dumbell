from tkinter import *

ws = Tk()
ws.geometry('600x600')
ws.title('PythonGuides')
ws['bg'] = '#5d8a82'

f = ("Times bold", 14)


def nextPage():
    ws.destroy()
    import exercise_one_pg


def prevPage():
    ws.destroy()
    import exercise_two_pg


Label(
    ws,
    text="ROMbell Home",
    padx=20,
    pady=20,
    bg='#5d8a82',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    ws,
    text="Exercise 1: Reverse Fly",
    font=f,
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Exercise 2: Side-Lying Rotation",
    font=f,
    command=prevPage
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()