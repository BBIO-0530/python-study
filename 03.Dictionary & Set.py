# ==========================================
# 파이썬 기초 문법 (03. Dictionary & Set)
# ==========================================

# ------------------------------------------
# 1. 딕셔너리 (Dictionary)
# ------------------------------------------
# 딕셔너리는 데이터를 키(Key)와 값(Value)을 한 쌍으로 묶어서 저장하는 자료 구조입니다.
# 중괄호 {}로 정의되며, 각 항목은 콜론(:)으로 키와 값을 구분합니다.
a = {"fruits": "foods", "meat": "animal"}
print(a)

# 1.1 값 접근하기
# 딕셔너리에서 특정 키의 값을 가져올 때는 대괄호 []를 사용합니다. 
b = a["fruits"]
print(b)

# [보충] get() 메서드를 사용해서 접근할 수도 있습니다.
# 대괄호 방식은 없는 키를 부르면 에러가 나지만, get()은 None을 반환하여 프로그램이 멈추지 않게 해줍니다.
print(a.get("meat"))

# 1.2 값 추가 및 수정하기
# 딕셔너리에는 새로운 키-값 쌍을 추가하거나 기존 키의 값을 쉽게 수정할 수 있습니다.
a["fruits"] = "plant"  # 기존 키("fruits")의 값을 수정
print(a)
a["cat"] = "fur"       # 새로운 키("cat")와 값 추가
print(a)

# 1.3 값 제거하기
# 딕셔너리에서 특정 키-값을 제거할 때 "del" 키워드를 사용합니다.
del a["fruits"]
print(a)

# 1.4 모든 키와 값 돌아가며 출력하기 (items)
# [보충] items()는 키와 값을 튜플 형태로 묶어서 반환해 줍니다. 반복문(for)과 찰떡궁합입니다.
for key, value in a.items():
    print(f"{key}: {value}")

# 1.5 모든 키 가져오기 (keys)
c = a.keys()
print(c)

# 1.6 모든 값 가져오기 (values)
d = a.values()
print(d)


# ==========================================
# 2. 딕셔너리 실전 예제 (BOYNEXTDOOR)
# ==========================================
BND = {
    "members": "Sungho,Riwoo,Jaehyun,Taesan,Leehan,Woonhak",
    "Wonderstick": "BND light stick",
    "HYBE LABLES": "label of BND",
    "KOZ": "BND's entertainment",
    "ONEDOOR": "BND fans"
}

BND["THE ACTION"] = "BND's most famous album" # 새로운 앨범 정보 추가
BND["KOZ"] = "BND home entertainment"         # 기존 KOZ 정보 수정
print(BND)


# ------------------------------------------
# 3. 집합 (Set)
# ------------------------------------------
# 중복되지 않는 고유한 값들만 저장하는 자료 구조입니다. 
# 중괄호 {}로 정의되지만, 딕셔너리와 달리 키:값 쌍이 아니라 값만 들어갑니다.
# [보충] 집합은 순서가 보장되지 않으므로 인덱스(예: Albums[0])를 사용할 수 없습니다.
Albums = {"WHO!", "HOW?", "Why..", "And,", "No Genre", "19.99", "boylife", "THE ACTION"}
print(Albums)

# 3.1 항목 추가하기 (add)
Albums.add("WHO!(crunch ver.)")
print(Albums)

# 3.2 항목 제거하기 (remove)
Albums.remove("WHO!(crunch ver.)")
print(Albums)


# ==========================================
# 4. 집합의 수학적 연산
# ==========================================
numbersa = {"one", "two", "three"}
numbersb = {"three", "four", "five"}

# 4.1 합집합 (union)
# a와 b의 모든 요소를 하나로 모은 집합 (중복된 "three"는 하나만 남습니다)
# [보충] 기호 `|` 를 사용하여 `numbersa | numbersb` 로 쓸 수도 있습니다.
print(numbersa.union(numbersb))

# 4.2 교집합 (intersection)
# a와 b에 공통적으로 속하는 요소들만 모은 집합
# [보충] 기호 `&` 를 사용하여 `numbersa & numbersb` 로 쓸 수도 있습니다.
print(numbersa.intersection(numbersb))

# 4.3 차집합 (difference)
# 한 집합에는 있지만, 다른 집합에는 없는 요소들로 이루어진 집합 (a - b)
# [보충] 기호 `-` 를 사용하여 `numbersa - numbersb` 로 쓸 수도 있습니다.
print(numbersa.difference(numbersb))


# ==========================================
# 5. 부분집합과 상위집합
# ==========================================
c = {"BBNEXDO", "SALAD DAYS", "BOYNEXTDOOR", "ZICO"}
d = {"BBNEXDO", "BOYNEXTDOOR"}

# 5.1 부분집합 (issubset)
# d의 모든 요소가 c에 포함되어 있는가? (True/False 반환)
print(d.issubset(c))  # True

# 5.2 상위집합 (issuperset)
# c가 d의 모든 요소를 다 품고 있는가? (True/False 반환)
print(c.issuperset(d)) # True


# ==========================================
# 6. 리스트를 집합으로 변환 (중복 제거 활용)
# ==========================================
# [보충] 리스트에 중복된 데이터가 있을 때, set()으로 변환하면 중복을 한 번에 날려버릴 수 있습니다!
year2025 = ["stanely", "slay queen", "sigma", "67", "41", "41", "rizz"]
meme = set(year2025)
print(meme)  # 중복되었던 "41"이 하나만 남아서 출력됩니다.


# ==========================================
# 7. 복합 구조 (딕셔너리 내부에 집합 사용)
# ==========================================
KPOP = {
    "BOYNEXTDOOR": {"HOLLYWOOD ACTION", "Sungho", "Riwoo", "Jaehyun", "Taesan", "Leehan", "Woonhak"},
    "Aespa": {"NEXT LEVEL", "Ningning", "Karina", "Winter", "Giselle"},
    "NewJeans": {"ATTENTION", "Minji", "Haein", "Hani", "Haerin"},
    "IVE": {"BANG BANG", "Gaeul", "Yujin", "Wonyoung", "Rei", "Leeseo"},
    "BLACK PINK": {"SHUT DOWN", "Jisoo", "Jenni", "Rose", "Lisa"},
}

KPOP["BOYNEXTDOOR"].add("bathroom")
KPOP["Aespa"].add("black magic")
KPOP["Aespa"].remove("black magic")
KPOP["Aespa"].add("Rich Man")
KPOP["NewJeans"].add("right now")

# [보충] 집합(Set)은 중복을 허용하지 않으므로, 이미 있는 "BANG BANG"을 추가해도 아무런 변화가 없습니다.
KPOP["IVE"].add("BANG BANG")

# [보충] 다른 그룹들은 {}를 써서 집합(Set)으로 만들었지만, 아래 (G)I-DLE은 소괄호 ()를 사용했으므로 튜플(Tuple) 구조로 추가됩니다.
KPOP["Idle"] = ("MONO", "Soyeon", "Minie", "YUQI", "Syuhua", "Miyeon") 

# [수정됨] 원본 코드의 괄호 에러( print(KPOP)) ) 수정
print(KPOP)
