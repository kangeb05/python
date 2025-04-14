# 실습 1
# 팩토리아(!) 계산기 : 1부터 N까지의 곱
N = 5
res = 1
for i in range(1,N+1,1):
    res = res * i
#print(res)


# 연습1
# 1000 ~ 2000 사이에서 홀수의 합을 구하는 프로그램
hap = 0
for i in range(1001,2000,2):
    hap = hap + i
#print(hap)


# 중첩 for문
for i in range(0,3,1):
    for k in range(0,2,1):
        #print('i: ',i,'  k:',k)
        pass
    

# 실습2
# 2단부터 9단까지 구구단을 출력하는 구구단 계산기
#for num1 in range(2,10,1):   #단
    #print('구구단',num1,'단')
    #for num2 in range(1,10,1):    #곱해지는 수
        #print(num1,'X',num2,'=\t',num1*num2)


# while문
#i = 0
#while(i < 3):
    #print('ㅎ', end='')    #Ctrl c 누르면 정지함



while(True):
    num1 = int(input('숫자1 -> '))
    #num1이 0이면 반복문 종료
    if num1 == 0:
        break
    num2 = int(input('숫자2 -> '))
    print(num1,'+',num2,'=',num1+num2)

    
# 연습2
# 1부터 100까지를 더하되 4의 배수는 더하지 않음
# 3의 배수도 더하지 않음
res = 0
for i in range(1, 101,1):
    if i%4 == 0:
        continue
    elif i%3 == 0:
        continue
    res = res+i
print(res)






# for 반복문
#for i in range(1,10,1):
    #print(i, end=' ')

