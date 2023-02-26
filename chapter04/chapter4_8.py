print('1부터 10까지의 짝수를 표시하세요.')

for i in range(10):
    if (i + 1) % 2 == 0:
        print(i + 1)

print('1부터 10까지의 짝수를 표시하세요.')

for i in range(2, 11, 2):
    print(i)

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, '\t', end='')
        print()

v = False

for i in range(1, 6):
    for j in range(i):
        print('*', end='')
    print()
