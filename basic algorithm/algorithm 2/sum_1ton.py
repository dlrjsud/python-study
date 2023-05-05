# 1부터 n까지 정수의 합 구하기

def sum_1ton(n):
    """1부터 n까지 정수의 합"""
    s=0
    while n > 0:
        s += n
        n -= 1
    return s

x = int(input('x의 값을 입력하세요 :'))
print(f'1부터 {x}까지의 정수의 합은 {sum_1ton(x)}입니다.')

#sum_1ton 함수의 실행 과정에서 매개변수 n 값은 5 4 3 ... 1 으로 1씩 감소 함수 종료 될때 n 값은 0