import tkinter

root = tkinter.Tk()




file = open("test.txt","r",encoding="UTF-8")

strFile = file.readline()
root.geometry(strFile[:-1])

strFile = file.readline()
root.title(strFile[:-1])




file.close()

root.mainloop()


'''
while True:
    str = file.readline()
    print(str,end='')
    if(str==""):
        break
'''


'''
filelist = file.readlines()
index = 1
for strList in filelist :
    print(str(index)+':'+strList,end='')
    index = index + 1
'''