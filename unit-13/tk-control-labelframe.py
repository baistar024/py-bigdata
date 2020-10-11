from tkinter import *
root = Tk()
def showeveinfo(event):
    print(event.type, event.x, event.y)
for lf in ['red','blue','yellow']:
    #可以使用text属性指定Frame的title
    lblf = LabelFrame(root)
    Label(lblf, text = lf).pack()
    Button(lblf, text = lf,bg = lf).pack()
    lblf.config(bg = lf)
    lblf.bind("<Enter>", showeveinfo)
    lblf.bind("<Leave>", showeveinfo)
    lblf.bind("<Motion>", showeveinfo)
    lblf.pack(fill = 'x')

root.mainloop()