# 구구단 곱셈표 만들기

print('-' * 27)
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j : 3}', end='')
    print()
print('-' * 27)

# 직삼각형 만들기

n = int(input('정수 입력 : '))

for i in range(n):
    for j in range(i + 1):
        print('*', end='')
    print()

print('-' * 28)

# 직삼각형 만들기 2

n = int(input('정수 입력 : '))

for i in range(n):
    for j in range(n - i - 1):  # 공백을 먼저 출력
        print(' ', end='')
    for j in range(i + 1):
        print('*', end='')
    print()

print('-' * 28)

# 함수 내부 외부에서 정의한 변수와 객체의 식별 번호 출력

n = 1  # 전역 변수 (함수 내 외부에서 사용)

def put_id():
    x = 1  # 지역 변수 (함수 내부에서 사용)
    print(f'id(x) = {id(x)}')

print(f'id(1)={id(1)}')
print(f'id(n)={id(n)}')
put_id()

print('-' * 28)

# 1부터 100까지 반복하여 출력

for i in range(1,100):
    print(f'i={i:3} id(i)={id(i)}')
