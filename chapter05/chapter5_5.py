# 리스트의 연결과 슬라이스

sale1 = [1, 2, 3, 4, 5, 6]
print('상반기 데이터는', sale1, '입니다.')

sale2 = [7, 8, 9, 10, 11, 12]
print('하반기 데이터는', sale2, '입니다.')

ysale = sale1 + sale2  # 리스트끼리 연결

print('연각 데이터는', ysale, '입니다.')  # 리스트가 연결됨

# 슬라이스로 지정

ysale = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print('연간 데이터는', ysale, '입니다.')

sale1 = ysale[0:6]  # 인덱스가 0부터 5
print('상반기 데이터는', sale1, '입니다.')

sale2 = ysale[6:]  # 인덱스가 6 이후
print('하반기 데이터는', sale2, '입니다.')

sale3 = ysale[::2]  # 간격 2/1 지정
print('1개월 거른 데이터는', sale3, '입니다.')

sale4 = ysale[::-1]  # 간격을 마이너스하면 역순
print('역순 데이터는', sale4, '입니다.')

print('연간 데이터는', ysale, '입니다.')
print('상반기 데이터를 바꿔 넣습니다.')
ysale[:6] = [0, 0, 0, 0, 0, 0, ]  # 슬라이스로의 대입에 따라 값 변경 가능
print('연간 데이터는', ysale, '입니다')

# 리스트를 역순으로

data = [1, 2, 3, 4, 5]
print('현재 데이터는', data, '입니다.')

print('data[::-1]을 for 문으로 처리합니다.')
for d in data[::-1]:  # *슬라이스로 처리
    print(d)  # 1.역순으로 처리 되지만
print('data[::-1]은', data[::-1], '입니다.')
print('현재 데이터는', data, '입니다.')  # 2.원래 데이터는 변경x

print('reversed(data)를 for 문으로 처리합니다.')
for d in reversed(data):  # *reversed()함수로 처리
    print(d)  # 3.역순으로 처리 되지만
print('reversed(data)는', reversed(data), '입니다.')  # 4. 데이터 변경x
print('현재 데이터는', data, '압나다.')

print('data.reverse()를 처리합니다.')  # *reversed()메서드로 처리
data.reverse()
print('현재 데이터는', data, '입니다.')  # 5.원래 데이터 역순으로 변경
