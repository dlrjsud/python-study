# if (조건이 true) elif(조건1이 false 조건2가 true) else(모든 조건이 false일때)

sale = int(input('매출액을 입력하세요.'))

if sale >= 100:
    print('매출은 순조롭습니다.')
elif sale >=50:
    print('매출은 보통입니다.')
else:
    print('매출은 저조합니다.')
print('처리를 종료합니다.')
