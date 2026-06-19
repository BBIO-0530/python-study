# 예외 처리 
# 프로그램을 실행하는 동안 오류가 발생할 때에도 프로그램이 정상적으로 작동하게 만드는 방법이다

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "not able to divide :(("
#    except TypeError:
#        return "y r u typing letters"
    except Exception as e:
        return f"hiiii{e}"
print(divide("number one","number two" ))

#예외가 발생할 가능성이 있는 구문을 try 블럭에 작성을 하고, 예외가 발생 했을 때 처리할 코드를 except 블럭에 작성합니다.
# 하나의 오류(error)를 막고 싶다면 except 에러 이름을 쓰고, 전부 막고 싶다면 except Exception as 를 쓴다.
# else는 예외가 발생하지 않았을 때 실행되는 코드 블럭이다.
# finally는 예외 발생 여부와 상관 없이 항상 실행하는 코드 블럭으로, 주로 정리할 때에 사용 된다.

def divide2(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
    else:
        return f"결과: {result}"
    finally:
        print("계산이 완료되었습니다.")

# 사용자 정의 예외
# 사용자 정의 예외는 기본적으로 exception를 상속받아 정의됩니다.

class NegativeNumberError(Exception):
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("음수는 제곱근을 계산할 수 없습니다.")
    return x ** 0.5

try:
    print(square_root(-9))
except NegativeNumberError as e:
    print(e)
