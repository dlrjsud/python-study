# 텍스트 파일에 써 넣는다

f = open('Sample.txt', 'w')  # 지정된 파일을 오픈

f.write('안녕하세요\n')
f.write('안녕히 계세요\n')  # 파일에 써 넣기

f.close()  # 파일을 닫는다

# 텍스트 파일을 읽기

f = open('Sample.txt', 'r')  # 파일을 읽기모드로 오픈

lines = f.readlines()  # 전체 행 읽기

for line in lines:  # 1행씩 반복해 꺼냄
    print(line, end='')  # 표시함
f.close()
