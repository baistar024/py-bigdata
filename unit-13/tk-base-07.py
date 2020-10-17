import tkinter as tk


class Application():
    def __init__(self, master = None):

        frame = tk.Frame(master)
        self.master = master

        self.btnquit = tk.Button(frame,text ="Quit",fg="red", command= frame.quit)
        self.btnquit.pack(side = tk.LEFT)
        self.btnsayhi = tk.Button(frame, text = "Say Hi", command = self.sayhi, fg = "green")
        self.btnsayhi.pack(side = tk.LEFT)
        frame.pack(fill = tk.X, expand = 1)
    def sayhi(self):
        print("Hi, everybody")

root = tk.Tk()
app = Application(root)
root.mainloop()