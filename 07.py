# 클레스(class)
# 클레스는 일종의 설계도이다. 이 설계도를 바탕으로 생성된 계별 항목을 객체 (Object) 혹은 인스턴스 (Instance)라고 한다.
#예시)
class KOZ: #클래스는 암묵적으로 첫 글자는 대문자로 시작해야 한다.
#__init__
#클레스의 생성자로, 겍체가 생성될때 자동으로 호출됩니다. 이를 통해, 객체 초기 속성을 설정할 수 있습니다.
#self
#생성괸 자신을 참조하는 변수로, 클레스 내 함수에서 반드시 첫 번째 매개 변수로 선언해야 합니다.
#예시)
    def __init__(self,BND, HYBELABLES):
        #속성 (Attribute):겍체의 상태나 데이터를 저장하는 변수입니다. 
        # 클레스의 생성자(__init__)에서 정의하며 'self.(속성 이름)'형태로 선언합니다.
        self.BND=BND
        self.HYBELABLES=HYBELABLES
        
    #함수 (Method): 겍체가 수행할 수 있는 동작을 정의하는 함수입니다.
    #클레스 내에서 정의되며, 첫 번째 매게 변수로 'self'를 사용하여 해당 겍체의 속성에 접근하거나 다른 함수를 호출할 수 있습니다.
    def name(self):
        print(f"{self.BND}(은/는) {self.HYBELABLES}와 KOZ에 소속되어 있습니다.")
a=KOZ("Taesan","HYBELABLES")
a.name()
#클레스 사용의 장점
#클레스를 사용하면, 관련 데이터와 함수를 하나의 논리적인 단위로 묶을 수 있기 때문에 코드의 재사용성과 유지보수성을 크게 향상시킬 수 있습니다.
#상속 (Inheritance)
#기존 클레스의 기능을 물려 받아 새로운 클레스를 생성하는 방법입니다. 이를 통해 코드의 중복 줄이고 기존 클레스의 기능을 확장할 수 있습니다.
class Animal:
    def __init__(self,codename):
        self.codename=codename

    def Speak(self):
        print(f"**{self.codename}소리**")
class Fox(Animal):
    def Speak(self):
        print(f"{self.codename}은/는 소리를 낸다")
ANIMAL=Fox("영숙이")
ANIMAL.Speak()
# 클레스 변수와 인스턴스 변수
#클레스 변수는 클레스 전체에서 공유되며, 인스턴스 변수는 각 객체마다 독립적으로 유지됩니다.
class circle:
    pi=3.14 #클레스 변수이다.
    def __init__(self,radius):
        self.radius=radius #인스턴스 변수이다.
    def area(self):
        return circle.pi*(self.radius**2)
