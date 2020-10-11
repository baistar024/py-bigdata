import tkinter as tk



class NoteBook():
    def __init__(self, window):
        super().__init__()
        self.master = window
        self.master.title("demo about plus")
        self.createwidgets()


    def createwidgets(self):
        self.lblplus1 = tk.Label(self.master, text = "加数1")
        self.lblplus1.grid(row =0, column = 1)
        self.lblplus2 = tk.Label(self.master, text = "加数2")
        self.lblplus2.grid(row =0, column = 3)
        self.lframe = tk.LabelFrame(self.master, text = "Area 1",width = 600,height = 100,  bg = "red")
        self.lframe.grid(row = 1, column = 1, )
win = tk.Tk()
app = NoteBook(win)
win.mainloop()



