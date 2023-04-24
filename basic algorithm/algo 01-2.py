# 1부터 n까지 정수 합 구하기 while문

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요.:'))

sum = 0
i = 1

while i <= n:  # i가 n보다 작거나 같을 동안 반복
    sum += i  # sum에 i를 더함
    i += 1  # i에 1을 더함

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

# 1부터 n까지 정수 합 구하기 for 문

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요.:'))

sum = 0
for i in range(1, n + 1):
    sum += i

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

# 연속하는 정수의 합

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.'))
b = int(input('정수 b를 입력하세요.'))

if a > b:
    a, b = b, a  # a와b를 오름차순으로 정렬

sum = 0
for i in range(a, b + 1):
    sum += i

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')

# a부터 b까지 정수의 합 구하기 1

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.'))
b = int(input('정수 b를 입력하세요.'))

if a > b:
    a, b = b, a  # a와b를 오름차순으로 정렬

sum = 0
for i in range(a, b + 1):
    if i < b:
        print(f'{i}+', end='')  # i가 b보다 작을때 합을 구하는 과정 3+ , 4+ , ...
    else:
        print(f'{i}=', end='')  # i가 b보다 크거나 같으면 최종값 출력을 위해 i= 를 출력 7= , 8= , ...
    sum += i

print(sum)

## a부터 b까지 정수의 합 구하기 1

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.'))
b = int(input('정수 b를 입력하세요.'))

if a > b:
    a, b = b, a  # a와b를 오름차순으로 정렬

sum = 0
for i in range(a, b):
    print(f'{i}+', end='')
    sum += i

print(f'{b} = ', end='')
sum += b

print(sum)

#+와 -를 번걸아 출력하기1

print('+와 -를 번갈아 출력합니다.')
n=int(input('몇 개를 출력할까요?'))

for i in range(n):
    if i % 2:
        print('-',end='') #홀수
    else:
        print('+',end='') #짝수
print()


print('-'*27)
#+와 -를 번갈아 출력하기 2

print('+와 -를 번갈아 출력합니다.')
n=int(input('몇 개를 출력할까요?'))

for _ in range(n//2):
    print('+-',end='')  # +-를 n//2개의 출력
if n % 2:
    print('+',end='') # n이 홀수일ㄸ대만 + 출력

print()

