# 파이썬 문자열 다루기 마스터해보자

import json

def read_json() :
    with open('./swit_chat.json', 'r', encoding='utf-8') as jsonfile:
        swit_chat_data = json.load(jsonfile)
        # print(swit_chat_data)
    
    return swit_chat_data


def print_max_chat_people(user_array, count_array) :
    idx = 0
    users = []

    max_num = max(count_array)

    # 가장 많이 채팅친 횟수가 여러명 일 수 있으므로 
    # 배열에 여러명 추가할 수 있도록 함
    for user in user_array :
        if count_array[idx] == max_num :
            users.append(user)
        idx += 1
    
    print('==========================================')
    print(f'이름 : {users} \n채팅친 횟수 : {max_num}번')
    print('==========================================')



def main() :
    swit_chat_data = read_json()

    user_array = []
    count_array = []
    
    for user in swit_chat_data['data'] :
        try:
            idx = user_array.index(user['user_name'])
            count_array[idx] += 1
        except :
            user_array.append(user['user_name'])
            count_array.append(1)
    
    # print(user_array)
    # print(count_array)
    
    print_max_chat_people(user_array, count_array)

main()


# swit_chat_data 에 담긴 데이터는 실제 광주인공지능사관학교 스윗의 데이터이다.
# 문제 :
# 가장 많이 글을 쓴 채팅을 작성한 사람은 누구일까..?

# 힌트 ) 유저 별 content 수를 세서 누가 가장 많이썼을지 알아보기