import tkinter as tk
window = tk.Tk()
window.state('zoomed')

# ---- functions -----
def show_frame(frame):
    frame.tkraise()

# make sures that the window will expand
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# --- creating/initializing all of our frames ---
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky='nsew')

# setting the first frame that you see ---
show_frame(frame1)

# ------------- frame one code --------
frame1_title = tk.Label(frame1, text="this is frame one", bg ='red')
frame1_title.pack(fill = 'x')

frame1_btn = tk.Button(frame1, text="Enter", command=lambda:show_frame(frame2))
frame1_btn.pack()

# -------------- frame two code ---------
frame2_title = tk.Label(frame2, text="this is frame two", bg ='yellow')
frame2_title.pack(fill = 'x')

frame2_btn = tk.Button(frame2, text="Enter", command=lambda:show_frame(frame3))
frame2_btn.pack()

# ------------- frame three code ------
frame3_title = tk.Label(frame3, text="this is frame three", bg ='green')
frame3_title.pack(fill = 'x')

frame3_btn = tk.Button(frame3, text="Enter", command=lambda:show_frame(frame1))
frame3_btn.pack()


window.mainloop()