# 함수
# 합수는 코드에서 재사용성과 가독성을 높히는 기능이다.
def birthday():
    print("생일 축하해 :)")
birthday()
def a(d):
    c=input("생일을 입력해주세요!")
    if c=="3/15":
        print (f"생일 축하합니다 {d}님!! :)")
a("손")
# 반환값이 있는 함수
# 함수의 값을 호출한 곳으로 돌려 주고 싶을 때 사용한다.
def add(a,b):
    c=a+b
    print(c)
    return c
d=add(3,2)
print(d) 
# 기본 값이 있는 매개변수
def m(name,greet="안녕하세요!"):
    print(f"{greet}, {name}님!")
m("면희","환영합니다")
# 가변 매개변수
# *args 또는 **kwargs를 사용한다
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4, 5)
# *몇개의 변수를 사용하던 괜찮다*
# 람다함수
# 이름이 없는 함수로 간단한 기능을 한줄로 작성 할 때 쓴다.
add1= lambda x,y: x+y 
print(add1(500,30))

def BND(member1, member2):
    pair = {member1, member2}
    
    if pair == {"성호", "명재현"}:
        print("03즈 (명냥즈)")
    elif pair == {"성호", "리우"}:
        print("03즈 (상성즈)")
    elif pair == {"성호", "태산"}:
        print("깜치즈")
    elif pair == {"성호", "이한"}:
        print("물냥즈") 
    elif pair == {"성호", "운학"}:
        print("눈냥즈") 
    elif pair == {"리우", "명재현"}:
        print("개털날리즈 (혁명즈)")
    elif pair == {"리우", "태산"}:
        print("태리우스") 
    elif pair == {"리우", "이한"}:
        print("이리온즈") 
    elif pair == {"리우", "운학"}:
        print("두부즈")
    elif pair == {"태산", "명재현"}:
        print("띵동즈") 
    elif pair == {"명재현", "이한"}:
        print("물멍즈")
    elif pair == {"명재현", "운학"}:
        print("운명즈")
    elif pair == {"태산", "이한"}:
        print("동동즈/04즈")
    elif pair == {"태산", "운학"}:
        print("산학회") 
    elif pair == {"원도어", "보넥도"}:
        print("사랑입니다")
    else:
        print("조합을 찾지 못 했습니다 :(((((((")

BND("리우","태산")
BND("원도어","보넥도")
BND("ak","a")
