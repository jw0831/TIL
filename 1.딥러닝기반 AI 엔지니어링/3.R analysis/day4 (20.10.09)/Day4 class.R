# 1차 데이터 분석 프로젝트 고민하기
# 1차 데이터 분석 프로젝트 진행 (조원 : 4명 정도) -> 발표
# 추천시스템, 시각화 (분석), 사회 이슈, 판매(번들 상품), 고객 분류 등등
# data.go.kr, uci.edu, ... 크롤링

# 2차 텍스트 분류 프로젝트 진행 예정 (10월말~11월 초) 
# - 머신러닝 진행 예정
# 자연어 처리 

library(dplyr)
library(ggplot2)
# kmeans를 이용한 클러스터링(snsdata)

snsData<-read.csv("day4 (20.10.09)/snsdata.csv")
teens<-snsData
str(teens)
#기업에서는 10대20대들의 언어를 분석해서 제품을 판매할때 자료로 사용한다.

table(teens$gender) #value_counts와 같다
#테이블 함수에서 NA값은 별도의 범주로 취급하지 않고 제외해서 보여준다. ㅜㅜ 

table(teens$gender, useNA = "ifany") #NA값도 범주로 취급, NA가 많은것을 확인 ^^ 
#여학생이 남학생보다 4배는 많다.. 여학생이 sns를 많이 사용 하는것을 확인 
table(teens$gradyear) #졸업연도

table(teens$age) #너무 더럽게 많으니까 소수때문에, newAge변수를 만들어서 깨끗하게 만들자.
table(teens$age, useNA = "ifany") # 너무 더럽게 많아서 안보인다.
summary(teens$age) #기술통계(describe)를 사용해서 NA를 확인 
#문제점 Min. 이 3살? Max가107세? 극단치가 있으므로 처리 필요

# 결측치를 처리하기 에매한 경우! 
# 범주형 데이터에 대한 결측치는 별도의 범주로 취급하자
str(teens)
# Manage NA for age
# (나이에대한 개념이 있어서 13을 사용 가능)
teens$age<-ifelse(teens$age>=13 & teens$age<20, teens$age, NA) #stats or boxplot 사용 
summary(teens$age)
###########################################################################################
teens$female<-ifelse(teens$gender=="F", 1, 0) #아니면 남성(NA는 제외)
table(teens$female, useNA="ifany")
#범주 : F or M 만 보이게 하고 싶다. (useNA="ifany) 옵션을 사용해도..어떻게?
teens$female<-ifelse(teens$gender=="F" & !is.na(teens$gender), 1, 0)
# F이면서 NA가 아니면 1, 그렇지 않으면 남성 0
table(teens$female, useNA="ifany")
#!is.na(teens$gender) 를 포함함으로써 위 구문을 사용해도 NA가 안보인다. 미포함 따로 제외할 번거로움 사라짐

# 남자 
teens$male<-ifelse(teens$gender=="M" & !is.na(teens$gender), 1, 0)
############################################################################################
teens$no_gender<-ifelse(is.na(teens$gender), 1, 0) #gender가 NA이면 1 아니면 0
table(teens$no_gender)
# teens$no_gender

#범주 : F or M
mean(teens$age) #NA가 포함되면 계산이 NA로 나온다.
mean(teens$age, na.rm=TRUE)

#졸업연도 정보 -> 나이 유추 


#졸업연도에 따른 나이의 평균 
#졸업연도 조사, 각 졸업연도별 나이 평균
teens 
# %>% group_by(gradyear)

table(teens$gradyear)
boxplot(teens$gradyear)$stats #이상치 없음 

teens %>% filter(!is.na(age)) %>% 
  select(age, gradyear) %>% 
  group_by(gradyear) %>% 
  summarise(mean_gradAge=mean(age))
#### 다른방법 ####
help("aggregate") #총계/집합
# formula	
# a formula, such as y ~ x or cbind(y1, y2) ~ x1 + x2, 
# where the y variables are numeric data to be split into 
# groups according to the grouping x variables (usually factors).
##### aggregate(data=(컬럼), y(나이)~x(졸업연도), 집계함수(평균), na.rm=TRUE)
##### x를 기준으로 y에 대해 집계함수를 수행

