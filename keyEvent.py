import tkinter

# 전역 변수
key = 0
cx = 400
cy = 300

# 함수 영역
def main_proc():
    global cx, cy, key
    #lable["text"] = key

    # 키보드 입력으로 위치 변경
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20 
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20

    # 시간에 따라 캐릭터가 내려감
    cy += 10
    
    
    # 변경된 위치의 경계를 확인
    if cy < 40 : cy = 40
    if cy > 600-40 : cy = 600-40
    if cx < 40 : cx = 40
    if cx > 800-40 : cx = 800-40


    # 변경된 위치에 이미지를 옮김
    canvas.coords("춘식",cx,cy)
    key = 0
    root.after(100, main_proc)

def key_down(e):
    global key
    key = e.keysym  #keycode

def key_up(e):
    global key
    key = 0

# 메인 영역
root = tkinter.Tk()
root.title("키 이벤트")
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)
#lable = tkinter.Label(font=('맑은 고딕',80))
#lable.pack()
canvas = tkinter.Canvas(width=800,height=600, bg='light yellow')
canvas.pack()

img = tkinter.PhotoImage(file="춘식.png")
canvas.create_image(400,300, image=img, tag="춘식")


main_proc()

root.mainloop()