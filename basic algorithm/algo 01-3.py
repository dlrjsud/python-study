# *를 n개 출력히되 w개마다 줄바꿈

print('*룰 출력합니다.')
n = int(input('몇 개를 출력할까요?'))
w = int(input('몇 개마다 줄바꿈 할까요??'))

for i in range(n):
    print('*', end='')
    if i % w == w - 1:  # n번 판단
        print()  # 줄바꿈

if n % w:  # 1번 판단
    print()  # 줄바꿈

print('--------------------------------------')
# *를 n개 출력히되 w개마다 줄바꿈2

print('*룰 출력합니다.')
n = int(input('몇 개를 출력할까요?'))
w = int(input('몇 개마다 줄바꿈 할까요??'))

for _ in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)

print('--------------------------------------')

# 1부터 n까지 정수의 합 구하기 (n값은 양수만 입력)

print('1부터 n까지 정수의 합을 구합니다.')

while True:
    n = int(input('n값을 입력하세요.'))
    if n > 0:
        break  # n이 0보다 커질 때 까지 반복

sum = 0
i = 1

for i in range(1, n + 1):
    sum += i
    i += 1
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

print('--------------------------------------')

# 가로, 세로 길이가 정수 넓이가 area인 직사각형에서 변의 길이 나열

area = int(input('직사각형의 넓이를 입력'))
for i in range(1, area + 1):
    if i * i > area: break        # input에 입력한 사각형의 넓이보다 사각형의 넓이가 커지만 강제종료
    if area % i: continue         # area 가 i로 나누어 떨어지지 않고 나머지가 생기면 for문의 다음 반복문으로 진행
    print(f'{i} x {area // i}')   # i와 erea // i 의 값을 짧은변 긴 변순으로 나열

print('---------------------------------------')

#10 ~ 99 사이의 난수 n개 생성 (13이 나오면 중단)

import random

n= int(input('난수의 갯수를 입력하세요.'))

for _ in range(n):
    r = random.randint(10,99)
    print(r, end=' ')
    if r == 13:
        print('\n프로그램을 종료합니당')
        break

else:
    print('\n난수 생성을 종료합니당')

print('---------------------------------------')

