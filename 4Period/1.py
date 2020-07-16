import re



list_a = ['ab', 'alb','a12b','a123b', '123  ab']
p = re.compile('A.*B', re.I)  # 옵션 I(IGNORECASE)는 대소문자 무시
# . 은 공백 포함 모든 문자를 뜻함

# +(앞에 있던 문자가 최소한 1부터 반복) *(최소한 0부터 반복) 를 활용해서
# a와 b사이에 어떤 문자가 몇개 있던 간에 매치시키도록 함

# *나 + 대신 {2,5} 이렇게 중괄호를 넣어 
# 2~5 범위를 지정해서 매치시키도록 할 수 있음

for i in list_a:   # 문자열 처음부터 매치
    print(p.match(i))

for i in list_a:   # 문자열 전체 매치
    print(p.search(i))

# for i in list_a :
#     print(p.match(i).group())


a = '정종민 - 학점 3.5'
p2 = re.compile(r'(?P<name>\w+)\s.\s(?P<greade>\w+)')

print(p2.match(a))
