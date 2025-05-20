# 고양이 지수 진단 프로그램
# 체크 버튼 실습 예제

import tkinter # 그래픽 사용 모듈 가져오기
'import tkinter.messagebox' # 메시지 박스(창 안의 창) 묘듈 가져오기(없어도 됨 고양이 실습 예제가 아니라 앞에 메시지 박스 연습할 때 씀)

root = tkinter.Tk() # 창 변수 선언하기(코드 내에서 창을 부르는 이름)
root.title("고양이 지수 진단 게임") #창 제목 설정하기 (사용자에게 보여지는 창의 이름)

# 진단 결과값 저장 리스트
result = [
    "전생에 고양이었을 가능성은 매우 낮습니다.",
    "보통 사람입니다.",
    "특별히 이상한 곳은 없습니다.",
    "꽤 고양이 다운 구석이 있습니다.",
    "고양이와 비슷한 성격 같습니다.",
    "고양이와 근접한 성격입니다.",
    "전생에 고양이었을지도 모릅니다.",
    "겉모습은 사람이지만, 속은 고양이일 가능성이 있습니다."
]

# 좌표 출력기 함수
def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse.config(text=str(x)+','+str(y))
    labelMouse.place(x=0,y=200)

# 체크 버튼에 대한 함수 (였으나 교수님께 필요한 지 여쭤보니 지워버리심, 어차피 btnClick에 포함됨,
# 다만 여기 있었을 때는 실시간으로 체크 개수가 체크 되었지만 이제 진단하기 버튼을 눌러야 터미널에 개수가 표시됨.)
def chkBtnClick():
    pass

# 진단하기 버튼에 대한 함수
def btnClick():
    numcheck = 0
    if cvalue1.get() == True: numcheck += 1
    if cvalue2.get() == True: numcheck += 1
    if cvalue3.get() == True: numcheck += 1
    if cvalue4.get() == True: numcheck += 1
    if cvalue5.get() == True: numcheck += 1
    if cvalue6.get() == True: numcheck += 1
    if cvalue7.get() == True: numcheck += 1
    print(numcheck) 
    textFilled.delete("1.0",tkinter.END)
    textFilled.insert("1.0", "<진단결과>\n당신의 고양이 지수는"
                      +str(int(numcheck/7*100)) + "%입니다. \n"
                      +result[numcheck])


# 캔버스
canvas = tkinter.Canvas(root, width=800, height=600, bg = "#FFFFFF") #캔버스 만들기
canvas.pack() #캔버스 위치 설정 (place는 좌표 조정 가능, pack은 창의 왼쪽 상단 꼭짓점에서 시작)

bgtimg = tkinter.PhotoImage(file="mina.png") # 캔버스에 넣을 이미지 변수 선언하기
canvas.create_image(400,300,image=bgtimg) # 이미지를 캔버스에 넣기 (좌표는 이미지 넣을 위치의 중앙값)

# 진단하기 버튼 만들기 / 위치 설정하기
btn = tkinter.Button(root, text='진단하기', font=('맑은 고딕', 30), bg='green',command=btnClick)
btn.place(x=410, y=480)

# 체크 밸류 만들기 / 체크 밸류 설정하기(체크 박스 켜졌는지 아닌지)  /// 체크 버튼 만들기 / 위치 설정
# 체크 버튼 하나에 들어가는 코드를 모아놔서 밸류랑 버튼이 왔다갔다 하는데 밸류랑 버튼으로 구분해서 한 번에 적는 게 보기 편함
ygap = 40 # 체크 버튼 y좌표 변화값
cvalue1 = tkinter.BooleanVar()
cvalue1.set(False)

cbtn1 = tkinter.Checkbutton(text="높은 곳이 좋다", bg='#CFFFE5', variable=cvalue1,command=chkBtnClick)
cbtn1.place(x=410, y=165+ygap*0) # ygap에서 체크 버튼 사이의 간격을 받아와서 더해줌

cvalue2 = tkinter.BooleanVar()
cvalue2.set(False)

cbtn2 = tkinter.Checkbutton(text="공을 보면 굴리고 싶어진다", bg='#CFFFE5', variable=cvalue2,command=chkBtnClick)
cbtn2.place(x=410, y=165+ygap*1) # 40씩 내려갈 때마다 곱해지는 값이 1 늘어남

cvalue3 = tkinter.BooleanVar()
cvalue3.set(False)

cbtn3 = tkinter.Checkbutton(text="깜짝 놀라면 털이 곤두선다", bg='#CFFFE5', variable=cvalue3,command=chkBtnClick)
cbtn3.place(x=410, y=165+ygap*2)

cvalue4 = tkinter.BooleanVar()
cvalue4.set(False)

cbtn4 = tkinter.Checkbutton(text="쥐구멍이 마음에 든다", bg='#CFFFE5', variable=cvalue4,command=chkBtnClick)
cbtn4.place(x=410, y=165+ygap*3)

cvalue5 = tkinter.BooleanVar()
cvalue5.set(False)

cbtn5 = tkinter.Checkbutton(text="개에게 적대감을 느낀다", bg='#CFFFE5', variable=cvalue5,command=chkBtnClick)
cbtn5.place(x=410, y=165+ygap*4)

cvalue6 = tkinter.BooleanVar()
cvalue6.set(False)

cbtn6 = tkinter.Checkbutton(text="생선 뼈를 발라 먹고 싶다", bg='#CFFFE5', variable=cvalue6,command=chkBtnClick)
cbtn6.place(x=410, y=165+ygap*5)

cvalue7 = tkinter.BooleanVar()
cvalue7.set(False)

cbtn7 = tkinter.Checkbutton(text="밤, 기운이 난다", bg='#CFFFE5', variable=cvalue7,command=chkBtnClick)
cbtn7.place(x=410, y=165+ygap*6)

# 진단 결과를 나타내는 텍스트 창
textFilled = tkinter.Text() #텍스트 창 변수 선언
textFilled.place(x=365, y=30, width=395, height=95) #텍스트 창 위치 설정

#마우스 좌표 라벨
root.bind('<Motion>',mouseMove)
labelMouse = tkinter.Label(root, text=',', font=("맑은 고딕", 10))
labelMouse.pack()

root.mainloop()
