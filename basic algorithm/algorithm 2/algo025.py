# 리스트의 모든 원소를 스캔(원소수 미리 파악)

x = ['Jhon', 'George', 'Paul', 'Ringo']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')

print('-' * 28)

# 리스트의 모든 원소를 enumerate() 함수로 스캔

x = ['Jhon', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x):
    print(f'[{i}] = {name}')

print('-' * 28)

# 리스트의 모든 원소를 enumerate() 함수로 스캔 1부터 카운트

x=['Jhon' , 'George' , 'Paul' , 'Ringo']

for i, name in enumerate(x,1):
    print(f'{i}번째 = {name}')

print('-'*28)

#리스트의 모든 원소를 스캔 ( 인덱스값을 사용하지 않음)

x=['조은아' , '쪼응아' , '쪼ㅎㅎ' , '공주']

for i in x:
    print(i)
