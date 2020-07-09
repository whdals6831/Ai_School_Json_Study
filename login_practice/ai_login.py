import json
from getpass import getpass


def load():
    with open('./users.json', 'r') as f:
        data = json.load(f)
    return data


def save(data):
    with open('./users.json', 'w') as f:
        json.dump(data, f)


def signup(data):
    user = {
        'id': '',
        'password': '',
        'name': '',
        'message': '',
        'hobby': ''
    }
    # 디스플레이용 이름
    dpnames = {
        'id': '아이디',
        'password': '비밀번호',
        'name': '이름',
        'message': '앞으로 5개월 동안의 다짐',
        'hobby': '관심분야'
    }

    print("=========📝 회원 가입 폼 작성===========")
    for value in user.keys():
        user[value] = input(f"{dpnames[value]} 을/를 입력하세요 ===>  ")
    data['users'].append(user)
    save(data)
    print("회원가입이 완료되었습니다.")
    print("========================================")


def get_logged_in_menu(user):
    print("========================================")
    while True:
        print(f"{user['name']}님, 메뉴를 선택하세요.")
        loggedin_menu = input(
            "1.마이페이지 보기 , 2.다른 유저 보기, 3.이전  ===>  ")

        if loggedin_menu == '1':
            print("마이페이지 ==> ")
            print(user)

        elif loggedin_menu == '2':
            print("다른 유저 보기 ==> ")
            for idx, u in enumerate(data['users']):
                if u['id'] != user['id']:
                    print("-------")
                    print("번호 : ", idx)
                    print("이름 : ", u['name'])
                    print("-------")

            while True:
                print("========================================")
                number = int(
                    input("찾아볼 유저의 번호를 입력하세요, -1을 누르면 이전으로 갑니다. ===> "))
                if number == -1:
                    break
                elif number >= 1 and number < len(data['users']):
                    print(data['users'][number])
                else:
                    print("잘못된 유저 번호")
                print("========================================")
        elif loggedin_menu == '3':
            return
        else:
            print("올바른 번호를 선택해주세요")
            continue
        print("========================================")


def login(data):
    users = data['users']

    while True:
        login_info = {
            'id': '',
            'password': ''
        }

        print("==============📝 로그인================")
        login_info['id'] = input("아이디를 입력하세요 ===>  ").lower()
        login_info['password'] = getpass("비밀번호를 입력하세요 ===>  ").lower()

        if(len(login_info['id']) <= 12 and len(login_info['password']) <= 12) :
            isLoggedIn = False
            for user in users:
                # 로그인 성공 케이스
                if user['id'] == login_info['id'] and user['password'] == login_info['password']:
                    print("로그인 성공")
                    isLoggedIn = True
                    get_logged_in_menu(user)
                    return

            if not isLoggedIn:
                print("로그인 실패")
                menu = input("1. 다시 로그인, 2. 회원가입")
                if menu == '1':
                    continue
                elif menu == '2':
                    signup(data)
                    return
        else :
            print('다시 로그인해주세요')
            return

        


while True:
    data = load()
    print("========================================")
    print("--인공지능 사관학교 로그인 실습--")
    print("메뉴를 선택하세요.")
    menu = input("1. 회원가입 , 2. 로그인, 3. 종료  ===>  ")
    print("========================================")
    # 회원가입
    if menu == '1':
        signup(data)
    # 로그인
    elif menu == '2':
        login(data)
    # 그 외 입력시
    elif menu == '3':
        print("종료합니다.")
        break
    else:
        print("올바른 입력이 아닙니다.")
        # 돌아가
        continue
