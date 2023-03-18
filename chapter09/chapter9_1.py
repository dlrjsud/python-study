# 문자열

str = input('문자열을 입력하세요.')

print('문자열은', str, '입니다.')
print('0번째 문자열은', str[0], '입니다.')
print('문자열을 역순으로 하면', str[::-1], '입니다.')
print('문자열의 길이는', len(str), '입니다.')
print('대문자로 하면', str.upper(), '입니다.')
print('소문자로 하면', str.lower(), '입니다.')

# 문자열 포맷

word0 = input('첫 번째 단어를 입력하세요.')
word1 = input('두 번째 단어를 입력하세요.')
word2 = input('세 번째 단어를 입력하세요.')
print('{0}은 {1}{2}입니다.'.format(word0, word1, word2))

num0 = int(input('개수를 입력하세요'))
num1 = int(input('금액를 입력하세요'))

print('{0:<}개{1:>10,}원'.format(num0, num1))

# 문자열 검색

str = input('문자열을 입력하세요.')
key = input('검색할 문자열을 입력하세요.')
res = str.find(key)
if res != -1:
    print(str, '의 ', res, '위치에서', key, '를 찾았습니다.')
else:
    print(str, '의 안에서 ', key, '를 찾을 수 없었습니다.')

#문자열 치환

str1=input('문자열을 입력하세요.')
old=input('치환될 문자열을 입력하세요.')
new=input('치환할 문자열을 입력하세요.')

if old in str1:
    str2=str1.replace(old,new)
    print(str2,'로 치환했습니다.')
else:
    print(str1+'의 안에서'+old+'를 발견했습니다.')
