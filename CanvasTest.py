import tkinter
import random
root = tkinter.Tk()
root.title('캔버스 만들기')

#좌표 출력기
def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse['text']=str(x)+','+str(y)
    
def click_btn():
    label['text'] = random.choice(['대길','중길','소길','흉'])
    text.insert(tkinter.END,label['text']+"\n")

#캔버스 생성
canvas = tkinter.Canvas(root, width=800, height=600, bg='skyblue')
canvas.pack()

#캔버스 내 이미지 생성
bgimg = tkinter.PhotoImage(file='miko.png')
canvas.create_image(400,300,image=bgimg)

canvas.create_rectangle(351,394,600,490,fill='darkgray',outline='red',width='5')



#좌표 출력기
root.bind('<Motion>',mouseMove)
labelMouse = tkinter.Label(root,text=',', font=('맑은고딕', 10))
labelMouse.pack()


label = tkinter.Label(root,text='??', font=('맑은 고딕', 120))
label.place(x=380, y=60)


btn = tkinter.Button(root, text='제비뽑기', font=('맑은고딕', 36), fg='skyblue', command=click_btn)
btn.place(x=360, y=400)

#텍스트창 생성
text = tkinter.Text()
text.place(x=0,y=600,width=800,height=200)


root.mainloop()
