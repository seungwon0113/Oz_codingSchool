import requests
from bs4 import BeautifulSoup

header_user = {"User_Agent" : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36'}

keyword = input("검색할 키워드를 입력해주세요. : ")
base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="

url = base_url + keyword
req = requests.get(url, headers=header_user)
html = req.text
soup = BeautifulSoup(html,"html.parser")

name = soup.select(".user_info > a") # soup에 들어있는 문자들 중에서 클래스가 name 인걸 찾는다 >> css : . = class, # = id
title = soup.select(".title_link")
advertisement = soup.select(".spblog.ico_ad")

for i in zip(title, name):
    print(f"블로그 제목: {i[0].text}")
    print(f"작성자: {i[1].text}") # 항상 텍스트 내용만 출력
    print(f"작성자 링크 : {i[1]['href']}")
    print()