# 인수

def sell(place):
    print(place, '지점의 판매가 되었습니다.')


sell('서울')
sell('대전')


# 실인수를 변수의 값으로

def sell(place):
    print(place, '지점의 판매가 되었습니다.')


shop = '서울'
sell(shop)  # 실인수로서  변수를 전달


# 여러 인수를 가진 함수 사용

def sell(place, num):  # 2개의 인수를 가진 함수
    print(place, '지점에서', num, '만 원 판매가 되었습니다.')  # 첫 번째 인수 출력 (place) 두번째 인수 출력 (num)


sell('서울', 5)  # 2개의 인수 전달

def func(**kwargs):
    print(kwargs)
func(a=1,b=2,c=3,d=4,e=5)