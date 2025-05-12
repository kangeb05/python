# test.txt 파일을 읽어와서 
# outTest.txt 파일에 작성한다.

inFile = open("test.txt","r",encoding="UTF-8")
outfile = open("outTest.txt","w",encoding="UTF-8")

#파일 읽어서 쓰기
while True:
    strFile = inFile.readline()    
    if(strFile==""):
        break
    #strFile
    strFileChange = ""
    for ch in strFile:
        #암호화
        chNum = ord(ch)
        chNum = chNum + 100
        chChange = chr(chNum)
        #기록
        strFileChange += chChange
    outfile.writelines(strFileChange)

inFile.close()
outfile.close()