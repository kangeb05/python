import tkinter
import random

# === 게임 설정 ===
GRID_W = 10
GRID_H = 12
CELL = 62
CANVAS_W = 912
CANVAS_H = 768

OFFSET_X = 20  # 왼쪽으로 더 이동
OFFSET_Y = 5   # 위쪽으로 더 이동

# === 변수 초기화 ===
index = 0
timer = 0
score = 0
hisc = 10000
difficulty = 0
tsugi = 0
destroyed_blocks = 0
game_time = 0  # 게임 시간 추가
wait_timer = 0  # 블럭 배치 대기 시간

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

def key_press(e):
    global index
    if e.keysym == "Escape" and index >= 2 and index <= 5:
        result = tkinter.messagebox.askyesno("게임 종료", "게임을 종료하시겠습니까?")
        if result:
            index = 0

# === 점수 파일 ===
def load_hisc():
    global hisc
    try:
        with open("hisc.txt", "r") as file:
            hisc = int(file.read())
    except:
        hisc = 1000

def save_hisc():
    try:
        with open("hisc.txt", "w") as file:
            file.write(str(hisc))
    except:
        pass

# === 블록 배열 ===
neko = [[0 for _ in range(GRID_W)] for _ in range(GRID_H)]
check = [[0 for _ in range(GRID_W)] for _ in range(GRID_H)]

def draw_neko():
    cvs.delete("NEKO")
    for y in range(GRID_H):
        for x in range(GRID_W):
            if neko[y][x] > 0:
                cvs.create_image(x * CELL + OFFSET_X + CELL//2,
                                 y * CELL + OFFSET_Y + CELL//2,
                                 image=img_neko[neko[y][x]], tag="NEKO")

def check_neko():
    for y in range(GRID_H):
        for x in range(GRID_W):
            check[y][x] = neko[y][x]

    # 세로 3개 연속
    for y in range(1, GRID_H - 1):
        for x in range(GRID_W):
            if check[y][x] > 0 and check[y - 1][x] == check[y][x] and check[y + 1][x] == check[y][x]:
                neko[y - 1][x] = neko[y][x] = neko[y + 1][x] = 7

    # 가로 3개 연속
    for y in range(GRID_H):
        for x in range(1, GRID_W - 1):
            if check[y][x] > 0 and check[y][x - 1] == check[y][x] and check[y][x + 1] == check[y][x]:
                neko[y][x - 1] = neko[y][x] = neko[y][x + 1] = 7

    # 대각선 3개 연속
    for y in range(1, GRID_H - 1):
        for x in range(1, GRID_W - 1):
            if check[y][x] > 0:
                if check[y - 1][x - 1] == check[y][x] and check[y + 1][x + 1] == check[y][x]:
                    neko[y - 1][x - 1] = neko[y][x] = neko[y + 1][x + 1] = 7
                if check[y + 1][x - 1] == check[y][x] and check[y - 1][x + 1] == check[y][x]:
                    neko[y + 1][x - 1] = neko[y][x] = neko[y - 1][x + 1] = 7

    # 4개 네모 패턴 체크 추가
    for y in range(GRID_H - 1):
        for x in range(GRID_W - 1):
            if (check[y][x] > 0 and 
                check[y][x] == check[y][x + 1] == check[y + 1][x] == check[y + 1][x + 1]):
                neko[y][x] = neko[y][x + 1] = neko[y + 1][x] = neko[y + 1][x + 1] = 7

def sweep_neko():
    count = 0
    for y in range(GRID_H):
        for x in range(GRID_W):
            if neko[y][x] == 7:
                neko[y][x] = 0
                count += 1
    return count

def drop_neko():
    moved = False
    for y in range(GRID_H - 2, -1, -1):
        for x in range(GRID_W):
            if neko[y][x] != 0 and neko[y + 1][x] == 0:
                neko[y + 1][x] = neko[y][x]
                neko[y][x] = 0
                moved = True
    return moved

def over_neko():
    for x in range(GRID_W):
        if neko[0][x] > 0:
            return True
    return False

def set_neko():
    for x in range(GRID_W):
        neko[0][x] = random.randint(0, difficulty)

def draw_txt(txt, x, y, siz, col, tag):
    fnt = ("Times New Roman", siz, "bold")
    cvs.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag=tag)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tag)

