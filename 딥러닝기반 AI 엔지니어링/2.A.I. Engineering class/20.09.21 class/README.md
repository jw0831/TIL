# 작성중..

#### 2020.09.21

# DataFrame 전처리, 문법

- Data 예측 전에 알면 좋은 지식!

### **Pandas**

> 사용되어진 함수: 

- .map()
- .duplicated()
- .drop_duplicates()
- .replace()
- .cut()    #구간을 나눌때 사용
  - right 옵션으로 개구간 및 폐구간 설정을 할 수 있다.
  - labels 옵션으로 각각의 구간안에 이름을 지정할 수 있다.
- .codes    #구간의 인덱스 번호를 나타낸다.
- .categories    #카테고리의 종류가 어떻게 나눠져 있는지 보여준다.
- .value_counts()    #구간별 건수를 알아보고 싶을때 괄호 안에 넣는다.



> 사용된 식: 

- lambda

  - ```python
    # 작업의 순서를 생각해 보자!
    # 소문자 변환 먼저? 찾은다음에?
    # 1. 소문자로 먼저 변환
    # x에는 food column이 들어간다.
    # 소문자로 변환된 데이터가 meat_to_ani로 가서 소문자에 해당되는 값을 가져와야 한다.
    # map 함수는 다양하게 사용해보고 손에 익혀야 합니다.
    data=pd.DataFrame({
        'food':['bacon', 'pork', 'bacon',
               'beef', 'Bacon', 'ham'],
        'ounces':[4,3,12,6,8,3]    
    })
    data
    data['food'].map(lambda x: meat_to_ani[x.lower()] ) # pig, pig, pig, cow, pig, pig 출력
    ```

    

>  스킬:

- mapping 규칙 생성

  - ```python
    meat_to_ani={
    	'bacon':'pig',
    	'pork':'pig',
    	'beef':'cow',
    	'ham':'pig'
    }
    ```

- DataFrame 의 열(columns)에 대해 대 소문자 변경시, 하나의 열은 -> 시리즈 이며 시리즈는 .lower() 또는 .upper() 속성 (attribute)를 갖고 있지 않는다. 그러므로 시리즈 안에 있는 각각의 데이터에 대해 속성을 설정할 때에는 str을 지정해 주어야 한다.

  - ```python
    lowercased=data.food.str.lower()
    data['animal']=lowercased.map(meat_to_ani) 
    #시리즈.map(딕셔너리) => 시리즈 타입으로 저장된
    #데이터가 딕셔너리의 키가 되며, 키에 해당되는 값이 리턴(시리즈)
    ```

- **축에대한 색인을 설정하는 방법** 을 배움

- 주피터 노트 한글 에러를 없에는 법

  - ```python
    import matplotlib
    from matplotlib import font_manager, rc
    import platform
    if platform.system()=="Windows":
        font_name=font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
    matplotlib.rcParams['axes.unicode_minus']=False
    
    import warnings
    warnings.filterwarnings("ignore")
    ```

    



