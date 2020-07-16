# python csv 모듈 공식 문서 참고
# pandas 등 사용하지 않고 풀어주시기 바랍니다.
# 한글 데이터를 다룰 경우 인코딩 문제가 생길 수 있습니다 -> 구글링으로 해결해주세요 (ex) 검색 : python 한글 인코딩 문제)
 
# 상점 데이터를 추가하고 원하는 column을 선택하여 읽을 수 있는 프로그램을 만드시오.
 
# 상점의 데이터 -> (이름, 위치, 판매하는 상품, 전화번호)
 
# 상점 데이터 예시
# baeks_stores = [
#     {
#         “name” : “빽다방 광주 상무역점”,
#         “location” : “광주 서구 치평로 20”,
#         “goods” : “커피”,
#         “num” : “0507-1430-3335”
#     },
#     {
#         “name” : “새마을 식당 광주 금호점” ,
#         “location” : “광주 서구 운천로17번길 4”,
#         “goods” : “고기”,
#         “num” : “062-381-7661”
#     },
#     {
#         “name” : “빽다방 종로관철점” ,
#         “location” : “서울 종로구 종로10길 21,
#         “goods” : “커피”,
#         “num” : “00-2445-5324”
#     },
#     {
#         “name” : “백인공지능 판매점” ,
#         “location” : “광주 북구 첨단과기로”,
#         “goods” : “인공지능”,
#         “num” : “1234-5678-9123”
#     }
# ]
 
# 필요한 기능
# 1. 상점의 데이터를 csv 파일에 등록하는 기능
# 2. 상점들의 이름을 모두 출력하는 기능
# 3. 상점의 이름을 입력 받으면, 해당 상점의 위치를 출력하는 기능
# 4. 상점의 이름을 입력 받으면, 해당 상점의 판매하는 상품을 출력하는 기능
# 5. 상점의 이름을 입력 받으면, 해당 상점의 전화번호를 출력하는 기능
import csv

def read_csv_file() :
    with open('./shop_data.csv', 'r', encoding='utf-8', newline='') as csv_file :
        shop_list = list(csv.reader(csv_file))
    
    return shop_list
        

def write_csv_file(shop) :
    with open('./shop_data.csv', 'a', encoding='utf-8', newline='') as csv_file :
        fieldname = ["name","location","goods","num"]
        wr = csv.DictWriter(csv_file, fieldnames=fieldname)
        wr.writeheader()
        wr.writerow(shop)



def register_shop() :
  shop = {
      'name' : '',
      'location' : '',
      'goods' : '',
      'num' : ''
  }

  shop['name'] = input('상점 이름을 입력해 주세요 : ')
  shop['location'] = input('상점 위치를 입력해 주세요 : ')
  shop['goods'] = input('판매하는 상품을 적어주세요 : ')
  shop['num'] = input('전화번호를 입력해주세요 : ')

  write_csv_file(shop)
  print('성공적으로 등록되었습니다.')


def print_shop() :
    shop_list = read_csv_file()

    for shop in shop_list :
        print(shop[0])


def find_shop(shop_name) :
    shop_list = read_csv_file()

    for shop in shop_list :
        if shop[0] == shop_name :
            print(f'{shop_name}의 위치는 {shop[1]}입니다.')
            return
        
    print('입력하신 이름의 상점이 없습니다.')


def find_goods(shop_name) :
    shop_list = read_csv_file()

    for shop in shop_list :
        if shop[0] == shop_name :
            print(f'{shop_name}은 {shop[2]}를 판매합니다.')
            return
        
    print('입력하신 이름의 상점이 없습니다.')

def find_phone_num(shop_name) :
    shop_list = read_csv_file()

    for shop in shop_list :
        if shop[0] == shop_name :
            print(f'{shop_name}의 전화번호는 {shop[3]} 입니다.')
            return
        
    print('입력하신 이름의 상점이 없습니다.')



# 실행 예시
# 1. 출력 : “성공적으로 등록되었습니다 “ / 결과 : csv 파일에 등록한 이름 잘 들어갈것
# 2. 출력 : “빽다방 광주 상무역점, 새마을 식당 광주 금호점, 빽다방 종로관철점, 백인공지능 판매점”
# 3. 출력: “빽다방 광주 상무역점의 위치는 광주 서구 치평로 20 입니다. / 없을 경우 : "입력하신 이름의 상점이 없습니다."
# 4. 출력 : “빽다방 광주 상무역점은 커피를 판매합니다.” / 없을 경우 : "입력하신 이름의 상점이 없습니다."
# 5. 출력 : “빽다방 광주 상무역점의 전화번호는 0507-1430-3335 입니다.” / 없을 경우 : "입력하신 이름의 상점이 없습니다."

def main() :
    while True :
        selected = input('1 - 상점추가, 2 - 상점 모두 보기, 3 - 상점 위치 찾기, 4 - 판매하는 상품 종 류 보기, 5 - 상점 전화번호 찾기, 0 - 프로그램 종료')
        
        if selected == '1' :
            register_shop()
        elif selected == '2' :
            print_shop()
        elif selected == '3' :
            find_shop(input('찾으시는 상점 이름을 기입해 주세요 : '))
        elif selected == '4' :
            find_goods(input('찾으시는 상점 이름을 기입해 주세요 : '))
        elif selected == '5' :
            find_phone_num(input('찾으시는 상점 이름을 기입해 주세요 : '))
        elif selected == '0' :
            exit()
        else : 
            print('번호를 다시 입력해주세요')

# 메인 함수 실행
main()