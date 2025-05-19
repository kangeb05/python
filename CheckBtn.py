import tkinter
import random
import tkinter.messagebox

root = tkinter.Tk()
root.title('고양이 지수 판정 게임')


#좌표 출력기
def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse['text']=str(x)+','+str(y)
    labelMouse.place(x=0,y=200)

result = [
    '전생에 고양이었을 가능성은 매우 낮습니다.',
    '보통 사람입니다.',
    '특별히 이상한 곳은 없습니다.',
    '꽤 고양이 다운 구석이 있습니다.',
    '고양이와 비슷한 성격 같습니다.',
    '고양이와 근접한 성격입니다.',
    '전생에 고양이었을지도 모릅니다.',
    '겉모습은 사람이지만, 속은 고양이일 가능성이 있습니다.'
]


#체크버튼 클릭시
def chkBtnClick():
    numCheck = 0
    if cvalue1.get() == True: numCheck += 1
    if cvalue2.get() == True: numCheck += 1
    if cvalue3.get() == True: numCheck += 1
    if cvalue4.get() == True: numCheck += 1
    if cvalue5.get() == True: numCheck += 1
    if cvalue6.get() == True: numCheck += 1
    if cvalue7.get() == True: numCheck += 1
    print(numCheck)
    textFiled.delete('1.0',tkinter.END)
    textFiled.insert('1.0','<진단결과>\n 당신의 고양이 지수는'+str(numCheck/7*100)+'%입니다. \n'+result[numCheck])

        #print('체크되었습니다.')
        #tkinter.messagebox.showinfo('제목','내용')
        #answer = tkinter.messagebox.askyesno('제목','오징어 게임에 참가하시겠습니까?')
        #if answer == True:
            #print('동의')
        #else :
            #print('거절')
    #else:
        #print('체크가 해제되었습니다.')


#버튼클릭시
def btnClick():

    
#캔버스 생성
canvas = tkinter.Canvas(root, width=800, height=600, bg='skyblue')
canvas.pack()

#캔버스 내 이미지 생성
bgimg = tkinter.PhotoImage(file="mina.png")
canvas.create_image(400,300,image=bgimg)

#좌표 출력기
root.bind('<Motion>',mouseMove)
labelMouse = tkinter.Label(root,text=',', font=('맑은고딕', 10))
labelMouse.pack()


cvalue1 = tkinter.BooleanVar()
cvalue1.set(False)
cvalue2 = tkinter.BooleanVar()
cvalue2.set(False)
cvalue3 = tkinter.BooleanVar()
cvalue3.set(False)
cvalue4 = tkinter.BooleanVar()
cvalue4.set(False)
cvalue5 = tkinter.BooleanVar()
cvalue5.set(False)
cvalue6 = tkinter.BooleanVar()
cvalue6.set(False)
cvalue7 = tkinter.BooleanVar()
cvalue7.set(False)

#체크버튼
cbtn1 = tkinter.Checkbutton(text="높은 곳이 좋다",variable=cvalue1,command=chkBtnClick,bg='#cfffe5')
cbtn1.place(x=404,y=163)

cbtn2 = tkinter.Checkbutton(text="공을 보면 굴리고 싶어진다",variable=cvalue2,command=chkBtnClick,bg='#cfffe5')
cbtn2.place(x=404,y=204)

cbtn3 = tkinter.Checkbutton(text="깜짝 놀라면 털이 곤두선다",variable=cvalue3,command=chkBtnClick,bg='#cfffe5')
cbtn3.place(x=404,y=244)

cbtn4 = tkinter.Checkbutton(text="쥐구멍이 마음에 든다",variable=cvalue4,command=chkBtnClick,bg='#cfffe5')
cbtn4.place(x=404,y=284)

cbtn5 = tkinter.Checkbutton(text="개에게 적대감을 느낀다",variable=cvalue5,command=chkBtnClick,bg='#cfffe5')
cbtn5.place(x=404,y=324)

cbtn6 = tkinter.Checkbutton(text="생선 뼈를 발라 먹고 싶다",variable=cvalue6,command=chkBtnClick,bg='#cfffe5')
cbtn6.place(x=404,y=364)

cbtn7 = tkinter.Checkbutton(text="밤,기운이 난다",variable=cvalue7,command=chkBtnClick,bg='#cfffe5')
cbtn7.place(x=404,y=404)


#텍스트창 생성
text = tkinter.Text()
text.place(x=333,y=51,width=692,height=128)

btn = tkinter.Button(text='진단하기',font=('맑은 고딕', 25),bg='#cfffe5',command=chkBtnClick)
btn.place(x=406,y=479,width=100,height=120)

root.mainloop()
