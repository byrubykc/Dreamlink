# Dreamlink mobile app
import tkinter as tk
# creation and modification of the main window (or first, idk)
root = tk.Tk()
root.title('Dreamlink')
root.geometry('393x873')#resolution size of my phone

# im learning tkinter wait
frm = tk.Frame(root, border=1, width=100, height=180, colormap='new')
frm.grid()
tk.Label(frm, text='Hello WOrld').grid(column=0, row=0)
tk.Button(frm, text="X", cursor='hand2', command=frm.grid_remove).grid(column=10, row=100)
frm.grid_propagate(0)
# functions

# classes

# main class

root.mainloop()