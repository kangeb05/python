import tkinter
import tkinter.font
root = tkinter.Tk()


# 총 매출액 계산 출력 함수
def click_calculation():
    # 물품 수량 변수    
    countCoffee_Sell = int(entry1_1.get())
    countSamkim_Sell = int(entry1_2.get())
    countBanana_Sell = int(entry1_3.get())
    countLunch_Sell = int(entry1_4.get())
    countCoke_Sell = int(entry1_5.get())
    countShrimp_Sell = int(entry1_6.get())

    countCoffee_Cost = int(entry2_1.get())
    countSamkim_Cost = int(entry2_2.get())    
    countBanana_Cost = int(entry2_3.get())    
    countLunch_Cost = int(entry2_4.get())    
    countCoke_Cost = int(entry2_5.get())    
    countShrimp_Cost = int(entry2_6.get()) 


    # 총 매출액 계산
    total = 0

    total += countCoffee_Sell * 1800
    total += countSamkim_Sell * 1400
    total += countBanana_Sell * 1800
    total += countLunch_Sell * 4000
    total += countCoke_Sell * 1500
    total += countShrimp_Sell * 2000

    total -= countCoffee_Cost * 500
    total -= countSamkim_Cost * 900
    total -= countBanana_Cost * 800
    total -= countLunch_Cost * 3500
    total -= countCoke_Cost * 700
    total -= countShrimp_Cost * 1000


    str1 = '오늘 총 매출액은 ' + str(total) + '원 입니다.'
    labelRes = tkinter.Label(root, text=str1, font=('돋움', 10))
    labelRes.place(x=100, y=200)


# 화면 설정
root.title('CU')
root.geometry('600x250')


# 항목 라벨
lbSell = tkinter.Label(root, text='판매 수량', font=('돋움',10))
lbCost = tkinter.Label(root, text='구매 수량', font=('돋움',10))
coffee = tkinter.Label(root, text='캔 커피', font=('돋움',10))
samkim = tkinter.Label(root, text='삼각김밥', font=('돋움',10))
banana = tkinter.Label(root, text='바나나 우유', font=('돋움',10))
lunch = tkinter.Label(root, text='도시락', font=('돋움',10))
coke = tkinter.Label(root, text='콜라', font=('돋움',10))
shrimp = tkinter.Label(root, text='새우깡', font=('돋움',10))

lbSell.place(x=10, y=70)
lbCost.place(x=10, y=120)
coffee.place(x=70, y=28)
samkim.place(x=150, y=28)
banana.place(x=230, y=28)
lunch.place(x=328, y=28)
coke.place(x=418, y=28)
shrimp.place(x=498, y=28)



# 수량 입력칸 설정
entry1_1 = tkinter.Entry(width=5)
entry1_2 = tkinter.Entry(width=5)
entry1_3 = tkinter.Entry(width=5)
entry1_4 = tkinter.Entry(width=5)
entry1_5 = tkinter.Entry(width=5)
entry1_6 = tkinter.Entry(width=5)

entry1_1.place(x=75, y=70)
entry1_2.place(x=160, y=70)
entry1_3.place(x=245, y=70)
entry1_4.place(x=330, y=70)
entry1_5.place(x=415, y=70)
entry1_6.place(x=500, y=70)


entry2_1 = tkinter.Entry(width=5)
entry2_2 = tkinter.Entry(width=5)
entry2_3 = tkinter.Entry(width=5)
entry2_4 = tkinter.Entry(width=5)
entry2_5 = tkinter.Entry(width=5)
entry2_6 = tkinter.Entry(width=5)

entry2_1.place(x=75, y=120)
entry2_2.place(x=160, y=120)
entry2_3.place(x=245, y=120)
entry2_4.place(x=330, y=120)
entry2_5.place(x=415, y=120)
entry2_6.place(x=500, y=120)



# 계산 버튼
calculation = tkinter.Button(root, text='계산', font=('돋움', 10), command=click_calculation)
calculation.place(x=100, y= 160, width=400)

root.mainloop()
