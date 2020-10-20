insurance<-read.csv("Data/insurance.csv", stringsAsFactors = TRUE)
str(insurance)

#회귀모델은 작성전에 정규성 확인
#선형회귀는 종속변수가 정규분포를 따르는게 더 잘 fitting

#요약통계
summary(insurance$expenses) #해석해보기 (정규분포를 따르는지)
#중앙값보다 평균값이 크다 => 의료비 분포가 오른쪽으로 꼬리가 긴 분포
hist(insurance$expenses)
### ****
#회귀모델은 모든 특징이 수치 데이터여야만 한다.
### ****

# 3개의 factor 타입 (sex, smoker, region)

table(insurance$sex)
table(insurance$smoker)
table(insurance$region)

# 회귀 모델 만들기 전에 독립변수가 종속변수와 어떤 관계가 있는지? -> 상관분석
cor(insurance[c("age","bmi","children","expenses")], method = "pearson" )
heatmap(cor(insurance[c("age","bmi","children","expenses")], method = "pearson" ), scale = "row")
#나이가 많을수록 비용이 드는 상관관계
# bmi ~ expenses
library(ggplot2)
pairs(insurance[c("age","bmi","children","expenses")]) #산포도 scatter
# install.packages("psych")
library(psych)
pairs.panels(insurance[c("age","bmi","children","expenses")]) 
#산포도 쪽에 타원형으로 강도를 시각화 원에 가까울수록 상관관계가 없다
#빨간색 점이 평균이다.
# 곡선 -> RES curve  

#lm
#종속변수~독립변수
#lm(expenses~독립변수+독립변수+..., data=insurance)
ins_model<-lm(expenses~age+children+bmi+sex+smoker+region, data = insurance)
ins_model<-lm(expenses~., data = insurance) # . 은 expenses를 제외한 모든 컬럼

ins_model

# 예측하려면:
# 예측값 변수 <- (age+children+bmi+sex+smoker+region 데이터들)
# predict(ins_model, newdata = 예측값 변수 )

str(insurance)
temp<-data.frame(age=25, children=2, bmi=30, sex='female', smoker='yes', region="northeast")
temp
# expense 결과 예측 
predict(ins_model, newdata=temp) #29456.97 

mydata<-read.csv("Data/ins_model_test.csv")
mydata
predict(ins_model, newdata=mydata)




# expenses = 256.8* age+475.7*children+..-959.3*regionsouthwest-11941.6

#범주별로 더미 변수화 : 명목형 특징값 -> 수치 
#sex 특징이 female, male 두 개의 범주
# sexmale=1 or 0
# smokeryes = 1 or 0   우리가 이작업을 안해도 내부적으로 처리해준다. (편리)

summary(ins_model)
#Residuals (잔차: 예측에 대한 오차(실제값-예측값)의 요약)
#오차 최고값: -11302
#오차 최대값: 29981(실제값보다 낮게 예측했다는 의미)
#오차의 50%는 q1과 q3사이, -2850.9 ~ 1383.9 달러 사이에 있다.
#오차 = 오류
# 오차가 얼마나 크게났는지 수치로 확인해 보고 싶을경우 

# Coefficients
#Pr(>|t|) : 추정된 계수가 실제 0일 확률 추정치. 
# p 값이 작은 경우 실제 계수가 아닐 가능성이 높다는 것을 의미.
# 특징 변수가 종속변수와 관계가 없을 가능성이 아주 낮다는 의미 
# ***(별) 의 의미는 유의 수준 

# Multiple R-squared(다중 r 제곱값, 결정계수): 모델이 종속변수 값을 얼마만큼
# 잘 설명하는지를 측정한 값. 1에 가까울 수록 모델이 완벽하게 종속변수를 설명
# 0.7509 => 모델이 종속변수 변화량의 약 75%를 설명하고 있다.

#선형회귀 -> 연속형 값 예측
#로지스틱회귀 -> 선형회귀 -> 연속형 값 예측 -> 특수한 함수 ->
#분류 결과 (0 또는 1, yes or no, 0~9,...)
# 연속형 값 예측 (선형회귀), 분류결과(로지스틱 회귀)
#특수함수를 sigmoid에 접하면 0~1 사이의 값으로 나오는데 여기서 0.5이상은 1 아니면 0 이런식으로 0또는 1로 나타낼수 있다.


#신경망 (로지스틱 회귀 ( 너무 단순, 간단한 모델 적절) 방식의 한계점을 개선)
#신경망을 여러 겹으로 쌓으면 딥러닝 

#주성분분석(pca, 차원축소) #차원을 내리는 알고리즘
#주로 데이터 전처리 단계에서 사용함

#전파? 신호(가중치 변수값)가 전달 (방향: 좌->우 => 순전파, 우<-좌 => 역전파)
# 딥러닝은 순천파/역전파가 번가아가며 수행되는 학습 방법

#손실함수(loss/cost function) 
# 손실함수의 결과를 바탕으로 오차를 최소화하는 과정
# (GD알고리즘 : COST의 최소값에 해당되는 위치(w,b)를 찾는 것)


