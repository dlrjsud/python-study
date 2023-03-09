# 반환 값

def sell(place, price, num):
    print(place, '지점에서', num, '회사에', price, '만 원 판매가 되었습니다.')
    tt = price * num
    return tt  # 반환 값 반환


total = sell('서울', 100, 5)
print('매출액은', total, '만 원이었습니다.')

#여러개의 반환값 반환

def sell():
    y=2023
    m=3
    d=20
    print(y,'년',m,'월',d,'일에 판매가 되었습니다.')
    return y,m,d
sy,sm,sd = sell()
print('판매 종료',sy,sm,sd)
