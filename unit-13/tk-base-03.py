#import tkinter
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createwidgets()

    def createwidgets(self):
        self.btnok = tk.Button()
        self.btnok["text"] = "Ok"
        #self.btnok["command"] = self.showInfo
        self.btnok.pack(side="bottom")
        self.btnok.bind('<ButtonPress>', self.showInfo())
    def showInfo(self):
        print("you press button oK")


root = tk.Tk()
app = Application(root)
app.master.title("demo about tkinter")
app.master.size()
app.mainloop()