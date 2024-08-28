USE yes24;
-- # 기본 조회 및 필터링
-- 1) 제목과, 저자의 목록
SELECT title, author FROM books;

-- 2) 평점이 8점 보다 크거나 같은 것을 확인
SELECT * FROM books WHERE rating >= 8.0;

-- 3) 리뷰 수가 100개 이상인 책들의 제목과 리뷰 수를 조회
SELECT title, review FROM books WHERE review >= 100;

-- 4) 가격이 20,000원 미만인 책들의 제목과 가격을 조회
SELECT title, price FROM books WHERE price < 20000;

-- 5) 국내 TOP100에 4주 이상 머문 책들을 조회
SELECT * FROM books WHERE ranking_weeks >= 4 ORDER BY ranking_weeks DESC;

-- 6) 특정 저자의 모든 책을 조회
SELECT * FROM books WHERE author = '강용수 저'

-- # 조인 및 관계
-- 1) 저자별로 출판한 책의 수를 조회
SELECT author, COUNT(*) FROM books GROUP BY author;

-- 2) 가장 많은 책을 출판한 출판사 조회
SELECT publisher, COUNT(*) as publisher_count FROM books GROUP BY publisher
ORDER BY publisher_count DESC LIMIT 1;

-- 3) 가장 높은 평점의 저자
SELECT author, AVG(rating) as rating_ranking FROM books GROUP BY author;

-- 4) 국내도서 랭킹 1위인 책의 제목과 저자 조회
SELECT * FROM books WHERE ranking = 1

-- 5) 판매 지수와 리뷰 수가 모두 높은 상위 10개책 조회
SELECT title, sales, review FROM books ORDER BY sales DESC, review DESC LIMIT 10;

-- # 집계 및 그룹화
-- 1) 저자별 평균 평점을 계산
SELECT author, AVG(rating) AS rating_avg FROM books GROUP BY author ORDER BY rating_avg DESC;

-- 2) 출판일별 출간된 책의 수를 계산
SELECT publishing, COUNT(*) FROM books GROUP BY publishing;

-- 3) 책 제목별 평균가격을 조회
SELECT title, AVG(price) FROM books GROUP BY title;
SELECT title, price FROM books;

-- 4) 리뷰 수가 가장 많은 상위 5권의 책조회
SELECT * FROM books ORDER BY review DESC LIMIT 5;

-- 5) 국내 도서 랭킹 별 평균 리뷰 수 계산
SELECT ranking, AVG(review) FROM books GROUP BY ranking;

-- # 서브쿼리 및 고급 기능
-- 1) 평균 평정보다 높은 평점을 받은 책들 조회
SELECT title, rating FROM books WHERE rating > (SELECT AVG(rating) FROM books) ORDER BY rating DESC;

-- 2) 평균 가격보다 비싼 책들의 제목과 가격을 조회
SELECT title, price FROM books WHERE price > (SELECT AVG(price) FROM books);

-- 3) 가장 많은 리뷰를 받은 책보다 많은 리뷰를 받은 다른 책들을 조회
SELECT title, review FROM books WHERE review > (SELECT MAX(review) FROM books);

-- 4) 평균 판매지수보다 낮은 판매지수를 가진 책들을 조회
SELECT title, sales FROM books WHERE sales < (SELECT AVG(sales) FROM books);

-- 5) 가장 많이 출판된 저자의 책들 중 최근에 출판된 책을 조회
SELECT author, title FROM books WHERE author = (SELECT author FROM books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1);
SELECT author FROM books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1; -- 가장 많이 출판된 저자

-- # 데이터 수정 및 관리
-- 1) 특정 책의 가격을 업데이트
UPDATE Books SET title = '제목 업데이트' WHERE author = '최태성의 저'

-- 2) 판매지수가 가장 낮은 책을 데이터베이스에서 삭제
DELETE FROM books WHERE sales = (SELECT MIN(sales)) FROM books

-- 3) 틀정 출판사가 출판한 모든 책의 평점을 1정 증가
UPDATE books SET rating = rating + 1 WHERE publisher = '웅진하우스'

-- # 데이터 분석 예제
-- 1) 저자별 평균 평점 및 판매지수를 분석하여 인기 있는 저자를 확인
SELECT author, AVG(rating), AVG(sales) FROM books GROUP BY author ORDER BY AVG(rating) DESC, AVG(sales) DESC;

-- 2) 출판일에 따른 책 가격의 변동 추세를 분석
SELECT publishing, AVG(price) FROM books GROUP BY publishing ORDER BY publishing ASC;

-- 3) 출판사별 출간된 책의 수와 평균 리뷰 수를 비교 분석
SELECT publisher, COUNT(*) AS book_count, SUM(review) AS review_sum FROM books GROUP BY publisher ORDER BY book_count DESC;

-- 4) 국내도서 랭킹과 판매지수의 상관 관계를 분석
SELECT ranking, AVG(sales) FROM books GROUP BY ranking;

-- 5) 가격 대비 리뷰 수와 평점의 관계를 분석(가성비 좋은 책찾기)
SELECT price, AVG(review), AVG(rating) FROM books GROUP BY price;