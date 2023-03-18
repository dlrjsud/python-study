# 정규표현

import re  # 정규 표현의 re 모듈을 임포트

ptr = ['Apple', 'GoodBye', 'Thankyou']  # 패턴 문자열
str = ['Hello', 'GoodBye', 'Thankyou']  # 검색 대산 문자열

for valueptr in ptr:
    print('------')
    pattern = re.compile(valueptr)  # 패턴 문자열 컴파일
    for valuestr in str:
        res = pattern.search(valuestr)  # 검색 (패턴 매치)
        if res is not None:
            m = 'ㅇ'
        else:
            m = 'x'
        msg = '(패턴)' + valueptr + '(문자열)' + valuestr + '(매치)' + m
        print(msg)

# 행의 앞 끝을 나타내는 정규 표헌

import re

ptr = ['TXT', '^TXT', 'TXT$', '^TXT$']
str = ['TXT', 'TXTT', 'TXTTT', 'TTXT']  # ^ 와 $를 사용한 패턴

for valueptr in ptr:
    print('------')
    pattern = re.compile(valueptr)
    for valuestr in str:
        res = pattern.search(valuestr)
        if res is not None:
            m = 'ㅇ'
        else:
            m = 'x'
        msg = '(패턴)' + valueptr + '(문자열)' + valuestr + '(매치)' + m
        print(msg)

# 문자를 나타내는 정규표현

import re

ptr = ['TXT.', 'TXT..', '.TXT', '..TXT']
str = ['TXT', 'TXTT', 'TXTTT', 'TTXT']  # .을 사용한 패턴을 만듬

for valueptr in ptr:
    print('------')
    pattern = re.compile(valueptr)
    for valuestr in str:
        res = pattern.search(valuestr)
        if res is not None:
            m = 'ㅇ'
        else:
            m = 'x'
        msg = '(패턴)' + valueptr + '(문자열)' + valuestr + '(매치)' + m
        print(msg)

# 문자 클래스를 나타내는 표현
import re

ptr = ['[012]', '[0-3]', '[^012]']
str = ['0', '1', '2', '3']  # []와 ^를 사용한 패턴

for valueptr in ptr:
    print('------')
    pattern = re.compile(valueptr)
    for valuestr in str:
        res = pattern.search(valuestr)
        if res is not None:
            m = 'ㅇ'
        else:
            m = 'x'
        msg = '(패턴)' + valueptr + '(문자열)' + valuestr + '(매치)' + m
        print(msg)

# 반복기호
import re

ptr = ['T*', 'T+', 'T?', 'T{3}']
str = ['X', 'TT', 'TTT', 'TTTT']  # 반복 기호를 사용한 패턴

for valueptr in ptr:
    print('------')
    pattern = re.compile(valueptr)
    for valuestr in str:
        res = pattern.search(valuestr)
        if res is not None:
            m = 'ㅇ'
        else:
            m = 'x'
        msg = '(패턴)' + valueptr + '(문자열)' + valuestr + '(매치)' + m
        print(msg)

# 그룹화

import re

ptr = ['(TXT)+', 'TXT|XTX']
str = ['TX', 'TXT', 'XTX', 'TXTXT']  # 그룹화를 사용하는 패턴

for valueptr in ptr:
    print('------')
    pattern = re.compile(valueptr)
    for valuestr in str:
        res = pattern.search(valuestr)
        if res is not None:
            m = 'ㅇ'
        else:
            m = 'x'
        msg = '(패턴)' + valueptr + '(문자열)' + valuestr + '(매치)' + m
        print(msg)

# 정규 표현 치환
import re

ptr = '\.(csv|html|py)$'
str = ['Sample.csv', 'Sample.exe', 'test.py', 'index.html']
pattern = re.compile(ptr)
for valuestr in str:
    res = pattern.sub('.txt', valuestr)
    msg = '(변환전)' + valuestr + '(변환후)' + res
    print(msg)
