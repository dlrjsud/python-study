# 기억 수명

a = 0


def func():
    global a #함수 내에서 증가하는 a는 전연 변수로 지정
    b = 0

    print('변수 a는', a, '변수 b는', b)

    a = a + 1
    b = b + 1  #각 변수를 1씩 시킨다.

for i in range(5):
    func()
