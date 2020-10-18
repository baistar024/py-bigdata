# -*- encoding utf-8 -*-
from tkinter import *
# step 定义主窗口
root = Tk()
root.title("Notebook demo")
root.geometry('640x480+100+100')

menubar = Menu(root)
root.config(menu= menubar)
filemenu = Menu(menubar)
filemenu.add_cascade(label= '新建', accelerator= "Ctrl+N")
filemenu.add_cascade(label= '打开', accelerator= "Ctrl+O")
filemenu.add_cascade(label= '保存', accelerator= "Ctrl+S")
filemenu.add_cascade(label= '新建', accelerator= "Ctrl+Shift+N")
menubar.add_cascade(label = "文件", menu = filemenu)

editemenu = Menu(menubar)
editemenu.add_cascade(label= '复制', accelerator= "Ctrl+N")
editemenu.add_cascade(label= '剪切', accelerator= "Ctrl+O")
editemenu.add_cascade(label= '粘贴', accelerator= "Ctrl+S")
editemenu.add_cascade(label= '编辑', accelerator= "Ctrl+Shift + N")
menubar.add_cascade(label = "编辑", menu = editemenu)


root.mainloop()

