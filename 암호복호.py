inFile = open("outTest.txt","r",encoding="UTF-8")
while True:
    strFile = inFile.readline()
    if(strFile==""):
        break
    #strFile
    strFileChange = ""
    for ch in strFile:
        #암호화
        chNum = ord(ch)
        chNum = chNum - 100
        chChange = chr(chNum)
        #기록
        strFileChange += chChange
    
    print(strFileChange,end="")

inFile.close()