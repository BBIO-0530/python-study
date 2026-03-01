# 반복문
# 코드를 여러번 실행하고 싶을 때 사용하는 문법이다.
#for문
#for문은 주로 리스트, 문자열, 튜플 등과 같은 각 항목에 순서대로 접근해야 할때 사용합니다.
BND=["onedoor","members","ZICO"]
for i in BND:
    print(i)
#range 함수
#for문에서 반복 횟수를 지정해줄 수 있는 함수이다.
for a in range(10):
    print("BND the G.O.A.T")
#기본 사용법
# range(n)은 0부터 n-1까지의 숫자를 생성합니다.
# 시작점과 끝 지점
# range(start, stop)을 사용하면 start부터 stop-1까지의 숫자를 생성합니다.
# 증가폭 지정
# range(start, stop, step)을 사용하여 증가폭을 지정할 수 있습니다.
# 감소폭 지정
# range(start, stop, step)을 사용하여 감소폭을 지정할 수 있습니다.
for b in range(1,10,2):
    print(b)
#while 문 
#조건이 거짓이 될 때까지 반복하는 문법이다.
count=0
while count < 10:
    print(count)
    count += 1
#while True:
#    print("난 돈이 좋아")
# break 
# 반복문을 즉시 종료합니다.
#continue
# 현재 반복을 건너뛰고 다음 반복을 시행합니다.
for l in range(10):
    if l==4 or l==6:
        continue
    print(l)
else:
    print("돈이 최고야")
# 반복문에서 else는 반복문이 정상적으로 시행되었을 때 실행되는 역할이다.
# 중첩반복문 
# 반복문 안에 다른 반복문을 중첩시킨 구조.
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print("-")
# len 사용법 
# len은 글자 수를 찾는 함수이다.
members = ["박성호", "리우", "명재현", "태산", "이한", "김운학"]
for BND in members:
    if len(BND)%2==0:
        print(BND)
# (^^^^두 글자인 멤버 이름 출력^^^^)
for BND in members:
    if BND=="명재현":
        print("leader")
