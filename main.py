import tkinter as tk
from tkinter import ttk
from storage_data import StorageData

class Main:
    def __init__(self, window):
        self.window = window
        self.window.title("Deadline Tracker")
        self.window.geometry("1280x800")

        #tools frame
        tools = tk.Frame(window)
        tools.pack(side = "top", fill = "x")

        # tools buttons
        add = tk.Button(tools, text="Add")
        add.grid(padx=3, pady=3)
        edit = tk.Button(tools, text="Edit")
        edit.grid(padx=3, pady=3, row=0, column=1)
        delete = tk.Button(tools, text="Delete")
        delete.grid(padx=3, pady=3, row=0, column=2)

        self.storage = StorageData()
        self.assignments = self.storage.load()

        #list frame
        list_frame = tk.Frame(self.window)
        list_frame.pack(fill = "both", expand = True, padx = 3, pady = 3)
        self.tree = ttk.Treeview(list_frame, columns = ["title", "due", "weight", "status"], selectmode = "browse")
        self.tree.heading("#0", text = "Course Title")
        self.tree.heading("title", text = "Title")
        self.tree.heading("due", text = "Due date")
        self.tree.heading("weight", text = "Weight %")
        self.tree.heading("status", text = "Status")
        self.tree.column("#0", width=120)
        self.tree.column("title", width = 500)
        self.tree.column("due", width = 180)
        self.tree.column("weight", width = 120, anchor = "center")
        self.tree.column("status", width = 180)
        self.tree.grid(row = 0, column = 0, sticky = "nsew")

        scrollbar = ttk.Scrollbar(list_frame, orient = tk.VERTICAL, command = self.tree.yview)
        self.tree.configure(yscrollcommand = scrollbar.set)
        scrollbar.grid(row = 0, column = 1, sticky = "nsw")
        list_frame. rowconfigure(0, weight = 1)
        list_frame. columnconfigure(0, weight = 1)
        self.refresh()

    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for i, a in enumerate(self.assignments):
            self.tree.insert("", "end",iid=str(i), text=a.course, values=(a.title, a.due, a.weight, a.status))




if __name__ == "__main__":
    window = tk.Tk()
    app = Main(window)
    window.mainloop()