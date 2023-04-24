#딕셔너리 조작

sale = {'서울':80,'대전':60.,'대구':22,'부산':50,'광주':75}
print('현재 데이터는',sale,'입니다.')

print('키를 표시합니다.')
for k in sale.keys(): #키를 하나씩 반환하는 구조를 얻음
    print(k,end='\t')
print()

print('값을 표시합니다.')
for v in sale.values(): #값을 하나씩 반환하는 구조를 얻음
    print(v,end='\t')
print()

print('키와 값을 표시합니다.')
for i in sale.items(): # (키,값)이 되는 튜플을 하나씩 반환하는 구조를 얻음
    print(i,end='')
print()

#딕셔너리 갱신

sale1={'서울':80,'대전':60,'대구':22}
sale2={'대구':100,'부산':50,'광주':75}

print('1의 데이터는',sale1,'입니다.')
print('2의 데이터는',sale2,'입니다.')

print('1을 2로 갱신합니다.')

sale1.update(sale2) #다른 딕셔너리 요소 추가 갱신

print('1의 데이터는',sale1,'입니다.')