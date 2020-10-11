import tkinter as tk
win = tk.Tk()
win.title("Control:Entry Or Text")
win.geometry("800x600+100+100")
txte1 = tk.Entry(win, show = "*")
txte2 = tk.Entry(win, show = None)
txte1.pack()
txte2.pack()

win.mainloop()
