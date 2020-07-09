import json


json_data_file_path = './aischool.json'


def read_json() : 
    with open(json_data_file_path, 'r', encoding='UTF-8') as json_data:
        user_data = json.load(json_data)
    return user_data


def write_json(user_data) :
    with open(json_data_file_path, 'w', encoding='UTF-8') as json_data:
        json.dump(user_data, json_data, ensure_ascii=False, indent=4)
        # 한글 저장시 ensure_ascii=False 인자를 추가 
        # 안하면 Unicode로 저장됨


def print_student(user_data) :
    user_number = 1

    for student in user_data['students'] :
        print(f'{user_number} - {student["name"]}')
        user_number += 1


def userid_input_check() :
    #     - 조건문으로 아이디를 안넣으면 쓰기 안되게 막아보기
    while True :
        userid = input("아이디를 입력해주세요 : ").strip()

        if userid == '' :
            print("아이디를 입력하지 않았습니다. 다시 입력해주세요\n메뉴로 돌아가고 싶으시면 exit를 입력해 주세요\n") 
            continue
        elif userid == 'exit' :
            return 'exit'
        else :
            return userid


def register_student() :
    student = {
        "userid": "",
        "password": "",
        "name":"",
        "age": "",
        "job": ""
    }
    
    student['userid'] = userid_input_check()

    if(student['userid'] == 'exit') :
        return
    
    student['password'] = input("비밀번호를 입력하세요 : ")
    student['name'] = input("이름을 입력하세요 : ")
    student['age'] = input("나이를 입력하세요 : ")
    student['job'] = input("직업을 입력하세요 : ")

    students = read_json()
    students['students'].append(student)

    if int(student['age']) < 20 :
        write_json(students)
        print('# 정상적으로 등록이 되었습니다. #')
    else :
        print('20살 이상이셔서 등록이 안됩니다.')


def print_youth(user_data) :
    user_number = 1

    for student in user_data['students'] :
        if int(student['age']) < 20 :
            print(f'{user_number} - {student["name"]}')
            user_number += 1


def average_students_age(user_data) :
    sum = 0

    for student in user_data['students'] :
        sum += int(student['age'])
    
    print(f'모든 학생들의 나이 평균 : {round(sum/len(user_data["students"]), 2)}')


def print_teacher(user_data) :
    user_number = 1

    for teacher in user_data['teachers'] :
        print(f'{user_number} - {teacher["name"]} [{teacher["job"]}]')
        user_number += 1



def main() :
    while True : 
        user_data = read_json()

        print('\n===============메뉴================')
        print('1. 학생 이름 전부 출력하기')
        print('2. 학생 등록하기 (20세 미만 가능)')
        print('3. 학생 출력하기 (20세 미만)')
        print('4. 모든 학생들의 평균 나이')
        print('5. 선생님들 이름 전부 출력하기')
        print('6. 나가기\n')

        menu_select_num = input('선택할 메뉴 : ')
        print('')

        if menu_select_num == '1' :
            #     - 학생 이름 전부 출력해보기
            print_student(user_data)

        elif menu_select_num == '2' :
            #     - 20살 미만 학생 open의 쓰기모드를 활용하여 넣어보기
            register_student()

        elif menu_select_num == '3' :
            #     - 성인이 아닌 학생 출력하기 (20세 미만..)
            print_youth(user_data)

        elif menu_select_num == '4' :
            # 학생들의 나이 평균
            average_students_age(user_data)

        elif menu_select_num == '5' :
            # 선생님들 이름 전부 출력해보기
            print_teacher(user_data)

        elif menu_select_num == '6' :
            exit()

        else :
            print('잘못된 선택입니다. 다시 골라주세요')

        #     - 모든 로직은 open 을 최대한 활용하기 !

main()
