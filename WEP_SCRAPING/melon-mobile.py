from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

options_ = Options()
options_.add_argument(f"user-agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])


#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)

url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(0.5)

# 멜론 홈아이콘 클릭
driver.find_element(By.CSS_SELECTOR, ".link-logo").click()
time.sleep(2)

# 멜론 차트 클릭
driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(2)

from selenium.webdriver.support.ui import WebDriverWait # 웹페이지 로딩 대기
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# WebDriverWait를 이용하여 페이지 로딩 대기후 추출한 XPATH를 이용하여 더보기 버튼 클릭
more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='moreBtn' and @onclick='hasMore2();']")))
more_button.click()
time.sleep(2)

# 페이지 소스 가져오기
html = driver.page_source

# BeautifulSoup으로 파싱
soup = BeautifulSoup(html, "html.parser")

view = soup.select(".list_item")

# 순위, 노래 제목, 가수 이름을 가져오기 위한 태그들
def scann():
    for i in view:
        ranks = i.select_one('.ranking_num')  # 순위
        title = i.select_one('.title.ellipsis')
        artists = i.select_one('.name.ellipsis')  # 가수 이름
        chart = i.select_one('.line_clamp2') 
        # 신규 차트 클래스를 계속 인식하길래 꿀에서 했던 광고 클래스 제외를 이용

        if not chart:
            rank_text = ranks.text.strip() if ranks else "N/A"
            title_text = title.text.strip() if title else "N/A"
            artist_text = artists.text.strip() if artists else "N/A"

            print(f"순위 : {rank_text}")
            print(f"제목 : {title_text}")
            print(f"가수 : {artist_text}")
            print()
scann()
#driver.quit()


# 출력하기

#driver.quit()
#아래 순서대로 스크래핑한 자료를 출력해주세요
#순위 :
#노래 제목 :
#가수 이름 :

