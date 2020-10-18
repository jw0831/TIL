# Database (using Python module)

강사: 박길식 교수님

작성자: 김진원

------

- 기본 지식:
- 데이터베이스 : 데이터가 모여있는 집합체 -> 중복되는경우 발생 (일관성 유지 어려움 -> 데디터베이스 체계적으로 관리 필요) ====> DBMS 데이터베이스 관리 시스템이 개발됨
- DBMS (소프트웨어): 오라클, MSSQL, MYSQL, SQLITE, MariaDB... 이 모든것이 데이터베이스 관리 도구들임.
  - 위 소프트웨어들이 언어가 좀달라도 공용어가 있음 => SQL (Structured Query Language) 그러므로 SQL의 문법만 알고 있으면 각기 다른 소프트웨어에서 명령을 내릴수 있다.

### Basically, Python provides **SQLITE3** (DBMS)

파이썬에서 기본적으로 제공되는 DBMS = SQLITE3

- DB연결/해제, 커서, 데이터 삽입/로드/조회/수정/삭제

<u>판다스</u>에서는 **DataFrame** 으로 불렀다면, <u>Database</u>에서는 **Table** 이라고 한다.

### **자료형**

| Python | SQLite  |
| ------ | ------- |
| int    | integer |
| float  | real    |
| str    | text    |
| bytes  | BLOB    |
| None   | NULL    |

#### Database (file형태로 존재, 하나의 논리적 파일형태로 생각)

- 테이블 구조 설계 (각 컬럼에 대한 타입 정의, **CREATE TABLE** 명령) -> 데이터 저장(**INSERT INTO**) -> 조회/수정/삭제/추가...

- 테이블이 저장되어지는 장소: Database

- Database가 이미 존제 한다면 (연결 하는 작업 필요)

#### 1.연결

```python
# database 연결
conn=sqlite3.connect("emp.db") #연결하는 명령
# 기존에 emp.db파일(database)이 없다면 -> 새롭게 생성하고 연결
# 기존에 emp.db파일(database)이 있다면 -> 연결을 진행
```

#### **2.테이블 생성**

```python
# CREATE TABLE
# conn.execute('공용어 (SQL) 활용')
# 데이터베이스 객체 변수를 이용햐여 테이블 설계, 테이블 명은 emp_data로 하여라
# create table 테이블명(컬럼1 타입, 컬럼2 타입,..., 컬럼n 타입)
conn.execute('create table emp_data(id integer, name text, nickname text, department text, employment_date text)')
# nick name 이렇게 공백이 생기면 안된다. nick_name 공백으로 구분을 짖는 명령어기 때문에 2개의 공백은 허용되지 않는다!
# 같은 이름의 테이블은 두번이상 생성이 안된다!
```

#### **3.cursor 를 이용한 데이터 추가**

```python
# cursor 생성
cur=conn.cursor()
```

#### 4.데이터 추가

```python
# data 추가
# data 를 한개 추가할때는 execute(), 여러개는 executemany()
# insert into 테이블명 values (?, ?, ?, ?, ... , ?)
###### execute ######
# cur.execute('insert into 테이블명 values ('a', 100)') 컬럼이 2개일 경우
# cur.execute('insert into 테이블명 values (?,?)', ('a', 100)) 뒤에 a 와 100이 물음표로 전달되는 방법
###### executemany ######
# data=[('a',100),('b',200)]
# cur.executemany('insert into 테이블명 values (?,?)', data)

cur.executemany(
'insert into emp_data values (?,?,?,?,?)',
    [(1, 'gildong', 'gd', 'marketing', '2020-10-06 10:36:00.000'),
     (2, 'sunshin', 'ss', 'marketing', '2019-10-06 10:36:00.000'),
     (3, 'yusin', 'ys', 'development', '2020-01-06 10:36:00.000'),
     (4, 'sejong', 'sj', 'marketing', '2020-05-06 10:36:00.000'),
     (5, 'bogo', 'bg', 'development', '2020-07-06 10:36:00.000')
    ]
)
```

#### 5.데이터 출력

```python
# emp_data테이블로 부터 모든 데이터를 가져와라 -> 가져온 데이터 -> cur가 데이터를 가리키고 있음
cur.execute('select * from emp_data')
```

```python
# cur가 가리키고 있는 위치부터 데이터를 하나씩 읽어내려가면서 row에 저장
for row in cur:
    print(row)
```

```python
# data를 가져올때 fetchall() 명령을 사용할 수 있다.
rows=cur.fetchall()
print(rows)
```

#### 6.저장 및 종료

```python
# 데이터베이스 저장
conn.commit()
# 데이터베이스 연결 종료
conn.close() #닫아주는게 리소스 관리 차원에서 여러모로 좋다.
```

다시 연결하고 싶은경우 1번으로 가서 연결 후 3 번으로 커서를 만들어주고

5번으로 데이터를 읽거나 2번에서 테이블을 만들거나 하면 된다.

### 데이터베이스를 테이블로 불러오는 작업 및 다른 응용방법은 1006 class.ipynb 참고



[저자 박길식](http://www.yes24.com/24/AuthorFile/Author/205437)

