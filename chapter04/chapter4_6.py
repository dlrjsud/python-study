# 구문 중첩

# for문 중첩
for i in range(5):  # 1
    for j in range(3):  # 1
        print('i는', i, ':j는,', j)  # 1,2

# if문 등과 조합
v = False

for i in range(5):
    for j in range(5):
        if v is False:
            print('*', end='')
            v = True
        else:
            print('-', end='')
            v = False
print()
