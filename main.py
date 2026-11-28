import tkinter as tk
from tkinter import ttk
from storage_data import StorageData
from tkinter import messagebox
from assignments import CourseAssignment

class Main:
    def __init__(self, window):
        self.window = window
        self.window.title("Deadline Tracker")
        self.window.geometry("1280x800")

        #tools frame
        tools = tk.Frame(window)
        tools.pack(side = "top", fill = "x")

        # tools buttons
        add = tk.Button(tools, text="Add", command = self.add)
        add.grid(padx=3, pady=3)
        edit = tk.Button(tools, text="Edit", command = self.edit)
        edit.grid(padx=3, pady=3, row=0, column=1)
        delete = tk.Button(tools, text="Delete", command = self.delete)
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

        #left and right side of the bottom frame
        self.show_done = tk.BooleanVar()
        bottom_frame = tk.Frame(self.window)
        bottom_frame.pack(side = "bottom", fill = "x")
        show = tk.Checkbutton(bottom_frame, text = "Show All", variable = self.show_done, command = self.refresh)
        show.pack(side = "right", padx = 3, pady = 3)
        self.status_label = tk.Label(bottom_frame, text = "")
        self.status_label.pack(side = "left", padx = 3, pady = 3)
        self.refresh()

    def refresh(self):
        self.assignments.sort(key = lambda a: a.due)
        for row in self.tree.get_children():
            self.tree.delete(row)
        count = 0
        for i, a in enumerate(self.assignments):
            if a.status == "Done" and self.show_done.get() == False:
                continue
            self.tree.insert("", "end",iid=str(i), text=a.course, values=(a.title, a.due, a.weight, a.status))
            count = count + 1
        self.status_label.config(text = "Showing " +str(count) + " of " + str(len(self.assignments)) + " Assignments")

    def get_selected(self):
        picked = self.tree.selection()
        if len(picked) == 0:
            messagebox.showinfo("No assignment clicked", "Click an assignment first.")
            return None
        return int(picked[0])
    def add(self):
        self.open_form(None, None)
    def edit(self):
        i = self.get_selected()
        if i != None:
            self.open_form(self.assignments[i], i)
    def delete(self):
        i = self.get_selected()
        if i == None:
            return
        a = self.assignments[i]
        answer = messagebox.askyesno("Delete assignment", "Delete " + a.course + " " + a.title + "?\nThis cannot be undone.")
        if answer:
            del self.assignments[i]
            self.storage.save(self.assignments)
            self.refresh()

    def open_form(self, a, index):
        # TODO: Joo Huen's part should be inserted
        if a == None:
            test = CourseAssignment("TST101", "Test assignment", "2026-12-12", 5, "Not Started")
            self.form_saved(test, None)
        else:
            a.status = "Done"
            self.form_saved(a, index)

    def form_saved(self, a, index):
        if index == None:
            self.assignments.append(a)
        else:
            self.assignments[index] = a
        self.storage.save(self.assignments)
        self.refresh()






if __name__ == "__main__":
    window = tk.Tk()
    app = Main(window)
    window.mainloop()