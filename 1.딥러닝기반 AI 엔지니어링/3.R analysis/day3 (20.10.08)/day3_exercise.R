library(factoextra)

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
data(iris)
set.seed(123)

iris_k_means<-kmeans(iris[ ,c("Petal.Length","Petal.Width")],2, nstart = 25)
iris_k_means$centers
iris[,c("Petal.Length","Petal.Width")]
iris[,-5]
iris_k_means$

round(sum(iris_k_means$withinss),2) #86.39
##시각화
ggplot(data=iris, aes(x=Petal.Length, y=Petal.Width, colour="npg"))+
  geom_point(shape=19, size=4)+
  ggtitle("iris data")

iris_plot<-ggplot(data=iris[,-5], aes(x=Petal.Length, y=Petal.Width, colour="npg"))+
  geom_point(shape=19, size=4)+
  ggtitle("iris data")

# iris_plot_2clusters<-iris_plot+
iris_plot2<-iris_plot+
  annotate("text", x=1.5, y=0.76, label="1", size=5)+#annotate: 표식 그림위에
  annotate("text", x=4.93, y=2.2, label="2", size=5)
iris_plot2
iris_plot2+
  annotate("point", x=1.5, y=0.26, size=5, color="black")+
  annotate("point", x=4.93, y=1.7, size=5, color="black")
################################################################################################
##### 4개 군집
data(iris)
set.seed(123)

iris_k_means<-kmeans(iris[ ,c("Petal.Length","Petal.Width")],4, nstart = 25)
iris_k_means$centers
# Petal.Length Petal.Width
# 1     4.769231    1.607692
# 2     5.802857    2.111429
# 3     3.903846    1.192308
# 4     1.462000    0.246000
  
round(sum(iris_k_means$withinss),2) #19.47
##시각화
ggplot(data=iris, aes(x=Petal.Length, y=Petal.Width, colour=Species))+
  geom_point(shape=19, size=4)+
  ggtitle("iris data")

iris_plot<-ggplot(data=iris[,-5], aes(x=Petal.Length, y=Petal.Width, colour="npg"))+
  geom_point(shape=19, size=4)+
  ggtitle("iris data")

# iris_plot_2clusters<-iris_plot+
iris_plot2<-iris_plot+
  annotate("text", x=1.5, y=0.76, label="1", size=5)+#annotate: 표식 그림위에
  annotate("text", x=3.9, y=1.7, label="2", size=5)+
  annotate("text", x=5.8, y=2.6, label="4", size=5)+
  annotate("text", x=4.7, y=2.1, label="3", size=5)+
  annotate("point", x=1.5, y=0.24, size=5, color="black")+
  annotate("point", x=3.9, y=1.2, size=5, color="black")+
  annotate("point", x=5.8, y=2.1, size=5, color="black")+
  annotate("point", x=4.7, y=1.6, size=5, color="black")
iris_plot2
################################################################################################



################################################################################################

read.csv("day3 (20.10.08)/wine_dataset/wine.data")
################################################################################################