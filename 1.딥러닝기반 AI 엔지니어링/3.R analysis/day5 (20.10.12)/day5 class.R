member<-data.frame(spent=c(10,1,1,17,4,6,1,15,22,3,0,3,7,0,2),
           time=c(15,2,10,7,5,7,1,10,18,3,1,3,7,10,2))
member
#member를 3개의 클러스터로 구성
res<-kmeans(member, 3)
res

# install.packages("fpc")
library(fpc)

plotcluster(member, res$cluster, color=TRUE)

library(factoextra)
# K-means clusters showing the group of each individuals
teen_clusters$cluster
fviz_cluster(res, data = member,
             palette = c("npg"),
             geom = "point",
             ellipse.type = "convex",
             ggtheme = theme_bw()
)

res$cluster #각 데이터가 소속된 클러스터
res$centers #각 클러스터의 중심 좌표
res$totss #각 클러스터와 데이터간 거리 제곱의 합의 전체 합 1028
res$withinss #응집력
res$tot.withinss #응집력의 총합 (작을수록 좋다)
res$betweenss #클러스터간 떨어져 있는 거리(크면 클수록 좋다)
res$size #클러스터에 소속된 데이터의 개수
res$iter #몇 번 반복 해서 클러스터를 찾았는가? 

#인사이트 도출 => 클러스터에 대한 그룹별 연산이 필요
#예시:
member$cluster<-res$cluster #맴버에 클러스터 컬럼을 생성
member
#각각의 그룹별 최대 spent 값을 찾아내고 싶다.
aggregate(data=member, spent~cluster, max)

# install.packages("NbClust")
# 이것을 사용해서 적절한 kmeans의 k개수를 찾아볼 수 있다.
library(NbClust)
nb<-NbClust(member[,1:2], min.nc = 2, max.nc=5, method='kmeans') #According to the majority rule, the best number of clusters is  2 
NbClust(iris[,1:4], min.nc = 2, max.nc=5, method='kmeans') #음집도(좌)와 분리도(우)에 대해서 보여준다
#conclusion: According to the majority rule, the best number of clusters is  2 

nb$Best.partition
###### exercise
data(iris)
head(iris)
iris[,-5]
irisScale<-scale(iris[,-5])

k.max=10 #변수 생성
wss<-rep(NA, k.max)
nClust<-list()

for(i in 1:k.max){
  irisRes=kmeans(irisScale, i) #k값을 바꿔가며 kmeans를 10번수행 
  wss[i]=irisRes$tot.withinss
  nClust[[i]]=irisRes$size #리스트인경우 리스트요소를 참조할때 대괄호 2개 사용해야한다.
  res$tot.withinss #응집력의 총합(작으면 좋다.) 이것을 위주로 본다.
  #res$betweenss #클러스터간 떨어져 있는 거리(크면 클수록 좋다) -이건 좀 무시하는편
}
wss
nClust #당연히 클러스터가 많아질수록 응집력이 떨어지는게 보이지만 응집간의 차이를 보는게 중요! 서로 빼서 가장 많이 떨어진 구간을 찾아야함
plot(1:k.max,wss, type='b')#대략 3정도가 적당해 보인다

fitk<-kmeans(irisScale, 3)
str(fitk)

plot(iris, col=fitk$cluster)

table(predicted=fitk$cluster, Actual=iris$Species) #정확도 조사
1-(11+14)/(50+39+36+25)
#전체 케이스 150 개 iris => 150 obs. of 5 variables
#11+14=25 -> 오류값?도 두개 더한 값이 25임!
################################################################################################
# h clustering
################################################################################################
set.seed(12)
a<-matrix(rnorm(100), nrow=5) #난수생성 #5행 20열, 표준 정규분포
#5 건의 데이터 (행1개당 1개의 데이터로 보면된다.) 몇차원? 20차원 (열의 개수)

