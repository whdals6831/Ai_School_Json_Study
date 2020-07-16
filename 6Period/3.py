def question(n) :
    answer = []

    for i in range(1,n//2+1) :
        if n%i == 0 :
            answer.append(i)
    
    answer.append(n)
    print(answer)


def main() :
    n = int(input('숫자를 입력해 주세요 : '))

    question(n)

main()


# 더 적은 횟수로 돌 수 있는 답

# num = int(input())
# sqrt_num = int(num ** (1/2))

# front_divisor_list = []
# rear_divisor_list = []

# for i in range(1, sqrt_num+1):
#     if num % i == 0:
#         front_divisor_list.append(i)
#         if i != int(num/i):
#             rear_divisor_list.append(int(num/i))

# print(front_divisor_list + rear_divisor_list[::-1])