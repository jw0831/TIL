iris
str(iris)

iris3 #꽃의 종류별로 나온다.
#리스트: 다양한 타입의 자료들이 저장될 수 있는 자료구조


#k-means 수업
y<-rnorm(100) #평균:0, 표준편차:1, 정규분포 난수
hist(y)

x=matrix(rnorm(100), nrow=5) #난수 100개 생성 -> 5행*20열

help(dist) # 두점 사이의 거리를 구해주는 함수 -> Arguments->method: 	
# the distance measure to be used. This must be one of 
# "euclidean", "maximum", "manhattan", "canberra", "binary" or "minkowski". 
# Any unambiguous substring can be given.
# default = euclidean distance
# usage:
# dist(x, method = "euclidean", diag = FALSE, upper = FALSE, p = 2)
#      x: a numeric matrix, data frame or "dist" object.
dist(x, method = "euclidean", diag = FALSE, upper = FALSE, p = 2)
# 1        2        3        4
# 2 8.037706                           
# 3 6.962919 5.255825                  
# 4 8.244698 5.533628 4.685244         
# 5 7.881960 6.839627 6.392738 5.567093
# 20차원에 해당되는 데이터에서 1번째, 2번째 데이터간의 유클리디안 거리 8.037706
dist(x, method = "manhattan", diag = FALSE, upper = FALSE, p = 2)
# 1        2        3        4
# 2 32.86493                           
# 3 24.82460 20.55810                  
# 4 29.26473 19.72289 17.96805         
# 5 25.49924 25.49841 23.41469 19.65032

################################################################################################
# 클러스터링(군집화) using K-means algorithm
################################################################################################
data(iris) #data함수 : 데이터를 로드
head(iris)
summary(iris)

iris[,-5]
help(kmeans) #Arguments: read about "x", "centers"
#k 값을 얼마를 주어야한다? 우리는 iris에서 3가지 종류가 있는것을 아니까 k=3이겠지만
# 모르는 경우는? 그럼 몇개를 클러스터링 해야하나?
# 방법: 1.엘보우(elbow)기법 2.k=sqrt(n/2)

# video check here

kmeans.iris<-kmeans(iris[,-5], 3)
kmeans.iris$centers
kmeans.iris$cluster
iris[,5]
# A vector of integers (from 1:k) indicating the cluster to which each point is allocated.
# 각각의 데이터에 대해서 어떤 그룹에 속하는지 나타냄 1~3
table(iris[,5], kmeans.iris$cluster)
###
kmeans.iris<-kmeans(iris[,-5], 3, nstart = 100) #100번 반복해서 시행해서 예측력이 올라감
table(iris[,5], kmeans.iris$cluster)
kmeans.iris

# Within cluster sum of squares by cluster:
#   [1] 15.15100 39.82097 23.87947
# 이 값이 작을수록 좋은거다. 클러스터 안에 거리, 데이터들 간에 거리가 적다는것 응집력good
data(iris)
set.seed(123)

kmeans10.iris<-kmeans(iris[,-5], 3, nstart = 10) #nstart 값이 클수록 거리의 합이 적게 나와야 한다.
round(sum(kmeans10.iris$withinss),2) #78.85

kmeans.iris<-kmeans(iris[,-5], 3)
round(sum(kmeans.iris$withinss),2) #더 크게 나와야함

##시각화
ggplot(data=iris, aes(x=Petal.Length, y=Petal.Width, colour=Species))+
  geom_point(shape=19, size=4)+
  ggtitle("iris data")

iris_plot<-ggplot(data=iris, aes(x=Petal.Length, y=Petal.Width, colour=Species))+
  geom_point(shape=19, size=4)+
  ggtitle("iris data")

iris_plot2<-iris_plot+
  annotate("text", x=1.5, y=0.7, label="Setosa", size=5)+#annotate: 표식 그림위에
  annotate("text", x=3.5, y=1.5, label="Verisicolor", size=5)+
  annotate("text", x=6, y=2.7, label="Virginica", size=5)

iris_plot2

iris_k_means<-kmeans(iris[ ,c("Petal.Length","Petal.Width")],3)
iris_k_means

