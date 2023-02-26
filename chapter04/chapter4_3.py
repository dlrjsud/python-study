# 논리 연산자
sale = int(input('매출액을 입력하세요.'))
num = int(input('인원 수를 입력하세요.'))

if sale >= 100 and num >= 30:
    print('매출은 대성황입니다.')
elif sale >= 100:
    print('매출은 순조롭습니다.')
elif sale >= 50:
    print('매출은 보통입니다.')
else:
    print('매출은 저조합니다.')
print('처리를 종료합니다.')
