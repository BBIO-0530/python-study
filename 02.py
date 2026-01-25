# 리스트
# 리스트는 여러개의 값을 순서대로 저장할 수 있는 자료 구조입니다.
# 각 항목은 콤마로 구분되며, 값을 추가, 삭제, 수정할 수 있습니다.
BND=["onedoor","members","ZICO"]
# 인덱스
# 인덱스란, 리스트에 각 항목에 부여된 고유한 번호이다.
# 0 부터 시작한다.
print(BND[2])
print(BND[-2])
# 항목 추가하기 (append())
BND.append("HYBE")
print(BND[-1])
# 항목 삽입하기 (insert())
BND.insert(1,"songs")
print(BND)
# 항목 제거하기 (remove())
BND.remove("songs")
print(BND)
# 인덱스로 항목 제거하기 (pop())
BND.pop(3)
print(BND)
# 항목 찾기 (index())
a=BND.index("onedoor")
print(a)
#인댁스로 값 출력하기
print(BND[0]) 
# 리스트 슬라이싱
# 리스트의 특정 부분을 추출할때에 슬라이싱을 사용한다.
# 슬라이싱은 [start_index:stop_index:step] 형식으로 사용된다.
a = [0,1,2,3,4,5,6,7,8,9]
print(a[1:4]) #출력 값: 1 2 3
print(a[:5]) #출력 값: 0 1 2 3 4
print(a[::-1])
# 튜플 (tuple)
#튜플은 리스트와 유사하지만, 변하지 않은 데이터를 저장핼 때 사용됩니다. ()로 정의되며, 각 항목은 콤마로 구분됩니다
color=('red','blue','green')
print(color)
print(color[-1]) #튜플도 인덱스 값을 사용한다.
# 인덱스와 카운트가 사용 가능하다.
#카운트는 특정값이 몆번 나타나는 지 셀때 사용한다.
b= (1,1,1,2,3,3,4)
c=b.count(1)
print(c)
member=[('성호','03년생','54cm'),('리우','03년생','댄싱머신','개그'),('재현','03년생','똥강아지'),('태산','04년생','태마태'),('이한','04년생','물고기 왕자'),('운학','06년생','눈사람')]
print(member)
print({member[0][0]})
print(f"1. 이름 : {member[0][0]}  나이 : {member[0][1]} 특징 : {member[0][2]}")
print(f"2. 이름 : {member[1][0]}  나이 : {member[1][1]} 특징 : {member[1][2]}")
print(f"3. 이름 : {member[2][0]}  나이 : {member[2][1]} 특징 : {member[2][2]}")
print(f"4. 이름 : {member[3][0]}  나이 : {member[3][1]} 특징 : {member[3][2]}")
print(f"5. 이름 : {member[4][0]}  나이 : {member[4][1]} 특징 : {member[4][2]}")
print(f"6. 이름 : {member[5][0]}  나이 : {member[5][1]} 특징 : {member[5][2]}")
