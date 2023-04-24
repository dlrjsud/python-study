# 컨스트럭터(생성자)

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


pr = Person('조은아', 20)

n = pr.getName()
a = pr.getAge()

print(n, '씨는', a, '쨜입니다.')


