# 1~12까지 8을 건너뛰고 출력 1

for i in range(1,13):
    if i == 8 :
        continue
    print(i, end=' ')
print()

print('-------------------------')

# 1~12 까지 8을 건너뛰고 출력 2

for i in list(range(1,8)) + list(range(9,13)):
    print(i, end=' ')
print()

print('-------------------------')

# 2자리 양수 10~99 입력 받기

print('2자리 양수 입력')

while True:
    no= int(input(' 값 입 력 : '))
    if no >10 and no <= 99:
        break
print(f'입력 받은 양수는 {no}입니다.')