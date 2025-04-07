num = int(input('숫자 입력: '))

# <- 100 / 100 ~ 1000 / 1000 ->
# 1. 100 이하 조건
# 2. 1000 이하 조건
if num < 1000:
    if num > 100:
        print('100보다 작음')
    else:
        print('100보다 크고 1000보다 작음')
else:
    print('100보다 큼')



if num < 100:
    print('100보다 작음')
else:
    if num < 1000:
        print('100보다 크고, 1000보다 작음')
    else : 
        print('1000보다 큼')





if num % 2 == 0 : 
    print('짝수입니다')
else : 
    print('홀수입니다')

print('프로그램 종료')

