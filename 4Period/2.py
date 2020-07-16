import re


list_a = ['ab','a1b','a12b','accb','a123b']

p = re.compile('a..b')

def subdef(match) :
    matched_text = match.group()
    return matched_text +'good'

for i in list_a :
    print(p.sub(subdef,i))







a = ['코끼리는 코끼리', '기린은 기린', '고양이는 고양이']
p = re.compile(r'(?P<name>.+)[은는]\s\1')  
# [^은]이면 은이 들어가면 안됨  ^ = not
# 대괄호 밖의 ^은 시작하는 문자열이 일치하는지를 확인
# 대괄호 밖의 $은 끝 문자열이 일치하는지 확인

for i in a :
    print(p.match(i))







a = '<안녕하세요><반갑습니다>'

p = re.compile('<.+?>')  # ?는 찾다가 처음으로 일치하는것이 있으면 멈춤

print(p.match(a))