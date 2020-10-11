import tkinter as tk
def showInfo(event):
    print(event.type, event.x, event.y)

window = tk.Tk()
window.title("Control:Button")
window.geometry("600x480+100+100")
btnok = tk.Button(window, text = "Entry")
btnok.bind("<Enter>",showInfo)
btnok.bind("<Leave>",showInfo)
btnok.bind("<Button-1>",showInfo)
btnok.pack(side = "top", expand = 1)
window.mainloop()



