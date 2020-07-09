# TODO_0 : csv 모듈 불러오기
import csv


def read_csv_file() :
    users_data = []

    with open('./users.csv', 'r', encoding='utf-8') as csvfile :
        users_data = list(csv.reader(csvfile))
    
    return users_data


def write_csv_file(user_data) :
    with open('./users.csv', 'a', encoding='utf-8', newline='') as csvfile :

        if type(user_data) == list :
            wr = csv.writer(csvfile)
            wr.writerow(user_data)

        elif type(user_data) == dict :
            wr = csv.DictWriter(csvfile, fieldnames=['id','pw'])
            wr.writerow(user_data)
        
        else :
            print('잘못된 데이터 형식입니다.')
            return
    
    
def user_input():
    try:
        id, pw = map(str, input("아이디와 비밀번호를 차례로 입력해주세요 : ").split())
        return id, pw
    except:
        print("올바르지 않은 입력입니다!")
        id, pw = user_input()
        return id, pw

# TODO_1 : signin 함수를 구현해서 로그인 시키기
# 1. csv 파일에서 존재하는 아이디인지 확인하기
# 2. 존재하면 비밀번호 맞는지 체크
# 3. 비밀번호도 맞으면 로그인성공 출력하기

def signin(id, pw) :
    users = read_csv_file()

    for user in users :
        if user[0] == id and user[1] == pw :
            print('로그인 성공')
            return 

        elif user[0] == id and user[1] != pw :
            print('비밀번호가 맞지 않습니다')
            return
        
        else :
            print('아이디가 존재하지 않습니다')
            return

# TODO_2 : csvfile 에 유저가 존재하는지 확인하는 함수 구현해서 호출하기
# 1. 아이디를 기준으로 존재하는 유저인지 확인
# 2. 존재한다면 다시 아이디를 입력받고,
# 3. 존재하지 않는다면 다음 단계로 넘겨주기

def check_id(id) :
    users = read_csv_file()

    for user in users :
        if user[0] == id :
            print('이미 존재하는 아이디입니다.')
            return '0'

    return id


# TODO_3 : csvfile 에 등록되어있는 형태로 유저 등록하는 함수 구현하기
# 1. 아이디와 비밀번호를 그냥 데이터로 받아서 추가해보기
# 2. 아이디와 비밀번호를 '딕셔너리' 형태로 받아서 추가해보기 (프로그래밍 실력의 기본은 구글링! 최대한 구글링 해보세요!!)

def signup(id, pw) :
    id = check_id(id)

    if(id == '0') :
        return

    user = []

    user.append(id)
    user.append(pw)

    write_csv_file(user)

# def signup(dict_user) :
#     id = check_id(dict_user['id'])

#     if(id == '0') :
#         return

#     write_csv_file(dict_user)


# TODO_4 : csvfile 에서 현재 가입되어 있는 유저 전부 출력하기
def userlist():
    print("현재 존재하는 유저 :")
    users = read_csv_file()

    for user in users :
        print(f'[ 아이디 : {user[0]} ]')



def exitcheck():
    stop = int(input("\n계속하시려면 0, 종료하시려면 1을 눌러주세요. : "))
    if stop == 0:
        start()
    elif stop == 1:
        exit()



def start():
    print('csv 로 데이터 다루기 로그인 예제')

    signup_or_login = int(input('1 - 로그인 / 2 - 회원가입 : \n'))

    if signup_or_login == 1:
        id, pw = user_input()
        # TODO_5 : 위의 TODO1 참고 후 signin 함수 실행하기
        
        signin(id, pw)
        
    elif signup_or_login == 2:
      # TODO_6 : 회원가입을 아이디와 비밀번호만 받아서 진행할 것
      # 1. 존재하는지 확인 (위의 TODO_2의 함수 활용)
      # 2. 문제 없으면 회원가입 완료 후 userlist() 함수 구현

        dict_user = {
            "id": '',
            "pw": ''
        }

        id, pw = user_input()

        dict_user['id'] = id
        dict_user['pw'] = pw

        signup(id, pw)
        # signup(dict_user)

        userlist()
    else:
        print("올바른 숫자를 입력하세요!")

    exitcheck()


start()

# TODO_7 : 깃헙에 업로드하고 깃헙 주소 제출!
