# Field Manual Style (전처리/타이타닉 데이터)

- 전처리 위주의 수업 

- Decision Tree 사용

- 목표 정확도: 0.8

- 시각화 -> EDA Exploratory Data Analysis (탐색적 데이터 분석) -> 특성공학 feature engineering (변수 추가, 선택...) -> 모델링 -> 평가

```python
import seaborn as sns
sns.set() #디폴트 색상, 스타일 등 설정 (오늘은 디폴트 사용)
```

> - 어린 아이나 여성이 먼저 구조가 될수 있도록 하기 때문에 Name열의 호칭 정보가 상당히 중요하다.
> - Ticket 번호 및 Fare 가 몇등석인지 선실의 정보등을 알 수도 있다.
> - Cabin 은 결측값이 매우 많다. (처리)

- 훈련 데이터 (70%), 테스트 데이터 (30%)

```python
# 아래 함수를 사용해서 컬럼의 종류나 결측값을 분석하기 편함
test.isnull().sum()
```

- features과 생존여부 사이에 어떤 관계가 있는지? (상관계수 분석)



등실별 생존여부 (1등실이 가장 높다는 것을 확인할 수 있다.)

```python
train[['Pclass','Survived']].groupby(['Pclass'], as_index=False).mean()
```

violin plot에 대해

![violin plot](README.assets/스크린샷 2020-09-23 오전 11.45.54.png)

dataset['Title']=dataset.Name.str.extract("([A-Za-z]+\.)")

"([A-Za-z]+)\.") 이렇게 하면 호칭 뒤에 .이 제외된다.

