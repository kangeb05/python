var1 = '나는 Python을 열공 중입니다.'
var2 = '화이팅'
var3 = var1+var2
var4 = var2+var1

str1Len = len(var1)
str2Len = len(var2)


print('두 문자열 길이의 차이는'+str(str1Len-str2Len)+'입니다.')

var5 = var1.upper()
print(var5)
var6 = var1.lower()
print(var6)

print(var1[0])



var7 = '''
선배, 마라탕 사주세요 (그래, 가자)
선배, 혹시 탕후루도 같이? (뭐? 탕후루도?)
그럼 제가 선배 맘에
'''

# -1이 나오면 끝
numThang = var7.find('마라',6)
numThang = var7.find('마라',numThang+1)
numThang = var7.find('마라',numThang+1)
numThang = var7.find('마라',numThang+1)
numThang = var7.find('마라',numThang+1)
print(numThang)
