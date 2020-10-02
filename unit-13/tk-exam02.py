from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text ="Hello class", bg = "red", command=frame.quit())
        self.button.pack()
        self.hiButton = Button(frame, text = 'Say hi', command= self.sayhi)
        self.hiButton.pack()
    def sayhi(self):
        print("hi, sundy, Tanks")

root = Tk()
app = App(root)
root.mainloop()