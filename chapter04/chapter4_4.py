#for문  for 변수(i) in 반복해서 반복 처리할 수 있는 구조:


for i in range(12):     #변수 i에 0~11까지 대입하면서
    print(i+1,'월 데이터입니다.')      #블록 내의 처리가 반복

for i in range(1,13):   #시작값과 정지값 지정
    print(i,'월의 데이터입니다.')

for i in range(1,13,1):     #간격 지정
    print(i,'월의 데이터입니다.')

for i in range(0,10,2):     #0,2,4,6,8 을 얻음
    print(i, '월의 데이터입니다.')

for i in range(10,0,-2):     #10,8,6,4,2를 얻음
    print(i, '월의 데이터입니다.')