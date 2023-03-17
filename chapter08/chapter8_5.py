# 파생 클래스 이용

class Person: #기저 클래스
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class Customer(Person): #파생 클래스
    def __init__(self, nm, ag, ad, tl):
        super().__init__(nm, ag) #기저 클래스의 데이터 속성을 초기화하기 위해 기저 클래스의 생성자 호출
        self.adr = ad
        self.tel = tl #추가한 데이터 속성

    def getName(self):
        return '고객 : ' + self.name

    def getAdr(self):
        return self.adr

    def getTel(self):
        return self.tel


pr = Customer('김영진', 23, 'aaa@aaa.aa.kr', '010-1111-2222')
nm = pr.getName()
ag = pr.getAge()
ad = pr.getAdr()
tl = pr.getTel()

print(nm, '씨는', ag, '세입니다')
print('메일 주소는', ad, '전화번호는', tl, '입니다.')
