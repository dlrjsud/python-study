a = int(input('a의 가위(1) , 바위 (2), 보(3) 을 입력하세염ㅋㅋ?'))
b = int(input('b의 가위(1) , 바위 (2), 보(3) 을 입력하세염ㅋㅋ?'))

if a == b:
    print('비겼습니다.')
elif a == 1 and b == 3 or a == 2 and b == 1 or a == 3 and b == 2:
    print('a승')
elif b == 1 and a == 3 or b == 2 and a == 1 or b == 3 and a == 2:
    print('b승')
else:
    print('잘못냈습니당ㅋ')
