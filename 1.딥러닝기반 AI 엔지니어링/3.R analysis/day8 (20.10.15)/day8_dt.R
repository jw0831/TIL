# default 채무불이행 (yes/no)? 분류기
credit<-read.csv("Data/credit.csv")
str(credit)

table(credit$checking_balance) #계좌 잔고
table(credit$savings_balance) #저축 계좌 잔고

summary(credit$months_loan_duration)
#대출금 4개월~72개월의 기간이 있다는 것을 확인할 수 있다.

summary(credit$amount)
#대출금: 250~18424, 중앙값: 2320, 평균: 3271 확인 

table(credit$default) #약 30%정도는 채무불이행을 하였다고 볼수 있다.
#은행 입장에서는 파산될 수 있다.

# 훈련: 90%, 테스트 : 10%
#랜덤 샘플링
set.seed(123)
sample(10,5) #1~10까지의 숫자중 5개의 난수 생성
#모델일 갱신하기 전과 후의 객관적 비교를 하기위해서 난수를 동일하게 생성
trainSample<-sample(1000,900)
str(trainSample)

str(credit) #data 1000건, 변수17건
creditTrain<-credit[trainSample,] #900개의 랜덤 컬럼이 추출된다.
creditTest<-credit[-trainSample,] #100개 : 총 1000개의 데이터에서 나머지

table(creditTrain$default)
table(creditTest$default)

#의사결정트리 
# install.packages("C50")
library(C50)
str(credit) #x,y data 구분을 해야한다. x: checking balance~phone, y: default column
creditTrain$default<-factor(creditTrain$default)
str(creditTrain) #구조가 factor 로 바뀐것 확인 
help(C5.0)
creditTrain[-17] #default 컬럼을 제외한 나머지 컬럼들 추출
model<-C5.0(creditTrain[-17], creditTrain$default, trials = 50)
model

creditPred<-predict(model, creditTest)

library(gmodels)
CrossTable(creditTest$default, creditPred, prop.chisq = FALSE, prop.c = FALSE, prop.r = FALSE,
           dnn=c("act default", "pred default"))
