import tkinter as tk

window = tk.Tk()

window.title("Deadline Tracker")
window.geometry("1280x800")

#tools frame
tools = tk.Frame(window)
tools.pack(side = "top", fill = "x")

#tools buttons
add = tk.Button(tools, text = "Add")
add.grid(padx = 3, pady = 3)
edit = tk.Button(tools, text = "Edit")
edit.grid(padx = 3, pady = 3, row = 0, column=1)
delete = tk.Button(tools, text = "Delete")
delete.grid(padx = 3, pady = 3, row = 0, column=2)


window.mainloop()