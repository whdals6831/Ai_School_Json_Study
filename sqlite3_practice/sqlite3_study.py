import sqlite3
import getpass

def create_database_table() :
    conn = sqlite3.connect('./user_data.db')
    # 자동 커밋 (이렇게 하면 execute할 때마다 커밋이 되어 
    # conn.commit()을 일일이 안해줘도 된다.)
    # conn = sqlite3.connect('./user_data.db', isolation_level=None)
    
    cur = conn.cursor()
    
    # 유저 Table
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id integer primary key autoincrement, 
        userid text unique not null, 
        password text not null,
        name text,
        age integer
        );""")
    
    # 글 Table
    cur.execute("""CREATE TABLE IF NOT EXISTS note(
        userid text unique not null,
        maintext text
        );""")
    
    conn.commit()
    conn.close()



def read_users_table() :
    conn = sqlite3.connect('./user_data.db')
    cur = conn.cursor()

    res = cur.execute('SELECT * FROM users').fetchall()

    conn.commit()
    conn.close()

    # 리스트로 반환
    return res



def read_note_table() :
    conn = sqlite3.connect('./user_data.db')
    cur = conn.cursor()

    res = cur.execute('SELECT * FROM note').fetchall()

    conn.commit()
    conn.close()

    # 리스트로 반환
    return res



def find_user_data(userid) :
    conn = sqlite3.connect('./user_data.db')
    cur = conn.cursor()

    user_sql = f'SELECT * FROM users WHERE userid="{userid}"'
    note_sql = f'SELECT maintext FROM note WHERE userid="{userid}"'

    user_result = cur.execute(user_sql)
    user = user_result.fetchall()[0]

    print('아이디 : ' + user[1])
    print('비밀번호 : ' + user[2])
    print('이름 : ' + user[3])
    print('나이 : ' + str(user[4]))

    note_result = cur.execute(note_sql)
    note = note_result.fetchall()[0]

    print('작성한 글 : ' + note[0])

    conn.close()



def write_user_table(user) :
    conn = sqlite3.connect('./user_data.db')
    cur = conn.cursor()

    sql = "INSERT INTO users (userid, password, name, age) VALUES (?,?,?,?);"

    cur.execute(sql, user)

    conn.commit()
    conn.close()



def write_note_table(note) :
    conn = sqlite3.connect('./user_data.db')
    cur = conn.cursor()

    sql = "INSERT INTO note VALUES (?,?);"

    cur.execute(sql, note)

    conn.commit()
    conn.close()


def user_input_check(input_type) :
    while True :
        input_data = ''

        if input_type == '아이디' :
            input_data = input("아이디를 입력하세요 : ").strip()
        elif input_type == '비밀번호' :
            input_data = getpass.getpass("비밀번호를 입력하세요 : ").strip()

        if input_data == '' :
            print(f'{input_type}를 입력하지 않았습니다. 다시 입력해주세요\n메뉴로 돌아가고 싶으시면 exit를 입력해 주세요\n') 
            continue
        elif len(input_data) > 12 :
            print(f'{input_type}는 12자 이하로 기입해주세요. 다시 입력해주세요\n메뉴로 돌아가고 싶으시면 exit를 입력해 주세요\n')
        elif input_data == 'exit' :
            return 'exit'
        else :
            return input_data
    

def register() :
    user = []
    note = []

    userid = user_input_check('아이디')

    if userid == 'exit' :
        return

    password = user_input_check('비밀번호')

    if password == 'exit' :
        return

    name = input("이름을 입력하세요 : ")
    age = input("나이를 입력하세요 : ")
    write = input("적고 싶은 글이 있으시면 적어주세요 : ")

    user.append(userid)
    user.append(password)
    user.append(name)
    user.append(age)

    note.append(userid)
    note.append(write)

    write_user_table(user)
    write_note_table(note)



def print_users_note() :
    conn = sqlite3.connect('./user_data.db')
    cur = conn.cursor()

    result_user = cur.execute('SELECT * FROM users').fetchall()
    result_note = cur.execute('SELECT * FROM note').fetchall()

    print('\n======= 유저 목록 ========')
    for user in result_user:
        print(user)
    
    print('\n====== 글 목록 =======')
    for note in result_note:
        print(note)

    conn.close()



def login() :
    while True :
        userid = input("아이디를 입력하세요 : ")
        password = getpass.getpass("비밀번호를 입력하세요 : ")

        users = read_users_table()

        for user in users :
            if(user[1] == userid and user[2] == password) :
                print("로그인에 성공하셨습니다.")
                my_page(userid)
                return

        print("로그인에 실패하였습니다. 다시 입력해주세요.")    


def my_page(userid) :
    print("\n---------- 마이 페이지 ----------")
    print("1. 나의 정보 가져오기")
    print("2. 나가기\n")

    select_menu_num = int(input("선택할 메뉴 : "))

    if select_menu_num == 1 :
        find_user_data(userid)
    elif select_menu_num == 2 :
        exit()
    else :
        print("잘못된 번호를 입력하셨습니다.")



def main() :
    # 시작할 때 데이터베이스에 테이블 생성
    create_database_table()

    # cur를 함수의 인자로 넣어주면 계속해서 불러올 필요없이
    # 바로바로 execute하면 되서 코드를 더욱 간결하게 만들 수 있다.

    while True :
        print("\n---------- 메뉴 화면 ----------")
        print("1. 회원가입")
        print("2. 로그인")
        print("3. 모든 사람 정보 보기")
        print("4. 나가기\n")
        
        select_menu_num = int(input("선택할 메뉴 : "))

        if select_menu_num == 1 :
            register()
        elif select_menu_num == 2 :
            login()
        elif select_menu_num == 3 :
            print_users_note() 
        elif select_menu_num == 4 :
            exit()
        else :
            print("잘못된 번호를 입력하셨습니다.")

main()