aggregate(data=teens, age~gradyear, mean, na.rm=TRUE)

# 나이가 NA인 경우
#1. 학생의 졸업연도를 확인
#2. 졸업연도에 해당되는 age열 값을 가져와서 대체 
# NA를 제외하면 좋겠지만, 유의미한 데이터들이 사라진다
###############################################
x<-1:10
x #vector structure length=10
mean(x)
ave(x) #numpy 처럼 작동한다.

mygroup<-rep(1:2, c(3,7)) #1이 3번, 2가 7번 반복 
mygroup #두 그룹
ave(x, mygroup, FUN = mean) #첫번째 인수에는 데이터가, 두번째 인수에는 그룹
# (1+2+3)/3 = 2
#          2  2  2  7  7  7  7  7  7  7
# x        1  2  3  4  5  6  7  8  9 10   (vector)
# mygroup  1  1  1  2  2  2  2  2  2  2   (vector)

ave(x, mygroup, FUN = sum)
ave(x, mygroup, FUN = function(a)sum(a^2))
# 1^2+2^2+3^2 = 14
# 4^2+5^2+6^2+7^2+8^2+9^2+10^2= 371
# 14  14  14 371 371 371 371 371 371 371
# 이걸 잘 사용하면 그룹별로 구하는 것을 group_by대체용으로 사용할 수 있다. 
###############################################
#년도 그룹별로 나이 평균 계산 한줄코드 
#function(x) 에 람다처럼 x는 teen$age값이 온다. 그런데 그룹별로 
ave(teens$age, teens$gradyear, FUN = function(x)mean(x, na.rm=TRUE))

ave_age<-ave(teens$age, teens$gradyear, FUN = function(x)mean(x, na.rm=TRUE))
teens$age<-ifelse(is.na(teens$age), ave_age, teens$age)
summary(teens$age) #이미 위에서 극단치는 제거함 

######
teens[5:40] #sns keywords
class(teens[5:40]) #3만행, 36열


#      축구  농구
# 만번 0번   1번
# 만번 1번   0번
# 유클리디안거리로 따지면 
# 축구는 1빼기 만번 9999^2
# 농구는 1-0번 1번 1^2 
# 이렇게되서 숫자가 너무 커져버리므로 표준화가 필요하다. (outlier 제거)
# 정규화는 데이터의 범위를 0 아니면 1만 갖도록 하게끔 하려고 하는것 이산적으로 할려는 경우

interests<-teens[5:40]
#표준화 (scale)
lapply(interests, scale) #lapply 는 파이썬의 apply와 비슷하다.
class(lapply(interests, scale)) #list 자료구조이다.
#표준화 (mu(평균)=0, sigma=1(표준편차)) mu가 중요! centers 해석 보기 (아래)
interests_z<-as.data.frame(lapply(interests, scale)) #DataFrame 자료구조로 바꿈
set.seed(12345) #동일한 난수발생
teen_clusters<-kmeans(interests_z, 5) #nstart 를 높여가며 확인해보기!
# sqrt(40/2) #4.472136 k값을 5정도로 하면 좋네 
teen_clusters

teen_clusters$size 
# 4161 21580   578  2663  1018
teen_clusters$centers #각 클러스터에 대한 중심점의 좌표(36차원)
#ex) 1번째 클러스터의 중심점: (0.0121330, 0.09171404, ...,-0.05735705)
# -> basketball 행 1 의 평균이 0.0121330 (전체 5개의 그룹에 대해서 조금 언급)
# 1번 : 운동 (좋지도 싫지도 / 보통), 교회(종교), 음악, 쇼핑, 외모 관심 많음
# 2번 : 운동 싫어함, 별 관심이 없음, 내성적인 아이들.. 
# 3번 : 운동 (보통), 외모 관심, 섹쉬함
# 4번 : 운동 매우 좋아함 
# 5번 : 운동 조금 좋아함 / 문제아 많음(위험), 멋을 많이 부림, 외모, 노는것 좋아함

teen_clusters$cluster
teens$cluster<-teen_clusters$cluster

teens[1:10, c("cluster","gender","age","friends")]

aggregate(data=teens, age ~ cluster, mean)
#클러스터 단위로 나이에 대한 평균을 구해라 
aggregate(data=teens, male ~ cluster, mean)
aggregate(data=teens, female ~ cluster, mean)
aggregate(data=teens, friends ~ cluster, mean)


