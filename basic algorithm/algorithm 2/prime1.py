# 1,000 이하의 소수를 나열하기

counter = 0  # 나눗셈 횟수를 카운트

for n in range(2, 1001):
    for i in range(2, n):
        counter += 1
        if n % i == 0:  # 나누어 떨어지면 소수가 아님
            break  # 반복은 더이상 불필요하여 중단
    else:  # 끝까지 나누어 떨어지지 않으면 다음 수행
        print(n)
print(f'나눗셈을 실행한 횟수: {counter}')

print('----------------------------')

# 1000이하의 소수 나열하기 2

counter = 0               # 나눗셈 횟수 카운트
ptr = 0                   # 이미 찾은 소수 개수
prime = [None] * 500      # 소수를 저장하는 배열

prime[ptr] = 2            # 2는 소수이므로 초깃값 지정
ptr += 1

for n in range(3, 1001, 2):  # 홀수만을 대상으로 설정
    for i in range(1, ptr):  # 이미 찾은 소수로 나눔
        counter += 1
        if n % prime[i] == 0: # 나누어 떨어지면 소수 아님
            break
    else:                    # 끝까지 나누어 떨어지지 않았다면
        prime[ptr] = n       # 소수로 배열에 등록
        ptr += 1

for i in range(ptr):          #ptr의 소수를 출력
    print(prime[i])
print(f'나눗셈을 실행한 횟수 : {counter}')


print('-'*28)
# 1000이하의 소수 나열하기 3

counter = 0               # 나눗셈 횟수 카운트
ptr = 0                   # 이미 찾은 소수 개수
prime = [None] * 500      # 소수를 저장하는 배열

prime[ptr] = 2            # 2는 소수
ptr += 1

prime[ptr] = 3            # 3은 소수
ptr += 1

for n in range(5, 1001, 2): # 홀수만 대상으로 실행
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:  # 나누어 떨어지는 소수 아님
            break
        i += 1
    else:                     # 끝까지 나우어 떨어지지 않았다면
        prime[ptr] = n        # 소수로 배열에 등록
        ptr += 1
        counter += 1

for i in range(ptr):       #ptr의 소수를 출력
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')

