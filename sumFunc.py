def func(user):
    print(user + "님. 두 숫자를 입력하세요.")
    num1 = int(input("정수1 ==> "))
    num2 = int(input("정수2 ==> "))
    hap = num1 + num2
    return hap

def calc(v1, v2, op):
    result = 0
    if op == "+":
        result = v1 + v2
    if op == "-":
        result = v1 - v2
    if op == "*":
        result = v1 * v2
    if op == "/":
        result = v1 / v2

    return(result)

    

op = input("계산 입력 ==> ")
v1 = int(input("첫 번째 숫자 입력 : "))
v2 = int(input("두 번째 숫자 입력 : "))
value = calc(v1, v2, op) # op는 자동완성 뜰 때 기존에 설정한 값을 불러오는 마크? 같은 게 있음
print("##계산기 :", v1, op, v2, "=", value)


"""
hap = func("A")
print("결과: ", hap)
hap = func("B")
print("결과: ", hap)
hap = func("C")
print("결과: ", hap)
"""
