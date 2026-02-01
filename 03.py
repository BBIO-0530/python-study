# Dictionary 
#딕셔너리는 데이터를 키와 값을 쌍으로 저장하는 자료 구조입니다. 중괄호로 정의되며 각 항목은 콜론으로 구분됩니다.
a={"fruits":"foods","meat":"animal"}
print(a)
#값 접근하기
# 딕셔너리에서 특성 키의 값을 가져올때는 대괄호를 사용합니다. 
b=a["fruits"]
print(b)
# 값 추가 및 수정하기
# 딕셔너리에는 새로운 키 값을 추가하거나 기존 키의 값을 수정할 수 있습니다.
a["fruits"]="plant"
print(a)
a["cat"]="fur"
print(a)
# 값 제거하기
#딕셔너리에서 특전 키 값을 제거할 때 "del" 키워드를 사용합니다.
del a["fruits"]
print(a)
# 모든 키와 값 돌아가며 출력하기
for key, value in a.items():
    print(f"{key}: {value}")
# 모든 키 가져오기
c=a.keys()
print(c)
# 모든 값 가져오기
d=a.values()
print(d)
BND={"members":"Sungho,Riwoo,Jaehyun,Taesan,Leehan,Woonhak",
    "Wonderstick":"BND light stick",
    "HYBE LABLES":"lable of BND",
    "KOZ":"BND's entertainment",
    "ONEDOOR":"BND fans"}
BND["THE ACTION"]="BND's most famous album"
BND["KOZ"]="BND home entertaiment"
print(BND)