# 분석은 끝냈고, 새로운 학생이 전학을 옴 -> sns data -> cluster? 
####data<-as.data.frame(snsData) #snsData에는 36개 컬럼에 대한 값이 저장된 상태 
#이 학생 데이터를 갖고 예측을 해보는건데 어떻게 하냐면, 
#kmeans작업을 하는데 scale을 했었으니까 이 학생도 scale 하고 
####data_z<-scale(data) 이렇게 만들어준다 
# teen_clusters<-kmeans(interests_z, 5) 위에서 이렇게 만듦
help(train) #함수 를 통해서 학생이 어느 군집에 속하는지 알아보면된다
help(dist) # 두점 사이의 거리를 구해주는 함수 -> Arguments->method: 	
# the distance measure to be used. This must be one of 
# "euclidean", "maximum", "manhattan", "canberra", "binary" or "minkowski". 
# Any unambiguous substring can be given.
# default = euclidean distance
# usage:
# dist(x, method = "euclidean", diag = FALSE, upper = FALSE, p = 2)
#      x: a numeric matrix, data frame or "dist" object.


#dist
#cosine_sim 코사인 유사도
#### 예시 ####
# install.packages("proxy")
library(proxy)
# 매우중요한 코드 문서 분류할때 많이 사용한다. 
# 문서번호 : d1, d2, d3 / 
# c(단어등장횟수 벡터) ==> c(sky, cloud, rain) => c(1, 0, 2)
d1<-c(1,0,5)
d2<-c(4,7,3)
d3<-c(40,70,30)
# 그냥 벡터가지고는 작업을 못한다. 연결해야함 
rbind(d1, d2, d3) # matrix 자료구조  (행렬)
class(rbind(d1, d2, d3))# "matrix" "array" 
doc<-rbind(d1, d2, d3)
doc
#컬럼에 대한 이름 주는법
colnames(doc)<-c("sky", "cloud", "rain")
doc
#코사인 유사도 0도일때가 1 (가장높다)/90도가 0 (가장 낮다)
#함수가 계산해준다.
dist(doc, method="cosine") # 코사인거리 = 1-코사인유사도
dist(doc, method="euclidean") # 유클리디안 거리 = 1-유클리디안

#############
######### plot 해봄 #####
library(factoextra)
teen_clusters <- kmeans(interests_z, 5, nstart = 25) #이건 모든 컬럼(35개)를 클러스터링 한거다
interests_z<-as.data.frame(lapply(interests, scale))
# K-means clusters showing the group of each individuals
teen_clusters$cluster
fviz_cluster(teen_clusters, data = interests_z,
             palette = c("npg"),
             geom = "point",
             ellipse.type = "convex",
             ggtheme = theme_bw()
)

# 질문: 왜 저렇게 한곳으로 뭉쳐서 보이는가 궁금했었는데요,
# 그 이유가 컬럼별로 나누어서 시각화를 하지않았기에 군집들이 뭉친게 맞나 해서요; (NO)
# 
# Ans:
# 시각화 도구들이 잘 알다시피 3차원을 못넘어가요 다차원은 시각화를 할 수 없어요 
# 그래서 지금 factoextra를 쓴것 같은데
# 
# 다차원 data를 pca라는 차원 축소 기법을 이용해서 차원 축소한 다음 
# 가장 의미가 있는 2개 차원을 추출해서 화면에 표시한거에요
# dim1 dim2 두 개의 축이 전체 데이터의 4.8% + 9.2%를 설명하고 있네요 보니까
# pca를 안배워서결론적으로겹쳐진것처럼 보인다 라고 생각하면 될것 같아요

# 36 차원 ->  pca  -> 차원축소 -> 가장 의미있는 2개 축 추출
# -> 시각화 이렇게 한거를 저에게 보여준거예요


# 선생님 위에 35개의 컬럼에대한 군집을 시각화를 하려면 각 컬럼별로 하는게 적절한가요?
# 강사 박길식에서 나에게: (비공개로) (3:48 오후)
# 예 의미 있는 컬럼별로 나누어서 시각화하면 될것 같아요


##########################################################################################################




