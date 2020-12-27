# Regular Expression

- 규칙, 패턴을 가진 문자열을 표현하는 방법
- 텍스트 처리 작업에 있어 아주 중요한 정규 표현식에 관한 문법 & 사용 정리. (Python re 패키지 기준)

```python
import re
```

### **`Navigator`**

- [re.match](https://github.com/ineed-coffee/TIL/blob/master/regular expression/all about RE.md#idx1)
- [re.search](https://github.com/ineed-coffee/TIL/blob/master/regular expression/all about RE.md#idx2)
- [re.findall](https://github.com/ineed-coffee/TIL/blob/master/regular expression/all about RE.md#idx3)
- [re.compile](https://github.com/ineed-coffee/TIL/blob/master/regular expression/all about RE.md#idx4)
- [re.sub](https://github.com/ineed-coffee/TIL/blob/master/regular expression/all about RE.md#idx5)
- [meta strings](https://github.com/ineed-coffee/TIL/blob/master/regular expression/all about RE.md#idx6)
- [groups](https://github.com/ineed-coffee/TIL/blob/master/regular expression/all about RE.md#idx7)
- [OR , AND](https://github.com/ineed-coffee/TIL/blob/master/regular expression/all about RE.md#idx8)

------



### ➡️ re.match 

```python
re.match(검사패턴,입력 문자열)
```



> **세부내용** :

- 입력 문자열을 처음부터 검사하면서 검사패턴을 찾으면 정보를 반환하며 종료.
- 검사 도중 패턴 불일치가 일어나면 나머지 문자열에 대해서는 검사를 더이상 진행하지 않는다.
- `<re.Match object; span=(0, 5), match='hello'>` 와 같이 `span` 정보와 실제 찾은 `match` 정보를 반환해주며 , 일치 패턴이 없으면 반환값은 None 이다.
- 매칭된 문자열을 반환 받으려면 `re.Match object.group()` 메소드 활용

------



### ➡️ re.search 

```python
re.search(검사패턴,입력 문자열)
```



> **세부내용:**

- match 와 거의 비슷하지만 패턴 매칭이 실패해도 문자열의 끝까지 계속 조사하며 일치 패턴을 발견하는 순간 조사가 종료된다.
- 입력 문자열에서 패턴이 여러번 존재하여도 패턴 일치와 함께 조사가 마무리되므로 가장 처음 등장하는 패턴 기준으로 반환된다.
- `span` 정보는 문자열에서 일치한 패턴이 시작과 끝 인덱스 정보를 담고 있다.

------



### ➡️re.findall 

```python
re.findall(검사패턴 , 입력 문자열)
```



> **세부내용:**

- 입력 문자열의 시작부터 끝까지 조사하면서 일치하는 모든 패턴을 리스트 형식으로 반환한다.
- match , search 와는 다르게 span 정보는 담겨 있지 않다.
- `finditer` 메소드를 활용하면 `span` 정보가 요소로 이루어진 반복 객체가 반환된다.

------



### ➡️re.compile 

```python
pattern = re.compile('정규표현식')
```



> **세부내용:**

- 패턴을 정의하여 패턴 객체를 생성할 수 있다.
- 패턴 객체를 활용하면 위의 메소드들을 re.match , re.search 대신 `pattern.match(입력 문자열)` 의 형식으로 사용할 수 있다.

------



### ➡️ re.sub 

```python
re.sub(정규표현식 , 대체 문자열 , 입력 문자열)
```



> **세부내용:**

- 파이썬 내장 문자열 대체 메소드인 replace 와 비슷한 작업을 수행하며 특정 단어가 아닌 정규표현식으로부터 매칭되는 모든 문자열을 대체 문자열로 바꾸는 작업이 가능하다.
- 이때 입력 문자열은 실제로는 변하지는 않고 대체 문자열로 바뀐 문자열이 반환된다.

------



### ➡️ meta strings 

> **정규표현식을 구성하는 여러 메타 문자들의 사용법**



🖊️ **`[] (대괄호)`**

- 대괄호 내부에 있는 문자들과 매치
- ex. [abc] => 입력 : b (match) , d (fail)
- [A-Z] , [a-z] , [a-zA-z] : 각각 모든 대문자 알파벳 , 모든 소문자 알파벳 , 모든 알파벳 과 매치
- [0-9] , [가-힣] : 각각 모든 숫자 , 모든 한글과 매치

🖊️ **`\ (역슬래시)`**

- 특수문자 일부를 메타문자가 아닌 그대로 쓰는 경우 혹은 특정 알파벳과 조합하여 집합의 의미를 가짐
- \d : 숫자 전체 그룹 , [0-9] 과 같은 의미
- \D : 대문자 활용은 Not 의 의미를 뜻함. 즉 숫자를 제외한 모든 문자와 매치 , [^0-9]
- \w : 모든 알파벳과 숫자 그룹 + _(언더바) , [a-zA-Z0-9_] 과 같은 의미
- \W : (알파벳 전체+숫자) 를 제외한 모든 글자와 매치 , [^a-zA-Z0-9]
- \s : 공백 문자 ( space , enter , tab)
- \+ , \* , \$ : 메타문자가 아닌 특수문자 그대로 패턴을 조사할 때 역슬래쉬를 붙임

🖊️ **`+` , `\*` , `{}` , `?` (반복지정 메타 문자)**

`+` : 최소 1번 이상의 반복을 조사함

- 예) *do+g* ==> *dog , doog, doooog* (매치) , *dg , doof* (매치 없음)

`*` : 최소 0번 이상의 반복을 조사함

- 예) *do\*g* ==> *dg,dog,doog* (매치) , *df* (매치 없음)

`{}` : 조사할 반복회수를 직접 숫자로 지정 (범위 지정도 가능)

- 예) *do{2}g* ==> *doog* (매치) , *dog , dooog* (매치 없음)
- 예2) *do{1,3}g* ==> *dog , doog , dooog* (매치) , *doooog* (매치 없음)

`?` : {0,1} 과 같은 의미로 없거나 최대 1번까지만 조사하는 반복 메타 문자

- 예) *do?g* ==> *dg , dog* (매치) , *doog,dooog* (매치 없음)

🖊️ **`. (점)`**

- 어떤 글자도 매치하는 메타 문자.
- 예) *d.g* ==> *dmg , dhg , drg* (매치) , *dgf , ddd* (매치 없음)
- 점 자체의 문자로 표현식에 활용하려면 `\.` 혹은 `[.]` 로 지정

🖊️ **`^ , $ (시작과 끝 , 혹은 부정)`** 

`^` : 일반적인 사용은 해당 패턴으로 문자열이 시작하는지를 조사하는 메타문자. 대괄호 안에 쓰이면 NOT 의 의미로 쓰인다.

- *^dog* ==> *dog looks happy* (매치) , *that's a cute dog* (매치 없음)
- 특수문자 그대로 활용하려면 `\^` 혹은 `[^]`

`$` : 문자열이 해당 패턴으로 끝나는지를 조사하는 메타문자.

- *dog$* ==> *that's a cute dog* (매치) , *dog looks happy* (매치 없음)
- 특수문자 그대로 활용하려면 `\$` 혹은 `[$]`

------



### ➡️ groups 



> 정규 표현식을 이루는 세부 표현식들에 대하여 그룹이름을 부여한 뒤에 매치된 문자열로부터 그룹이름으로 참조할 수 있다.



```python
( ?P<function name> 정규 표현식 일부)
pattern='(?P<letter>[a-zA-Z_]\w*)[(](?P<number>[a-zA-Z0-9,]*)[)]$'
res = re.match(pattern,'print(345,34)')
res.group('letter')
'print'
```



------



### ➡️ OR , AND 



🖊️ **`OR`**

```python
pattern = '(group1)|(group2)'
```



🖊️ **`AND`** :정식 표현은 아님 , 확장 표현

```python
pattern = '(?=group1)(?=group2)'
```



## Reference

https://github.com/ineed-coffee