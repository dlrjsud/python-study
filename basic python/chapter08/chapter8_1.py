# 데이터 속성 메서드

class Person:  # 클래스 정의
    def getName(self):  # 메서드 정의
        return self.name  # 데이터 속성을 나타내느 데는 self를 사용

    def getAge(self):
        return self.age


pr = Person()  # 인스턴스를 작성
pr.name = '김영진'
pr.age = 23  # 데이터 속성에 값 대입

n = pr.getName()
a = pr.getAge()  # 메서드 호출

print(n, '씨는', a, '세입니다.')


# 여러개의 인스턴스

class Person:
    def getName(self):
        return self.name

    def getAge(self):
        return self.age


pr1 = Person()
pr1.name = '이권형'
pr1.age = 29
n1 = pr1.getName()
a1 = pr1.getAge()

pr2 = Person()
pr2.name = '이거녕'
pr2.age = 28
n2 = pr2.getName()
a2 = pr2.getAge()

print(n1, '씨는', a1, '세입니다')
print(n2, '씨는', a2, '세입니다')
