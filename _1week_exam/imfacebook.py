
import sqlite3

def namecheck():
    #여기서 사용자 이름을 받아주세요
    return input("당신의 이름을 적어주세요 : ")

def readcheck():
    #여기서 글을 쓰려면 0, 읽으려면 1이라는 인풋값을 받아주세요
    return int(input("글을 쓰려면 0, 글을 읽으려면 1을 입력해주세요 : "))

def user_input():
    #사용자가 글을 쓴다고 말한다면 인풋으로 제목과 내용을 받아주세요
    title = input('제목 : ')
    content = input('내용 : ')

    return title, content

def user_search():
    #사용자가 글을 읽는다고 말한다면 인풋으로 검색할 제목을 받아주세요
    return input('검색할 제목을 입력해주세요 : ')

def write(title, content, username, cursor):
    #user_input으로 부터 받은 내용과 namecheck으로부터 받은 내용을 함께 쿼리문으로 db에 insert해주세요

    sql = "INSERT INTO feed VALUES (?,?,?);"

    x = []
    x.append(title)
    x.append(content)
    x.append(username)

    cursor.execute(sql, x)

def read(title, cursor):
    #user_search로 받은 내용을 통해 해당 내용을 제목에 포함하는 글이 있으면 제목, 내용, 작성자를 모두 표시해주세요
    user_list = cursor.execute('''
    SELECT *
    FROM feed
    ''').fetchall()

    for user in user_list :
        if user[0] == title :
            print(f'제목 : {user[0]}') 
            print(f'내용 : {user[1]}') 
            print(f'작성자 : {user[2]}') 
            return
    
    print('찾으시는 사용자가 없습니다.')
            

def start():
    print("\n나만의 페이스북!")

    username = namecheck()
    read_check = readcheck()

    #db에 연결하고 커서 객체를 만들어주세요
    con = sqlite3.connect('./imzuckerberg.db')
    cur = con.cursor()

    #여기에서 table을 만들어주세요

    cur.execute("""CREATE TABLE IF NOT EXISTS feed(
        title text, 
        content text,
        name text
        );""")

    if read_check == 0:
        #user_input 함수로 인풋을 받고, write 함수를 이용해 쿼리를 수행해주세요.
        #쿼리를 수행하신 뒤에는 db에 커밋을 해주세요.
        title, content = user_input()
        write(title, content, username, cur)
        con.commit()
    elif read_check == 1:
        #user_search 함수로 인풋을 받고, read 함수를 이용해 쿼리를 수행해주세요.
        title = user_search()
        read(title, cur)
    else:
        print("올바른 숫자를 입력하세요!")
        start()

    #db와의 연결을 닫아주세요.
    con.close()

start()