for i in range(6):
    for j in range(6, i, -1):
        print(' ', end='')
    for j in range((i + 1) * 2 - 1):
        print('*', end='')
    print()

print('-------------------------------------------')

for i in range(6):
    for j in range(6, i, -1):
        print('*', end='')
    for j in range((i - 6) * 2 - 1):
        print(' ', end='')
    print()

print('----------------------------------')

n = int(input('정수를 입력하세요'))
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

print('---------------------------------')

n = int(input('정수를 입력하세요'))
for i in range(n):
    print(' ' * (n - i) + '*' * (2 * i + 1))

print('----------------------------------')

n = int(input('정수를 입력하세요'))
for i in range(1, n + 1):
    print(' ' * (n - i))
    print('*' * (2 * i - 1))

print('------------------------------------------')

for i in range(3):
    for j in range(3):
        print(' ',end='')
    for j in range(-i+2):
        if (i%2==0):
            print('*',end='-')
        else:
            print(i%2==1,'*')
    print()