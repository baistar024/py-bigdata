import tkinter as tk

class AllControls(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

    def createControl(self):
        frame1 = tk.Frame(self.master, width = 120, height = 20, bg = "red")
        lbl1 = tk.Label(frame1,text = "haha").pack()
        frame1.pack()
        frame2 = tk.Frame(self.master)
        frame1.pack()
        frame3 = tk.Frame(self.master)
        frame1.pack()
        frame4 = tk.Frame(self.master)
        frame1.pack()
        frame5 = tk.Frame(self.master)
        frame1.pack()

root = tk.Tk()
app = AllControls(root)
app.mainloop()
