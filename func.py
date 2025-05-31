def func2():
    result = 100 + num1 #파이썬은 전역 변수를 함수 안에서 읽을 수 있다.
    hap = result # 하지만 전역 변수를 쓰지는 못한다. 즉 이 hap과 함수 밖의 hap은 다른 변수다.
    globals
    hap = result #global 함수를 사용하면 전역 변수를 쓸 수 있다.
    "num1 = 1" # <= 여기서도 num1을 선언하면 함수 안의 지역 변수를 우선하기에 result 값이 101이 된다.
    return result

hap = 0
num1 = 10
hap = func2()
print("func2에서 돌려준 값 ==> ", hap)