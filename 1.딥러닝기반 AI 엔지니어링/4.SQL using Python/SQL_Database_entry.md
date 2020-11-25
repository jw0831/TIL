## SQL Database 입문 
참고: https://github.com/ahracho/TIL/blob/master/SQL/sql_20170328.md

참고 : codeschool free day에 다운받은 강의자료  

### 1. Understanding Database
- Database란 : 정보를 모아놓고 정리해서 쉽게 업데이트 하고, 보여줄 수 있도록 하는 구조  
- 영화 상영시간을 찾아보고 싶을 때, 사이트에서 검색을 할 수도 있고, 신문 광고를 볼 수도 있찌만, 신문 광고는 사이트에서와 달리 정보가 업데이트 되지 않는다. 사이트에서 최신 정보를 찾아볼 수 있는 건, DB의 최신 자료를 사이트에서 보여주는 것이기 때문!  
- DB는 거의 모든 디바이스에서 사용되고 있다.  
- 영화관 DB를 상상해 보면, CGV 라는 DB가 있고, 그 안에 테이블로 정보들을 관리한다. 예를 들어, 영화 정보 테이블, 상영시간 테이블 등등
- 테이블의 행은 하나의 데이터셋을 나타낸다. A row represents an entire data record within each table.  
- 테이블의 열은 속성을 나타낸다.  
- 각 테이블에는 Unique Identifier가 있다. Primary key of the table : 즉 각 데이터셋을 고유하게 나타내는 속성  

### 2. SQL Language
- SQL : DB와 상호작용하도록 작성된 프로그래밍 언어  
- SQL로 작성된 문장을 DB에 전달하면 DB가 처리결과를 리턴한다.  


- 테이블에서 특정 열 내용 탐색하기 
~~~sql
SELECT title
FROM movies;
# title 열에 있는 데이터만 리턴

SELECT title, genre
FROM movies;
# title, genre 열에 있는 데이터 리턴

SELECT *
FROM movies;
# 모든 열의 데이터 리턴
~~~

- 조건에 맞는 데이터 탐색하기 
~~~sql
SELECT title
FROM movies
WHERE id = 2;
# id 값이 2인 행의 title 열 값 리턴

SELECT *
FROM movies
WHERE title = 'The Kid';
# title이 The Kid인 행의 모든 열 데이터 리턴
~~~

### 3. Guiding Data Criteria
- 데이터를 정렬하고 싶을 때  
~~~sql
SELECT title
FROM movies
ORDER BY duration;
# duration 열의 오름차순으로 title 열의 데이터 정렬

SELECT title
FROM movies
ORDER BY duration DESC; 
# 내림차순으로 정렬
~~~

- 데이터 비교를 통해 걸러내기
~~~sql
SELECT title
FROM movies
WHERE duration > 100;
# WHERE에 비교문 추가

SELECT *
FROM movies
WHERE genre <> 'Horror';
# 장르가 호러가 아닌 것만 골라서 리턴
~~~

- 여러 조건 걸기
~~~sql
SELECT *
FROM movies
WHERE id = 1 AND genre = 'Comedy';
# id가 1이면서 장르가 코미디인 영화 골라내기

SELECT *
FROM movies
WHERE id =1 OR genre = 'Comedy';
# id가 1이거나 장르가 코미디인 영화 골라내기
~~~

### 4. Adding Data
- 지금 있는 테이블에 데이터를 더하고 싶으면?
~~~sql
INSERT INTO movies (id, title, genre, duration)
VALUES (5, 'The Circus', 'Comedy', 71);
# 열 순서는 표랑 안 맞아도 되지만 column - value 쌍은 맞아야 해

INSERT INTO movies
VALUES (5, 'The Circus', 'Comedy', 71);
# 이때는 열 순서를 꼭 맞춰야해

INSERT INTO movies (title, duration)
VALUES ('The Fly', 80);
# id가 primary key이기 때문에 id는 명시 안 해줘도 자동으로 들어가, 나머지 열은 NULL

# NULL value represents missing data
~~~

### 5. Changing Current Data
- 현재 저장되어 있는 내용을 수정하고 싶다!
~~~sql
# WHERE은 옵션
UPDATE movies
SET genre = 'Romance'
WHERE title = 'The Circus';
# 타이틀이 The circus 인 애의 genre를 로맨스로 바꿔

UPDATE movies
SET genre = 'Comedy', duration = 70
WHERE id = 5; 
# 여러 열을 동시에 수정할 수도 있다.

UPDATE movies
SET genre = 'Romance'
WHERE id = 3 OR id = 5;
# 여러 행을 동시에 수정할 수도 있다.
~~~

### 6. Removing data
- 지금까지 Select, Add, Edit까지 했어, 그 다음은 delete

~~~sql
# WHERE은 옵션이지만, 없으면 테이블 전체가 삭제되겠지

DELETE FROM movies WHERE id = 5;

DELETE FROM movies WHERE duration < 100;
# 여러 행을 삭제할 수 있어
~~~

### 7. Creating and Removing Database and Tables
- 데이터베이스와 테이블을 새로 만들자!
- 메가박스 데이터베이스를 만들고 싶어
~~~sql
CREATE DATABASE megabox;
# DB가 새로 만들어졌지만 테이블은 하나도 없는 상태

DROP DATABASE megabox;
# DB 자체를 삭제 => DB 안의 모든 데이터가 삭제되니까 조심!
~~~

- DB 안에 테이블을 만들자
~~~sql
CREATE TABLE movies
(
  id int, # primary key
  title varchar(50), # varchar => letters or numbers
  genre varchar(15),
  duration int
);

DROP TABLE movies;
# 테이블만 삭제
~~~

### 8. Manipulating Tables
- add, change, drop a column from a TABLE
~~~sql
# 새로운 열 추가하기
ALTER TABLE movies
ADD COLUMN ratings int;

# 새로운 열이 추가됐으니까 기존 데이터에 채워넣기
UPDATE movies
SET ratings = 8
WHERE id = 1;

# 열 삭제하기
ALTER TABLE movies
DROP COLUMN ratings;
~~~
