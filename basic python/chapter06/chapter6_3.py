# 딕셔너리 조작

sale = {'서울': 80, '대전': 60, '대구': 22, '부산': 50, '광주': 75}  # 딕셔너리 지정
print('현재 데이터는', sale, '입니다.')

k = input('추가할 키를 입력핫요.')
if k in sale:
    print(k, '의 데이터는 이미 존재합니다.')
else:
    d = int(input('추가할 데이터를 입력하세요.')) #요소 추가
    sale[k] = d
    print(k, '의 데이터로서', sale, '입니다.')

k = input('어떤 키의 데이터를 변경할까요?')
if k in sale:
    print(k, '의 데이터는', sale[k], '입니다.')
    d = int(input('데이터를 입력하세요.')) # 요소 변경
    sale[k] = d
    print(k, '의 데이터는', sale[k], '로 변경되었습니다..')
else:
    print(k, '의 데이터는 존재하지 앖습니다.')
print('현재 데이터는', sale, '입니다.')

k = input('어떤 키의 데이터를 삭제할까요?')
if k in sale:
    print(k, '의 데이터는', sale[k], '입니다.') #요소 삭제
    del sale[k]
    print('데이터를 삭제했습니다.')
else:
    print(k, '의 데이터는 존재하지 않습니다.')
print('현재 데이터는', sale, '입니다.')
