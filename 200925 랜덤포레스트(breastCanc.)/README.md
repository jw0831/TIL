# 0925 class 

### (오전: 24일 학습내용을 베이스로 유방암 데이터를 xTrain,yTrain,xTest,yTest 로 분류한것을 예측 모델 생성 및 예측 점수 확인)

- 원래 분류가 잘되어있는 데이터 [캐글: Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data)
- 따로 전처리를 하지않음
- x: 
  - 제외: 'id', 'diagnosis', 'Unnamed: 32'
  - 포함: [['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']]
- y:
  - 제외:  'diagnosis'를 제외하고 모든 컬럼
  - 포함: ['diagnosis']
  - y.ravel() 또는 flatten() 함수를 이용하여 1차원 배열로 변환

```python
### 모든 컬럼을 사용할 경우

data.columns

#데이터 분리:
'''
모든 열:
['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst', 'Unnamed: 32']
'''
Xfn=data[['radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst']]
Yfn=data['diagnosis']

x=Xfn

y=Yfn

y=y.ravel() #1차원 배열로 전환

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=0) #8:2의 비율로 나눈다.

xTrain.shape, xTest.shape

yTrain.shape, yTest.shape

#####################################################################################

## 모델 생성

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
# 최적의 파라미터를 검색
param_grid={
    'n_estimators': [11, 31, 51,100,200],
    'min_samples_split': [4, 6, 8 ,10],
    'max_depth' : [3, 5, 7]
}
# random_state 지정 (seed 와 유사한 개념)
rfc=RandomForestClassifier(random_state=2020)

CV_rfc = GridSearchCV(estimator=rfc, param_grid=param_grid, cv=5, n_jobs=-1)
CV_rfc.fit(xTrain, yTrain)
#최적의 파라미터 보기 및 점수 보기
CV_rfc.best_params_
CV_rfc.best_score_
#최적의 파라미터로 모델 생성
randomForest=RandomForestClassifier(n_estimators=31, min_samples_split=4, max_depth=7, random_state=2020, n_jobs=-1) #default : 100
#n_estimators = 11, 31, 51
#max_depth = 3, 5, 7
#min_samples_split: 4, 6, 8 ,10

randomForest.fit(xTrain, yTrain) #fit: 사이킷런에 있는 머신러닝 알고리즘 으로 모델 생성

## xTest 입력 및 예측결과 출력
yPred=randomForest.predict(xTest)
yPred

randomForest.score(xTrain, yTrain)
#xTest와 yTest 예측 점수
randomForest.score(xTest, yTest) #0.956140350877193

#####################################################################################

# KFold 교차검증
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

kfold=KFold(n_splits=10, shuffle=True, random_state=42)

from sklearn.ensemble import RandomForestRegressor

model=RandomForestRegressor(n_estimators=100,
                     n_jobs=-1,
                     random_state=42)

randomForest.fit(xTrain, yTrain)

pred=randomForest.predict(xTest)
pred

#RMSLE
from sklearn.metrics import make_scorer

def rmsle(pv, av): #예측값, 실제값
    #넘파이 배열로 변환
    pv=np.array(pv)
    av=np.array(av)
    #예측값과 실제값에 1을 더하고 로그를 씌운다
    log_predict=np.log(pv+1)
    log_actual=np.log(av+1)
    
    res=log_predict-log_actual
    res=np.square(res)
    res.mean() #합하는작업 따로 필요없음 평균을 구할때 자동임
    
    mean_res=res.mean()
    score=np.sqrt(mean_res)
    return score

rmsle_scorer=make_scorer(rmsle)
rmsle_scorer

score=cross_val_score(randomForest, xTrain, yTrain, cv=kfold, scoring=rmsle_scorer)
score #rmsle이므로 0에 가까울수록 잘나오는것임

score.mean() #교차 검증을 통해서 위의 전처리를 예측한 것이 얼마나 일반화가 잘되어 있는지 확인하는것임.
```

### 모델.score( , ) 메커니즘:

- 모델.score(xTest, yTest)

  1) 모델에 xTest가 입력

  2) 모델에서는 예측결과가 출력

  3) 예측 결과와 yTest간 비교를 하여, 점수를 계산(100%)



