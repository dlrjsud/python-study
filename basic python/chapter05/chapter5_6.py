# 리스트 요소 조합  zip(리스트1,리스트2,...)  emunerate(리스트명)

city = ['서울', '대전', '대구', '부산']
sale = [80, 60, 22, 50, 75]

print('도시명 데이터는', city, '입니다.')
print('매출액 데이터는', sale, '입니다.')

print('데이터를 조합합니다.')

for d in zip(city, sale):  # 리스트 2개가 조합됨
    print(d)

print('데이터와 인덱스를 조합합니다.')

for d in enumerate(city):  # 요소값과 인덱스 조합
    print(d)

# 리스트 요소 분해

city = ['서울', '대전', '대구', '부산']
sale = [80, 60, 22, 50, 75]

print('도시명 데이터는', city, '입니다.')
print('매출액 데이터는', sale, '입니다.')

print('데이터를 조합합니다.')

for d in zip(city, sale):  # 리스트 2개가 조합됨
    print(d)

print('데이터와 인덱스를 분해합니다.')

for c, s in zip(city, sale):  # 조합한 요소 분해
    print('도시명은', c, '매출은', s)

# 리스트로부터 새로운 리스트 얻기

data = [1, 2, 3, 4, 5]
print('현재 데이터는', data, '입니다.')

ndata = [n * 2 for n in data if n != 3]  # n*2 식의 값을 새로운 리스트의 요소 # n 요소를 변수에 꺼내 # n!조건이 True면

print('새로운 데이터는', ndata, '입니다.')
