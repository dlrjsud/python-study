# 키보드로 입력    변수 = input('화면에 표시할 메시지')
n = input('값을 입력하세요.')
print(n, '이(가) 입력되었습니다.')

# 수치 입력
num1 = input('수치1을 입력하세요.')
num2 = input('수치2를 입력하세요.')  # 1.문자열로 입력되므로
num3 = num1 + num2  # 2.계산을 해도
print(num1, '+', num2, '은(는)', num3, '입니다.')  # 3.입력 문자를 연결한 값이 출력

#수치를 제대로 계산
num1 = int(input('정수1을 입력하세요.'))
num2 = int(input('정수2을 입력하세요.'))
num3 = num1 + num2
print(num1,'+',num2,'은(는)',num3,'입니다.')
