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

