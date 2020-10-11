import tkinter as tk
def showInfo(event):
    print(event.char)
    print(val1)
val1 = tk.StringVar

win = tk.Tk()
win.title("Control:Entry Or Text")
win.geometry("160x100+100+100")
txte1 = tk.Entry(win, show = "*", textvariable = val1)
txte2 = tk.Entry(win, show = None)
txte2.bind("<Key>", showInfo)
# print(type(txte1))
txte1.pack()
txte2.pack()

win.mainloop()
