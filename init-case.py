import os
units = int(input("please input how many units:"))
if units >= 0:

    for i in range(1, units+1):
        path = "./unit-"
        if i<10 :
           path += ("0" + str(i))
        else:
            path += str(i)
        if not os.path.exists(path):
            os.mkdir(path)

