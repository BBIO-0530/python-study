# 조건문 
# 특정 조건이 충족 될때만 특정 코드가 시행되게 하는 문법


# ==========================================


# if문
name = input("BND를 좋아하십니까??")

if name == "예":
    print("혹시 덕메 가능하실까요?:))")


# ==========================================


# if-else문
fan_or_not = input("onedoor이실 경우 onedoor를 입력해주십시오.")

if fan_or_not == "onedoor":
    print("지금부터 저의 덕메가 되셨습니다.")
else:
    print("BND 태산 얼윈파 직캠 한번 보실래요??")


# ==========================================


# if-elif-else문
if fan_or_not == "onedoor":
    print("지금부터 저의 덕메가 되셨습니다.")
elif fan_or_not == "잼도어":
    print("예의좀 가추시길요;;")
else:
    print("BND 태산 얼윈파 직캠 한번 보실래요??")


# ==========================================


# 중첩조건문
music = input("Spotify로 음악을 들으시나요 Youtube Music으로 들으시나요??")

if music == "Spotify":
    Q2 = input("premium, 아님 free plan으로요??")
    
    if Q2 == "premium":
        print("와 돈 많으시다")
