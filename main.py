import tkinter as tk

class Main:
    def __init__(self, window):
        self.window = window
        self.window.title("Deadline Tracker")
        self.window.geometry("1280x800"  )

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

if __name__ == "__main__":
    window = tk.Tk()
    app = Main(window)
    window.mainloop()