def game_main():
    global index, timer, score, hisc, difficulty, tsugi
    global cursor_x, cursor_y, mouse_c, destroyed_blocks, game_time, wait_timer

    if index == 0:
        draw_txt("야옹야옹", 312, 240, 100, "violet", "TITLE")
        cvs.create_rectangle(168, 384, 456, 456, fill="skyblue", width=0, tag="TITLE")
        draw_txt("Easy", 312, 420, 40, "white", "TITLE")
        cvs.create_rectangle(168, 528, 456, 600, fill="lightgreen", width=0, tag="TITLE")
        draw_txt("Normal", 312, 564, 40, "white", "TITLE")
        cvs.create_rectangle(168, 672, 456, 744, fill="orange", width=0, tag="TITLE")
        draw_txt("Hard", 312, 708, 40, "white", "TITLE")
        index = 1
        mouse_c = 0

    elif index == 1:
        difficulty = 0
        if mouse_c == 1:
            if 168 < mouse_x < 456 and 384 < mouse_y < 456:
                difficulty = 4
            if 168 < mouse_x < 456 and 528 < mouse_y < 600:
                difficulty = 5
            if 168 < mouse_x < 456 and 672 < mouse_y < 744:
                difficulty = 6
        if difficulty > 0:
            for y in range(GRID_H):
                for x in range(GRID_W):
                    neko[y][x] = 0
            score = 0
            destroyed_blocks = 0
            tsugi = 0
            cursor_x = 0
            cursor_y = 0
            game_time = 0  # 게임 시간 초기화
            wait_timer = 0  # 대기 시간 초기화
            set_neko()
            draw_neko()
            cvs.delete("TITLE")
            index = 2
        mouse_c = 0

    elif index == 2:
        if not drop_neko():
            index = 3
        draw_neko()

    elif index == 3:
        check_neko()
        draw_neko()
        index = 4

    elif index == 4:
        sc = sweep_neko()
        old_bonus = destroyed_blocks // 10
        destroyed_blocks += sc
        new_bonus = destroyed_blocks // 10
        bonus_score = (new_bonus - old_bonus) * 10
        score += sc * difficulty * 2 + bonus_score
        if score > hisc:
            hisc = score
            save_hisc()
        if sc > 0:
            index = 2
        else:
            if not over_neko():
                tsugi = random.randint(1, difficulty)
                wait_timer = 0  # 새 블럭이 나올 때 대기 시간 초기화
                index = 5
            else:
                index = 6
                timer = 0
        draw_neko()

    elif index == 5:
        wait_timer += 1  # 대기 시간 증가
        
        # 5초(50프레임) 이상 대기하면 자동으로 블럭 배치
        if wait_timer >= 50:
            # 빈 곳 중 랜덤하게 배치
            empty_positions = []
            for y in range(GRID_H):
                for x in range(GRID_W):
                    if neko[y][x] == 0:
                        empty_positions.append((x, y))
            if empty_positions:
                pos = random.choice(empty_positions)
                neko[pos[1]][pos[0]] = tsugi
                tsugi = 0
                set_neko()
                index = 2
        
        if OFFSET_X <= mouse_x < OFFSET_X + CELL * GRID_W and OFFSET_Y <= mouse_y < OFFSET_Y + CELL * GRID_H:
            cursor_x = (mouse_x - OFFSET_X) // CELL
            cursor_y = (mouse_y - OFFSET_Y) // CELL
            if mouse_c == 1:
                neko[cursor_y][cursor_x] = tsugi
                tsugi = 0
                set_neko()
                index = 2
            mouse_c = 0
        cvs.delete("CURSOR")
        cvs.create_image(cursor_x * CELL + OFFSET_X + CELL // 2,
                         cursor_y * CELL + OFFSET_Y + CELL // 2,
                         image=cursor, tag="CURSOR")
        draw_neko()

    elif index == 6:
        timer += 1
        if timer == 1:
            draw_txt("GAME OVER", 312, 348, 60, "red", "OVER")
        if timer == 50:
            cvs.delete("OVER")
            index = 0

    # 게임 진행 중일 때 시간 증가
    if index >= 2 and index <= 5:
        game_time += 1

    cvs.delete("INFO")
    draw_txt("SCORE " + str(score), 160, 60, 32, "blue", "INFO")
    draw_txt("HISC " + str(hisc), 450, 60, 32, "yellow", "INFO")
    draw_txt("DESTROYED " + str(destroyed_blocks), 160, 100, 24, "green", "INFO")
    draw_txt("TIME " + str(game_time // 10), 450, 100, 24, "orange", "INFO")  # 게임 시간 표시 추가
    
    # 보너스 점수 표시 추가 (10개마다 보너스)
    bonus_count = destroyed_blocks // 10
    if bonus_count > 0:
        draw_txt("BONUS x" + str(bonus_count), 160, 140, 20, "purple", "INFO")
    
    if tsugi > 0:
        cvs.create_image(OFFSET_X + GRID_W * CELL + 130, OFFSET_Y + 225, image=img_neko[tsugi], tag="INFO")
        # 대기 시간 표시 (5초 카운트다운)
        remaining_time = max(0, 5 - (wait_timer // 10))
        draw_txt("AUTO: " + str(remaining_time), OFFSET_X + GRID_W * CELL + 130, OFFSET_Y + 300, 20, "red", "INFO")

    root.after(100, game_main)

# === 초기화 ===
import tkinter.messagebox

root = tkinter.Tk()
root.title("블록 낙하 퍼즐 '야옹야옹'")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
root.bind("<KeyPress>", key_press)
root.focus_set()  # 키보드 이벤트를 받기 위해 포커스 설정

cvs = tkinter.Canvas(root, width=CANVAS_W, height=CANVAS_H)
cvs.pack()

bg = tkinter.PhotoImage(file="new_bg.png")
cursor = tkinter.PhotoImage(file="neko_cursor.png")
img_neko = [
    None,
    tkinter.PhotoImage(file="neko1.png"),
    tkinter.PhotoImage(file="neko2.png"),
    tkinter.PhotoImage(file="neko3.png"),
    tkinter.PhotoImage(file="neko4.png"),
    tkinter.PhotoImage(file="neko5.png"),
    tkinter.PhotoImage(file="neko6.png"),
    tkinter.PhotoImage(file="neko_niku.png")
]

load_hisc()
cvs.create_image(CANVAS_W // 2, CANVAS_H // 2, image=bg)
game_main()
root.mainloop()