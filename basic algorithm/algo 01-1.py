# 알고리즘이란?

print('세 정수의 최댓값을 구합니다.')

a = int(input('정수 a의 값을 구하시오.'))
b = int(input('정수 b의 값을 구하시오.'))
c = int(input('정수 c의 값을 구하시오.'))

maximum = a  # maximum에 a의 값을 대입
if b > maximum: maximum = b  # b의 값이 max보다 크면 max에 b 값을 대입
if c > maximum: maximum = c  # c의 값이 max보다 크면 max에 c 값을 대입

print(f'최댓값은 {maximum}입니다.')

# 문자열과 숫자

print('이름을 입력하세요.:', end='')
name = input()
print(f'안녕하세요? {name} 님')


# f'aaa {AA} aa' {}안에는 input의 변수를 출력하기 위해 print문 맨 앞에 f를 넣는다

# 세 정수의 최댓값 구하기

def max3(a, b, c):
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum


print(f'max3(3,2,1)={max3(3, 2, 1)}')  # a>b>c
print(f'max3(3,2,2)={max3(3, 2, 2)}')  # a>b=cd


# 세 정수를 입력받아 중앙값 구하기

def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b


print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.:'))
b = int(input('정수 b의 값을 입력하세요.:'))
c = int(input('정수 c의 값을 입력하세요.:'))

print(f'중앙값을 {med3(a, b, c)}입니다.')


# 중앙값 구하는 또 다른 방법

def med3(a, b, c):
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    else:
        return c


print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.:'))
b = int(input('정수 b의 값을 입력하세요.:'))
c = int(input('정수 c의 값을 입력하세요.:'))

print(f'중앙값을 {med3(a, b, c)}입니다.')

#입력받은 정수의 부호 (양수,음수,0) 출력하기

n=int(input('정수를 입력하셈'))

if n>0:
    print('양수')
elif n<0:
    print('음수')
else:
    print('0 입니다.')

#분기하는 조건문

n=int(input('정수 입력'))

if n==1:
    print('A')
elif n==2:
    print('B')
else:
    print('C')

#4개로 분기

n=int(input('정수 입력'))

if n==1:
    print('A')
elif n==2:
    print('B')
elif n==3:
    print('C')
else:
    pass