[MAPE, 그래프 등등 참고](https://www.kaggle.com/emanueleamcappella/random-forest-hyperparameters-tuning)

```python
# https://stackoverflow.com/questions/47648133/mape-calculation-in-python
MAPE 결과 나오는 코드
def percentage_error(actual, predicted):
    res = np.empty(actual.shape)
    for j in range(actual.shape[0]):
        if actual[j] != 0:
            res[j] = (actual[j] - predicted[j]) / actual[j]
        else:
            res[j] = predicted[j] / np.mean(actual)
    return res

def mean_absolute_percentage_error(y_true, y_pred): 
    return np.mean(np.abs(percentage_error(np.asarray(y_true), np.asarray(y_pred)))) * 100
  
mean_absolute_percentage_error(yTest, yPred)
```



[시계열 데이터와 랜덤 포레스트를 활용한 시간당 초미세먼지 농도 예측 ](https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO202013261020958&dbt=NART)

------

# 레이블 인코딩, 원핫 인코딩

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
```

> 문자 -> 숫자 : 레이블 인코딩, 원핫 인코딩
>
> 문자열 데이터 : 카테고리형 (학점, 도시...), 텍스트형 (일반적인 문장에 포함된 단어들 ..)
>
> A -> 1, B -> 2, ... CDF (레이블 인코딩, 숫자가 커질수록 학점이 나쁨)
>
> A<B<C<D<F
>
> 
>
> 서울 -> 1, 대전 -> 2, 부산 -> 3, 제주 -> 4, 강릉 ->5,.. (레이블 인코딩을 하면 안됨..................)
>
> 1+2=>3 서울+대전=부산?? 
>
> 1<2<3<...???
>
> A->1000, B->0100, O->0010, AB->0001 (원핫인코딩)
> 서울->10000, ... 강릉->00001 (원핫인코딩)

# label 인코딩 
주의: 회기모델을 만들때, 데이터를 이렇게 만들면 만드는 과정에서 문제가 생긴다.

냉장고에 에어컨을 더하면 전자레인지? 말이 안된다.. 크기순서같은 것도 없다.

레이블 인코딩을 할때는 0부터 시작해서 일련번호를 붙여준다. 데이터가 발생되는 순서대로 0부터 쭉 번호를 붙여준다.

문자열데이터를 숫자로 변환할때 사용하는 것이다.

주의!!! 레이블 인코딩은 선형회귀와 같은 알고리즘에 적용하면 안됨!!!

- 숫자간의 대소관계를 따지기 때문임.!!

```python
items=['tv', '냉장고', '에어컨','에어컨','전자레인지']
encoder=LabelEncoder()
encoder.fit(items)
labels=encoder.transform(items)
print(labels)
encoder.inverse_transform(labels) #원 데이터
encoder.classes_ #종류
```

> 하는 이유: 숫자나 문자가 서로 더해지거나 수식같은 관계가 전혀 없을경우

# 원핫 인코딩

주의할점:

1. 원핫인코딩을 하기 전에 모든 문자열 값을 숫자로 변환
2. 숫자로 변환된 데이터(2차원)에 대해 원핫인코딩

```python
# 1. 문자열 값을 숫자로 변환
items=['tv', '냉장고', '에어컨','에어컨','전자레인지']
encoder=LabelEncoder()
encoder.fit(items)
labels=encoder.transform(items)
print(labels)

# 2. 숫자로 변환된 데이터에 대해 원핫인코딩
# 1) 2차원으로 변환
labels.reshape(-1,1)
# 2) 원핫인코딩
labels=labels.reshape(-1,1)
ohe=OneHotEncoder()
ohe.fit(labels)
oh_labels=ohe.transform(labels)
oh_labels.toarray()
#getdummies 함수도 가능

#다른방법 한번에 하는법
df=pd.DataFrame(['tv', '냉장고', '에어컨','에어컨','전자레인지','tv'], columns=['items'])
pd.get_dummies(df) #OneHotEncoding
```





### 변수의 스케일링(표준화, 정규화)을 하지 않아도 됨 (DecisionTree, RandomForest) No Worry!

- 연속형, 바이너리형.. 데이터들이 혼합되어 있어도 잘 동작

유클리디안거리

x축: 몸무게, y축: 태어난 날로부터 경과일 (30살= 약 11000)    <이런데이터가 있다고 가정>

```python
거리: sqrt((y1-y1)^2 + (x2-x1)^2)
경과일에 영향을 어마어마하게 받는다.. (10000의 제곱때문에.. y축에 영향을 많이 받아버리는 문제)
이런문제 인해 표준화, 정규화를 했다.

표준화는 평균을 0으로 둔다.
-값은 평균보다 작다
+값은 평균보다 크다

정규화는 0 에서 1사이 (공식참고)
```

decision tree, random forest는 변수의 스케일링을 해도되고 안해도 된다. 스스로 하기때문에...

엔트로피계산 과정에서 해버린다. (criterion = 'entropy')

지니(gini)계수까지 총 2가지 방식이 있다. (default)

주의: RNN등 다른 방식은 정규화 표준화 꼭 해주어야함!



아래와 같은경우

- train -> dt -> 모델 -> train입력 -> 모델평가(성능 100%==과적합! 문제있다!) => 가지치기를 안함. (트레인데이터에대한 모든 케이스가 트리 안에 있는경우) prunning(가지치기를 해야함)
- 성능이 좀 떨어지는게 당연한것임
  - train입력 -> 모델평가 (95%)
  - test 입력 -> 모델평가 (93%)
  - train입력 -> 모델평가 (95%) >> test 입력 -> 모델평가 (73%) 
    - => 오버피팅(일반화를(가지치기)를 하지 않아서...)





[3.3 scikit-learn의 전처리 기능](https://datascienceschool.net/view-notebook/f43be7d6515b48c0beb909826993c856/)



# 함수

- 교차행렬 confusion_matrix:

  - 만든 모델이 얼마나 정확한지 확인

    ```python
    from sklearn.metrics import confusion_matrix
    cm= confusion_matrix(ytest, ypred)
    cm
    
    """
    array([[암, not암],
          [not암, 암]])
         
    array([실제암: [89(TP),  1(FN)],  
           not암: [ 1(FP), 52(TN)]]) ,
    """
    실제로 암인데 암예측 89건 (true positive), 실제로 암인데 암이 아니다예측 2건(False negative)
    암을 not암으로 예측(False positive), 암이아닌데 암이 아닌것으로 예측 52건 (True negative)
    암인데 암이 아니라고 예측한 False Positive
    
    TP: 암을 암이라고 정확하게 예측
    TN: 암이 아닌것을 암이 아니라고 정확하게 예측
    FP: 암을 암이 아니라고 잘못 예측 (가장 위험)
    FN: 암이 아닌것을 암이라고 잘못 예측
      
    #암 (cancer)을 검진할때 암에 걸린것을 양성(positive), 걸리지 않은것을 음성 (negative)
    #종양 (tumar) 양성 (benign), 악성(malignat)
    ```

    

연속형 수치값을 예상할때에는 random_forest 의 regressor를 사용하면 된다.

[House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)

회기와 분류에대해 위키피디아..[랜덤포레스트 회기와 분류](https://ko.wikipedia.org/wiki/랜덤_포레스트)

