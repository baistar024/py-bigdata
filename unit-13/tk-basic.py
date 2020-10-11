import tkinter as tk
#tkinter程序基本框架
#定义一个应用框架
class Application(tk.Frame):
    #初始化
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    # 窗体控制
    def create_widgets(self):
        #初始化控件
        self.hi_there = tk.Button(self)
        #控件设置
        self.hi_there["text"] = "Hello World\n(click me)"
        #绑定事件与处理函数
        self.hi_there["command"] = self.say_hi
        #显示部件
        self.hi_there.pack(side="top")
        #初始化部件
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        #显示部件
        self.quit.pack(side="bottom")
    #处理函数
    def say_hi(self):
        print("hi there, everyone!")

#创建窗体
root = tk.Tk()
#用本窗体来安放frame
app = Application(master=root)
#显示窗体
app.mainloop()