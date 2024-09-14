from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pymysql

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='seungwon0113',
    db='kream',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

options = Options()
options.add_argument(f"User-Agent={user}")
options.add_experimental_option("detach", True)  # 브라우저 유지
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

url = "https://kream.co.kr/"
driver.get(url)

time.sleep(1)

# 돋보기 아이콘 클릭
driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()
time.sleep(0.7)

# 검색창에 '슈프림' 입력
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
time.sleep(0.7)

# 엔터키 동작
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(1)

# 페이지 스크롤
for i in range(20):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

# HTML 페이지 소스 가져오기
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".item_inner")

# 데이터베이스 삽입
try:
    with conn.cursor() as cur:
        for item in items:
            product_name = item.select_one(".translated_name").text
            if "후드" in product_name:
                product_brand = item.select_one(".product_info_brand.brand").text
                product_price = item.select_one(".amount").text.replace(",", "").strip()

                # "원" 기호와 쉼표 제거 > 숫자로 변환
                product_price = product_price.replace("원","").replace(",","").strip()

                # 데이터베이스에 삽입할 SQL 쿼리 작성
                sql = """INSERT INTO products (product_name, product_brand, product_price)
                         VALUES (%s, %s, %s)"""
                cur.execute(sql, (product_name, product_brand, product_price))
                
                print(f"브랜드 : {product_brand}")
                print(f"제품명 : {product_name}")
                print(f"제품 가격 : {product_price}")
                print(f"Data for {product_name} inserted successfully.")
        
        # 변경 사항을 커밋
        conn.commit()

finally:
    # 데이터베이스 연결 종료
    conn.close()
    print("Database connection closed.")
    # 브라우저 종료
    driver.quit()
