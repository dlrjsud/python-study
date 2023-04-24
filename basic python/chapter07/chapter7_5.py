# 함수를 리스트에 대입

def append():
    print('데이터를 추가합니다.')


def update():
    print('데이터를 갱신합니다.')


def delete():
    print('데이터를 삭제합니다.')


list = [append, update, delete]  # 함수를 리스트의 요소로 저장

res = int(input('조작할 번호를 입력하세요(0~2):'))

if 0 <= res and res < len(list):
    list[res]()  # 리스트의 요소로 함수 호출

# 람다함수

data = [1, 2, 3, 4, 5]

for d in map(lambda x: x * 2, data):  # 무명 함수와(lamda x : x * 2) 리스트(data)를 map()함수로 조합
    print(d)

data = [1, 2, 3, 4, 5]
for d in [x * 2 for x in data]:  # 이렇게 사용해도 됨
    print(d)


# 데코레이터로 함수에 기능 추가

def deco(func):  # 바깥쪽 함수에서 원래 함수로 받음
    def wrapper(x):
        wx = '---' + x + '---'
        return func(wx)  # 안쪽의 함수에서 처리, 원래 함수도 처리

    return wrapper  # 바깥쪽 함수가 안쪽의 함수를 반환값으로서 반환


@deco #데코레이션 지정
def printmsg(x):
    print(x, '를 입력했습니다.') # 함수에 기능 추가


str = input('메시지를 입력하세요.')

printmsg(str) # 함수 호출
