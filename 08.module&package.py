# 패키지 (package)
# 직접 모든 기능을 만들지 않아도, 이미 만들어진 기능들을 이용하여, 더 빠르고 쉽게 개발할 수 있다.

# 1. pip로 패키지 설치하기
# pip install 패키지 이름
# 터미널에 위와 같은 명령어를 입력하여 패키지를 설치한다.
from forex_python.converter import CurrencyRates

# 환율 정보를 가져오기
c = CurrencyRates()
usd_to_krw = c.get_rate('USD', 'KRW')
print(f"1달러는 {usd_to_krw:.2f} 원입니다.")
# 설치된 패키지 목록 확인하기
# 'pip list'이라고 터미널에 써준다면 설치된 패키지를 전부 확인 할 수 있다.
# 3. 패키지 업데이트와 제거
# pip install --upgrade (package name) <-- 업데이트 방식
# pip uninstall (package name) <-- 제거 방식
