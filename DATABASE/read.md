## < 데이터 베이스 생성 및 삭제 >
- CREATE DATABASE 정승원(:만들려는 데이터 베이스이름) : 정승원이란 데이터베이스를 생성
- SHOW DATABASES; : 나의 데이터베이스들을 보여줌
- USE mydatabase; : mydatabase를 이용한다는 명령어
- DROP DATABASE IF EXISTS mydatabase; : 만약 데이터베이스가 존재한다면 삭제한다.

## < 접속 >
- USE mysql; : mysql 접속
- SELECT * FROM USER; : 로컬 상황과 권한을 보여줌

## < 사용자 생성 밒 비밀번호 변경 >
- CREATE USER 'username'@'localhost' IDENTIFIED BY 'user_password'; : 유저 생성
- SET PASSWORD FOR 'username'@'%' = '신규비밀번호'; : 사용자 비밀번호 변경

## < 권한 부여 및 확인 >
# 로컬호스트 경로의 username이라는 유저에 .(전체권한)을 부여하겠다.
- GRANT ALL PRIVILEGES ON . TO 'username'@'localhost';

- SHOW GRANTS FOR 'username'@'localhost';
- SHOW GRANTS; : 현재 로그인한 유저의 권환 확

## < 사용자 삭제 >
- DROP USER 'username'@'localhost';

## 쿼리 최적화 (인덱스 : 듀이 십진분류법)
