import tkinter.filedialog as tkfd
import os
dia = tkfd.asksaveasfile()
if dia:
    print(dia.name)
    print(os.path.basename(dia.name))
diaopen =tkfd.askopenfile()
if diaopen:
    