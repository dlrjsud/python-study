import chapter8_7

pr = chapter8_7.Customer('김영진', 23, 'aaa@aaa.aa.kr', '010-1111-2222')

nm = pr.getName()
ag = pr.getAge()
ad = pr.getAdr()
tl = pr.getTel()

print(nm, '씨는', ag, '세입니다.')
print('메일 주소는', ad, '전화번호는', tl, '입니다.')
