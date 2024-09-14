import requests
from bs4 import BeautifulSoup

header_user = {"User_Agent" : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36'}

keyword = input("검색할 키워드를 입력해주세요. : ")
base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="

url = base_url + keyword
req = requests.get(url, headers=header_user)
html = req.text
soup = BeautifulSoup(html,"html.parser")

view = soup.select(".view_wrap") # 33 개

for i in view:
    title = i.select_one(".title_link") # select_one
    name = i.select_one(".user_info > a") # soup에 들어있는 문자들 중에서 클래스가 name 인걸 찾는다 >> css : . = class, # = id
    advertisement = i.select_one(".spblog.ico_ad")

    if not advertisement:
        print(f"블로그 제목: {title.text}")
        print(f"작성자: {name.text}") # 항상 텍스트 내용만 출력
        print(f"작성자 링크 : {name['href']}")
        print()