#5개의 데이터를 h-clustering 알고리즘 -> 군집화(1~5)
# hclust(d(거리행렬), method = 거리구하는방법) 여러가지 방법들이 있다. 
# 5데이터에 대해서 각각의 거리행렬 dist함수
dist(a) #유클리디안 거리
# help(hclust) method의 single(최단거리끼리), complete(최장거리끼리)
h<-hclust(dist(a), method = "single") #가장 가까운 거리
h<-hclust(dist(a), method = "complete") #가장 먼 거리
h<-hclust(dist(a), method = "average") #클러스터 평균(극단치영향을 받음) 간 거리
h<-hclust(dist(a), method = "centroid")

plot(h)
# 1,2,3,4,5 거리행렬
# (4,5),2,3,1 거리행렬 (가장 가까운거리)
# (4,5,2),3,1 거리행렬
# (4,5,2,3),1 거리행렬
# (4,5,2,3,1)



################################################################################################
# knn (k-nearest neighbour):거리 기반으로 유사도 측정
# 레이블이 없는 데이터들에 대해 거리 기반으로 클래스를 할당
# 이웃에대한 데이터들을 기반으로 해당데이터를 역으로 알아내는방법
# 활용: 영화, 음악 추천시스템
# 패턴 인식 (얼굴, 글자, 사용가능한 유전데이터 등등)

# 장점: 단순, 효율, 데이터 분포를 가정하지 않는다, 빠르다
# 단점(한계점): 적절한 k 선택 (모든 점들이 숫자로 표현)

# knn?(설명): 가장 가까운 거리에 있는 k개 데이터를 추출 -> 대상 데이터에 대한 레이블링 수행

wbcd<-read.csv('day5 (20.10.12)/wisc_bc_data.csv')
str(wbcd) 
#diagnosis 는 chr 로 나온다. 범주형은 순서가 있는게 있고 없는게 있다. 그런데 diagnosis 같은
# 경우는 카테고리형(R=factor형)으로 읽는게 좋다. B또는 M이기 때문.
wbcd<-read.csv('day5 (20.10.12)/wisc_bc_data.csv', stringsAsFactors = TRUE) #(default)=False
#stringAsFactors = TRUE : 범주(Factor)형으로 문자 데이터를 읽겠습니까? TRUE
#단점, 따로 안된다. 
#예) 문자컬럼 : 5개, 4개(범주), 1개(문자) 일경우 5개를 모두 범주로 읽고 나머지 1개는 문자타입으로 변환.
str(wbcd) #diagnosis 가 factor로 바뀐것을 볼 수 있다.
#따로 타입을 변환하고 싶을때:
wbcd<-read.csv('day5 (20.10.12)/wisc_bc_data.csv')
wbcd$diagnosis<-factor(wbcd$diagnosis, levels=c("B","M"),
       labels=c("Benign", "Malignant")) 
str(wbcd)
wbcd$diagnosis
table(wbcd$diagnosis)
round(prop.table(table(wbcd$diagnosis))*100,1) #종양 양성 악성 percentage

wbcd[c("radius_mean","area_mean","smoothness_mean")] 
# 이 특징을보면서 knn값을 적용할수 있는지 살펴보아야함 
# (거리 계산이 되어야 하는데 area_mean을 보면 표준화 또는 정규화가 필요해보임) 이런것 확인 꼭 필요 
#이런식의 확인보다 summary가 편리하다.
summary(wbcd[c("radius_mean","area_mean","smoothness_mean")])
#area의 최대와 최소가 엄청 차이나는것을 볼 수 있다.
#정규화: normalize() 함수  값을 0~1 사이로 만들어준다.
#수식:      0 <= (각 데이터 -최소값)/최대값-최소값 <= 1

