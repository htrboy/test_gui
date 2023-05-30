from tkinter import *
from tkinter import ttk


window = Tk()

window_width = int(window.winfo_screenwidth()/3)
window_height = int(window.winfo_screenheight()/4)

# get screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

window.title('My GUI')

window.mainloop()