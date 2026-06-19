# 파일 입출력

# 파일 쓰기
upsidedown=open(r"C:/Users/choib/OneDrive/문서/python/study/viralmustgoviral.txt","w",encoding="utf-8")
upsidedown.write("the song upside down is good too.....!!!!")
upsidedown.close()

#파일 추가 (use write)
ADIOS=open(r"C:/Users/choib/OneDrive/문서/python/study/viralmustgoviral.txt","a",encoding="utf-8")
ADIOS.write("젊음은 가 아픔도 떠나가...... 못내 아픈 청춘이여!!!!!")
ADIOS.close()

# 파일 열기
a=open(r"C:/Users/choib/OneDrive/문서/python/study/viralmustgoviral.txt","r",encoding="utf-8")
bnd=a.read()
#viral=a.readline()
#home=a.readlines()
print(bnd)
#print(viral)
#print(home)
a.close()

# 알면 좋은거
# r = 읽기 모드
# r + = 읽기 및 쓰기 모드
# w = 쓰기 모드
# w+ = 읽기 및 쓰기 모드 (기존 내용 삭제)
# a= 추가 모드
# a+ = 읽기 및 추가 모드

# with문 활용 파일 열기
with open(r"C:/Users/choib/OneDrive/문서/python/study/viralmustgoviral.txt","r+",encoding="utf-8") as dophamine:
    caffeine=dophamine.read()
    print(caffeine)
