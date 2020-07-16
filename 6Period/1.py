# 나머지와 몫이 같은 수 구하기
# 숫자 n이 주어졌습니다.
# n으로 나누었을 때 나머지와 몫이 같은 모든 자연수의 합이 얼마인지 찾는 문제를 풀어 봅시다.
# 예를 들어서,
# n이 1일 경우, 해당하는 자연수는 없기에 0으로 간주한다.
# n = 2일 경우 3,
# n = 3일 경우 12,
# n = 4일 경우는 30이 정답으로 간주된다.

# 자연수 n이 주어질 때 나머지와 몫이 같은 모든 자연수의 합을 출력하시오.

def question(n) :
    sum = 0
    d = []

    for i in range(1, n**2) :
        mok = i//n
        namerge = i%n

        if mok == namerge :
            sum += i
            d.append(i)
    
    print(f'답 : {sum}    {d}')


def answer(n) :
    sum = 0

    for i in range(1,n) :
        sum += i*(n+1)
    
    print(f'답 : {sum}')


def another_answer(n) :
    sum = (n*(n+1)*(n-1))/2

    print(f'답 : {sum}')


while True :
    # question(int(input()))
    # answer(int(input()))
    another_answer(int(input()))



