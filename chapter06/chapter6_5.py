# 세트 조작

city = {'서울', '대전', '대구', '부산', '광주'}
print('현재 데이터는', city, '입니다.')

d = input('추가할 데이터를 입력하세요.')
if d in city:
    print(d, '이(가) 이미 존재합니다.')
else:
    city.add(d)
    print(d, '을(를) 추가했습니다.')
print('현재 데이터는', city, '입니다.')

d = input('삭제할 데이터를 입력하세요.')
if d in city:
    city.remove(d)
    print(d, '을(를) 삭제했습니다.')
else:
    print(d, '은 존재하지 않습니다.')
print('현재 데이터는', city, '입니다.')

# 세트 집합 연산

cityA = {'서울', '대전', '대구', '부산'}
cityB = {'대구', '부산', '광주'}

print('A의 도시명은', cityA, '입니다.')
print('B의 도시명은', cityB, '입니다.')

print('공통하는 데이터는', cityA & cityB, '입니다.')
print('A만의 데이터는', cityA - cityB, '입니다.')
print('B만의 데이터는', cityB - cityA, '입니다.')
print('모든 데이터는', cityA|cityB, '입니다.')
