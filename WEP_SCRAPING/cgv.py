import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"
req = requests.get(url, headers=header_user)
html = req.text
soup = BeautifulSoup(html, "html.parser")

view = soup.select(".sect-movie-chart ol > li")
for i in view:
    ranking = i.select_one(".rank")
    title = i.select_one(".title")
    rate = i.select_one(".percent")
    info = i.select_one(".txt-info")
    dday = i.select_one(".dday") # d-day

    if not dday and ranking and title and rate and info: # dday 제외와 text
        ranking_text = ranking.text.strip()
        title_text = title.text.strip()
        rate_text = rate.text.strip()
        info_text = info.text.strip().replace("개봉", "").replace("재","").strip() 
        # replace() : <span>개봉</span>, <span>재개봉</span> 지우기
        
        print(f"순위 : {ranking_text}")
        print(f"제목 : {title_text}")
        print(f"예매률 : {rate_text}")
        print(f"개봉일자 : {info_text}")
        print()