wbcd<-wbcd[-1] #1번열 제거(id)
head(wbcd)
####  함수 만들기  ####
normalize<-function(x){
  return ((x-min(x))/(max(x)-min(x)))
}
normalize(c(1,2,3,4,5))
######################## id가 1번이었는데 제거했으므로 1번열이 diagnosis열
wbcd_n<-as.data.frame(lapply(wbcd[2:31], normalize)) #수치 데이터 정규화 (list 구조 -> dataFrame으로 변환)
str(wbcd_n)
wbcd_train<-wbcd_n[1:469,] #트레이닝 데이터
wbcd_test<-wbcd_n[470:569,] #테스트 데이터
#diagnosis 열
wbcd_train_labels<-wbcd[1:469, 1] # 정답 
wbcd_test_labels<-wbcd[470:569, 1] # 정답

#1) 트레이닝 입력 데이터와 정답
#2) 모델링 (knn)
#3) 모델에 테스트 입력 데이터 -> 예측/분류 결과
library(class)
wbcd_test_pred<-knn(train=wbcd_train, test=wbcd_test, cl = wbcd_train_labels, k=21)
wbcd_test_pred

# install.packages("gmodels")
library(gmodels)
CrossTable(x=wbcd_test_labels, y=wbcd_test_pred)

#표준화 -> 종양의 큰값 등이 중요한 지표이므로
#정규화 보다는 큰 종양에 대한 정보를 담는게 중요하다는 뜻
wbcd_z<-as.data.frame(scale(wbcd[-1])) #표준화
wbcd_train<-wbcd_z[1:469,] #트레이닝 데이터
wbcd_test<-wbcd_z[470:569,] #테스트 데이터
#diagnosis 열
wbcd_train_labels<-wbcd[1:469, 1] # 정답 
wbcd_test_labels<-wbcd[470:569, 1] # 정답

wbcd_test_pred<-knn(train=wbcd_train, test=wbcd_test, cl = wbcd_train_labels, k=21)
wbcd_test_pred
CrossTable(x=wbcd_test_labels, y=wbcd_test_pred)

# for 문 사용해서 k 값을 5, 11, 15, 27 넣어보기
ki<-c(5,11,15,27)

for(i in ki){
  CrossTable(x=wbcd_test_labels, y=knn(train=wbcd_train, test=wbcd_test, cl = wbcd_train_labels, k=i))
}
# CrossTable(x=wbcd_test_labels, y=knn(train=wbcd_train, test=wbcd_test, cl = wbcd_train_labels, k=5))



######### 표준화+ 정규화 ## 종양의 크기가 다양해서 이상치 제거는 무의미할듯 굳이 이렇게 할 필요가 없다.
wbcd_z_n<-as.data.frame(lapply(scale(wbcd[-1]), normalize)) 
wbcd_train<-wbcd_z_n[1:469,] #트레이닝 데이터
wbcd_test<-wbcd_z_n[470:569,] #테스트 데이터
#diagnosis 열
wbcd_train_labels<-wbcd[1:469, 1] # 정답 
wbcd_test_labels<-wbcd[470:569, 1] # 정답

wbcd_test_pred<-knn(train=wbcd_train, test=wbcd_test, cl = wbcd_train_labels, k=21)
wbcd_test_pred
CrossTable(x=wbcd_test_labels, y=wbcd_test_pred)

predict.kmeans <-function(x,newdata){
  
}
data(iris)
mydata<-iris
m<-mydata[1:4]
train<-head(m,100)
xNew<-head(m,10)
xNew

norm_eucl<-function(train){
  # train연산
  train/apply(train,1,function(x)sum(x^2)^.5) #margin = 1일경우 행단위 함수적용
}
m_norm<-norm_eucl(train)
m_norm

#연습문제: 임의의 데이터 입력 -> kmeans 클러스터 -> 클러스터를 할당 구현
# 입력데이터 <-> 클러스터 중심 1,2,3
# 데이터차원:30차원 
# 클러스터: c1, c2, c3
# c1=(0.5, 0.7, ..., 0.4)
# c2=(1.5, 0.7, ..., 0.4)
# c3=(1.5, 0.7, ..., 0.4)
# # 분류할 데이터 (newData)
# newData(0.5, 0.2, ..., 0.1) 이것과 각각의 클러스터를 계산해야함


