# 리스트 대입

data1 = [1, 2, 3, 4, 5]  # 리스트를
data2 = data1  # 다른 변수에 대입

print('data1은', data1, '입니다.')
print('data2는', data2, '입니다.')  # 2개의 변수는 하나의 리스트를 나타냄

data1[0] = 10  # 한 쪽의 변수에 대해 변경을 하면

print('data1은', data1, '입니다.')
print('data2는', data2, '입니다.')  # 다른 쪽도 변경됨

# 새로운 리스트 작성

data1 = [1, 2, 3, 4, 5]
data2 = list(data1)

print('data1은', data1, '입니다.')
print('data2는', data2, '입니다.')  # 두개의 변수는 다른 2개의 리스트를 나타냄

data1[0] = 10  # 한 쪽의 변수를 사용해서 변경해도

print('data1은', data1, '입니다.')
print('data2는', data2, '입니다.')  # 2개의 리스트는 다른 것으로 된다