```python
#시각화 -> EDA -> 특성공학(변수 추가/선택...) -> 모델링 -> 평가
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set() #디폴트 색상, 스타일 등 설정

train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")

train.head()
train.shape
train.describe()
train.info()
train.describe(include=['O']) #Object 타입에 대한 기술통계를 구해라
train.info()
train.isnull().sum()

test.shape
#891(훈련) + 418(테스트) = 1309건 데이터
#2/3(훈련)+1/3(테스트)
#   70%         30%

test.info()
test.head()
test.isnull().sum()

#features과 생존여부 사이에 어떤 관계가 있는지?

survived=train[train['Survived']==1]
not_survived=train[train['Survived']==0]
#1.퀴즈
# Survived: 300 (40.0%)
# Not Survived: 591 (60.0%)
# Total : 891

print("Survived: %d (%.1f%%)" % (len(survived), len(survived) / len(train)*100.0 ))
print("Not Survived: %d (%.1f%%)" % (len(not_survived), len(not_survived) / len(train)*100.0 ))
print("Total : %d" % len(train))


train.Pclass.value_counts()

#2.퀴즈 
#등실별 생존여부에 따른 인원수 출력
#train.groupby(["Pclass", "Survived"]).size()
#train.groupby("Pclass")["Survived"].value_counts()
#train.groupby(['Pclass','Survived']).apply(lambda x:len(x))
train.groupby("Pclass").Survived.value_counts()

train[['Pclass','Survived']].groupby(['Pclass']).mean()

train[['Pclass','Survived']].groupby(['Pclass'], as_index=False).mean()

#train.groupby('Pclass').Survived.mean().plot() #선그래프
train.groupby('Pclass').Survived.mean().plot(kind='bar')

sns.barplot(x='Pclass', y='Survived', data=train)

#성별과 생존여부?
train.Sex.value_counts()

train.groupby('Sex').Survived.value_counts()

train[['Sex', 'Survived']].groupby('Sex').mean()
train[['Sex', 'Survived']].groupby('Sex', as_index=False).mean()

sns.barplot(x='Sex', y='Survived',data=train)

#Pclass & Sex 동시 고려 생존율과의 관계

#크로스테이블(교차행렬)
pd.crosstab(train['Pclass'], train['Sex'])

sns.factorplot('Sex', 'Survived', hue='Pclass', size=4, aspect=2, data=train)

#sns.factorplot(x='Pclass', y='Survived', hue='Sex', data=train)

#승선항 : 3개
sns.factorplot(x='Pclass', y='Survived', hue='Sex', col='Embarked', data=train)

# 승선 항구에 따른 생존여부?
train.Embarked.value_counts()

train.groupby('Embarked').Survived.value_counts()

sns.barplot(x='Embarked', y='Survived', data=train)

#parch 와의 생존여부?
train.Parch.value_counts()

train.groupby('Parch').Survived.value_counts()

train[['Parch', 'Survived']].groupby('Parch', as_index=False).mean()

sns.barplot(x='Parch', y='Survived', data=train)
#error bar(오차 막대): 신뢰구간

sns.barplot(x='Parch', y='Survived', data=train, ci=None)

sns.barplot(x='Parch', y='Survived', data=train, ci="sd")

#SibSp와의 생존여부?
train.SibSp.value_counts()

train.groupby('SibSp').Survived.value_counts()

train[['SibSp', 'Survived']].groupby('SibSp', as_index=False).mean()

sns.barplot(x='SibSp', y='Survived', data=train, ci=None)

#연령별(y), 항구/pclass/성별 (x) 생존여부(범례) -> 바이올린 plot

#외형(틀)은 matplotlib.pyplot(plt)
#내부에 들어가는 그래는 seaborn
fig=plt.figure(figsize=(15,5))
ax1=fig.add_subplot(131) #1줄 3칸으로 나눈 다음 1번째 위치(칸)
ax2=fig.add_subplot(132)
ax3=fig.add_subplot(133)
#연령별(y), 항구/pclass/성별 (x) 생존여부(범례)
sns.violinplot(x='Embarked', y='Age', hue='Survived', data=train,ax= ax1)
sns.violinplot(x='Pclass', y='Age', hue='Survived', data=train,ax= ax2)
sns.violinplot(x='Sex', y='Age', hue='Survived', data=train,ax= ax3)

#흰색점 : 중앙값(median)
#중앙의 두꺼운 선 : 사분위 범위
#중앙의 얇은 선 : 신뢰구간(95% 신뢰구간)

total_survived=train[train['Survived']==1]
total_not_survived=train[train['Survived']==0]
male_survived=train[(train['Survived']==1) & (train['Sex']=='male')]
female_survived=train[(train['Survived']==1) & (train['Sex']=='female')]
male_not_survived=train[(train['Survived']==0) & (train['Sex']=='male')]
female_not_survived=train[(train['Survived']==0) & (train['Sex']=='female')]

#distplot :히스토그램, 수치형 데이터의 빈도수를 시각화(나이에 따른 빈도수)
plt.figure(figsize=[15,5])
plt.subplot(111)
sns.distplot(total_survived['Age'].dropna().values, kde=False, bins=range(0,81,1), 
             color='blue')
sns.distplot(total_not_survived['Age'].dropna().values, 
             kde=False, bins=range(0,81,1), color='red', axlabel='Age')
#kde=True 디폴트, kde:밀집도그래프
#sns.set_style("bluegrid")

#total_survived['Age'].dropna().values

plt.figure(figsize=[15,5])
plt.subplot(121) #1줄 2칸, 1번째 칸에 출력
sns.distplot(female_survived['Age'].dropna().values, kde=False, bins=range(0,81,1), 
             color='blue', axlabel='Female Age')
sns.distplot(female_not_survived['Age'].dropna().values, kde=False, bins=range(0,81,1), 
             color='red', axlabel='Female Age')

plt.subplot(122) #1줄 2칸, 2번째 칸에 출력
sns.distplot(male_survived['Age'].dropna().values, kde=False, bins=range(0,81,1), 
             color='blue', axlabel='male Age')
sns.distplot(male_not_survived['Age'].dropna().values, kde=False, bins=range(0,81,1), 
             color='red', axlabel='male Age')

#양/음의 상관관계
plt.figure(figsize=(5,6)) 
sns.heatmap(train.drop("PassengerId",axis=1).corr(), square=True, annot=True, vmax=0.6)

#train.info()
#train.corr()
#train.drop("PassengerId",axis=1)

#상관계수 행렬
#train.drop("PassengerId",axis=1).corr()

#Feature Engineering & category <-> numerical
train #891 rows × 12 columns
test #418 rows × 11 columns
train_test_data=[train, test] #리스트 내에 데이터프레임 2개가 요소로 저장

for dataset in train_test_data:
    dataset['Title']=dataset.Name.str.extract(" ([A-Za-z]+)\.")
#호칭의 특징: 공백문자+알파벳+점(.)

test.head()

#3. 퀴즈

#전체 호칭은 행 인덱스로, 성별은 열 인덱스
# Sex   female    male
# Title
# ---------------------
# Capt    0        1
# ...
# Miss    182      0
# ...

#train.groupby(['Title','Sex']).size().unstack().fillna(0)

pd.crosstab(train['Title'], train['Sex'])

train['Title'].value_counts()

for dataset in train_test_data:
    dataset['Title']=dataset['Title'].replace('Mlle','Miss')
    dataset['Title']=dataset['Title'].replace('Ms','Miss')
    dataset['Title']=dataset['Title'].replace('Mme','Mrs')
    dataset['Title']=dataset['Title'].replace('Lady','Mrs')    
    dataset['Title']=dataset['Title'].replace(['Countess','Don', 'Sir', 'Jonkheer',
                                               'Capt','Major','Col','Rev','Dr'],'Other')

pd.crosstab(train['Title'], train['Sex'])

train[['Title', 'Survived']].groupby(['Title']).mean()
train[['Title', 'Survived']].groupby(['Title'], as_index=False).mean()

title_mapping={"Mr":1,
              "Miss":2,
              "Mrs":3,
              "Master":4,
              "Other":5}

for dataset in train_test_data:
    dataset['Title']=dataset['Title'].map(title_mapping)
    dataset['Title']=dataset['Title'].fillna(0)

train.head()
train['Title'].value_counts()

#female -> 1, male -> 0
for dataset in train_test_data:
    dataset['Sex']=dataset['Sex'].map({'female':1, 'male':0})

train.head()
train.info()

train.Embarked.unique() 
train.Embarked.value_counts()

#nan은 모두 'S'로 설정
for dataset in train_test_data:
    dataset['Embarked']=dataset['Embarked'].fillna('S')

#train.head()
#S:0, C:1, Q:2로 변경
for dataset in train_test_data:
    dataset['Embarked']=dataset['Embarked'].map({'S':0, 'C':1, 'Q':2})

#train['Age'].isnull().sum()

#Age 열에 대해 결측값 대체 
#age평균-age표준편차 <=난수발생(Age 결측값 대체)<=age평균+age표준편차

for dataset in train_test_data:
    age_avg=dataset['Age'].mean()
    age_std=dataset['Age'].std()
    age_null_count=dataset['Age'].isnull().sum()
    
    age_null_random_list=np.random.randint(age_avg-age_std, age_avg+age_std, 
                                           size=age_null_count)
    dataset['Age'][np.isnan(dataset['Age'])]=age_null_random_list
#연습문제 (더 좋은 방법을 고민...)

train['Age'].isnull().sum()
test['Age'].isnull().sum()
train.info()

#train['Age'].mean() #29-14 ~ 29+14
#train['Age'].std()

train['Age'].mean()

#train['Age'][np.isnan(train['Age'])]
#train['Age']
train['AgeBand']=pd.cut(train['Age'],5)

train[['AgeBand', 'Survived']].groupby(['AgeBand'],as_index=False).mean()

for dataset in train_test_data:
    dataset.loc[dataset['Age']<=16,'Age']=0
    dataset.loc[(dataset['Age']>16) & (dataset['Age']<=32),'Age']=1
    dataset.loc[(dataset['Age']>32) & (dataset['Age']<=48),'Age']=2
    dataset.loc[(dataset['Age']>48) & (dataset['Age']<=64),'Age']=3
    dataset.loc[(dataset['Age']>64),'Age']=4    

train['Age']

for dataset in train_test_data:
    dataset['Fare']=dataset['Fare'].fillna(train['Fare'].median())
#train과 test의 'Fare'컬럼 값이 nan인 셀 값을 train의 'Fare' 컬럼값의 중앙값으로 설정

train['FareBand']=pd.qcut(train['Fare'],4)
train[['FareBand', 'Survived']].groupby(['FareBand'],as_index=False).mean()
#pd.cut():동일 길이로 나누어서 범주로 만듬
#pd.qcut():동일 데이터 개수로 나누어서 범주로 만듬

train[['FareBand', 'Survived']].groupby(['FareBand'],as_index=False).mean()

train['Fare']

#아래 구문을 2번 이상 실행하면 Fare열 값이 0~3 범위 내로 변경된 상태이므로,
#모두 0으로 변경됨(주의!!!)
for dataset in train_test_data:
    dataset.loc[dataset['Fare']<=7.91,'Fare']=0
    dataset.loc[(dataset['Fare']>7.91) & (dataset['Fare']<=14.454),'Fare']=1
    dataset.loc[(dataset['Fare']>14.454) & (dataset['Fare']<= 31.0),'Fare']=2
    dataset.loc[(dataset['Fare']> 31.0) ,'Fare']=3
    dataset['Fare']=dataset['Fare'].astype(int)

train['Fare']

train.info()

for dataset in train_test_data:
    dataset['FamilySize']=dataset['SibSp']+dataset['Parch']+1

train[['FamilySize', 'Survived']].groupby(['FamilySize'],as_index=False).mean()

#혼자 여행한 경우에 사망률이 높음을 알 수 있음.
for dataset in train_test_data:
    dataset['IsAlone']=0  #혼자가 아님(디폴트)
    dataset.loc[dataset['FamilySize']==1, 'IsAlone']=1
train[['IsAlone', 'Survived']].groupby(['IsAlone'],as_index=False).mean()

features_drop=['Name','SibSp','Parch', 'Ticket','Cabin','FamilySize']
train=train.drop(features_drop, axis=1)
test=test.drop(features_drop, axis=1)
train=train.drop(['PassengerId','AgeBand','FareBand'],axis=1)

train.head()
train.Fare.value_counts()
test.head()
train.columns
test.info()

xTrain=train.drop('Survived', axis=1)
yTrain=train['Survived']
xTest=test.drop('PassengerId', axis=1).copy()
xTrain.shape, yTrain.shape, xTest.shape

from sklearn.tree import DecisionTreeClassifier

model=DecisionTreeClassifier()
# model=DecisionTreeClassifier(max_depth=15, random_state=2020, criterion='entropy')
model.fit(xTrain, yTrain)

round(model.score(xTrain, yTrain)*100, 2)

y_pred_dt=model.predict(xTest)
y_pred_dt

mysubmit=pd.DataFrame({
    'PassengerId':test['PassengerId'],
    'Survived':y_pred_dt
})

mysubmit.to_csv("mysubmit.csv", index=False)

#1. Age열에 대해 더 좋은방법을 고민
#2. cabin결측값을 적절하게 대체 -> 모델링 -> 평가 (score, before: 87%, after:???)
```



참고:[타이타닉 솔루션](https://www.kaggle.com/startupsci/titanic-data-science-solutions)

pd.cut() : 동일 길이(구간) 로 나누어서 범주로 만듦

pd.qcut() : 동일 데이터 개수로 나누어서 범주로 만듦 