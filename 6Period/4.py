def question(n) :
    max = n[0]
    min = n[0]

    for i in n :
        if i > max :
            max = i
        elif i < min :
            min = i
    
    print(f'{max} {min}')


def main() :
    n = list(map(int, input().split()))

    question(n)

main()