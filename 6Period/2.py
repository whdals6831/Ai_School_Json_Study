def question() :
    a, b, R = map(int, input().split())
    N = int(input())

    answer = []

    for i in range(N) :
        x, y = map(int, input().split())
        if (x-a)**2+(y-b)**2 >= R**2 :
            answer.append('silent')
        else :
            answer.append('noise')

    for s in answer :
        print(s)

def main() :
    question()

main()