iris_k_means$cluster
iris_k_means$totss
iris_k_means$withinss #intracluster distances are minimized
iris_k_means$betweenss #Intercluster distances are maximized

prop.table(iris_k_means$size) #prop 비율이 나온다.

iris_k_means_centers<-iris_k_means$centers
iris_k_means_centers
# 중심 좌표를 검정색 점으로 표현
iris_plot2+
  annotate("point", x=5.62, y=2.04, size=5, color="black")+
  annotate("point", x=4.29, y=1.35, size=5, color="black")+
  annotate("point", x=1.46, y=0.24, size=5, color="black")
####
################################################################################################
# https://uc-r.github.io/kmeans_clustering
# library(ggpubr)
library(factoextra)
fviz_cluster(kmeans.iris, data = iris[,-5])
# # Compute k-means with k = 3
# set.seed(123) #동일한 난수 발생 
res_km <- kmeans(scale(iris[, -5]), 3, nstart = 25)
# K-means clusters showing the group of each individuals
res.km$cluster
fviz_cluster(res_km, data = iris[, -5],
             palette = c("#2E9FDF", "#00AFBB", "#E7B800"),
             geom = "point",
             ellipse.type = "convex",
             ggtheme = theme_bw()
)
# # https://www.datanovia.com/en/blog/k-means-clustering-visualization-in-r-step-by-step-guide/
################################################################################################
# 거리에 영향을 미치지 않으려면 표준화 작업이 필요하다!!! 
# 고려사항: 표준화 작업! (데이터에따라 필요할수도 않을수도 있다.)
#범주별 데이터 개수가 비슷한 경우 -> 클러스터링 잘 됨
#범주별 데이터 개수 차이가 심한 경우 -> 클러스터링 잘 되지 않음
# 차이가 심한 경우 (고려사항) => 한쪽의 데이터를 (증식 또는 감소) balance를 맞춰주는법
# 아래 사이트를 참고하면 선생님 강의와 유사한 설명을 볼 수 있다. (DBSCAN)
# https://ssoondata.tistory.com/28

z_iris<-scale(iris[,-5])
z_iris #표준화

################################################################################################
# 연습문제

# iris 컬럼 2개, 3개, 4개 => 클러스터링 수행
data(iris)
set.seed(123)
# kmeans.iris<-kmeans(scale(iris[,-5]), 2, nstart = 25)
# round(sum(res_km$withinss),2)
############# 2개
res_km2 <- kmeans(scale(iris[, -5]), 2, nstart = 25)
round(sum(res_km2$withinss),2) # 220.88
# K-means clusters showing the group of each individuals
res_km2$cluster
fviz_cluster(res_km2, data = iris[, -5],
             palette = c("#2E9FDF", "#00AFBB", "#E7B800"),
             geom = "point",
             ellipse.type = "convex",
             ggtheme = theme_bw()
)
table(iris[,5], res_km2$cluster)
############# 3개
res_km3 <- kmeans(scale(iris[, -5]), 3, nstart = 25)
round(sum(res_km3$withinss),3) # 138.888
# K-means clusters showing the group of each individuals
res_km3$cluster
fviz_cluster(res_km3, data = iris[, -5],
             palette = c("#2E9FDF", "#00AFBB", "#E7B800"),
             geom = "point",
             ellipse.type = "convex",
             ggtheme = theme_bw()
)
table(iris[,5], res_km3$cluster)
############# 4개
res_km4 <- kmeans(scale(iris[, -5]), 4, nstart = 25)
round(sum(res_km4$withinss),4) # 113.3319
# K-means clusters showing the group of each individuals
res_km4$cluster
fviz_cluster(res_km4, data = iris[, -5],
             palette = "npg",
             geom = "point",
             ellipse.type = "convex",
             ggtheme = theme_bw()
)
table(iris[,5], res_km4$cluster)





################################################################################################
# http://archive.ics.uci.edu/ml/datasets/Wine/
read.csv("day3 (20.10.08)/wine_dataset/wine.data")
# read.csv("day3 (20.10.08)/wine_dataset/Index")
# read.csv("day3 (20.10.08)/wine_dataset/wine.names")







