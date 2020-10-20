groceries<-read.csv("Data/groceries.csv") 
#첫번째 줄이 4개 컬럼으로 시작해서 4개로 잘려버림 다음행에 6컬럼이면 다른옵션을 생각해보자
dim(groceries)

install.packages("arules") #association rules
library(arules)
groceries<-read.transactions("Data/groceries.csv", sep = ",")
summary(groceries)
inspect(groceries[1:5])
groceries

# 9835*169=100만개 중 2%=>2만개 셀(0이아님), 98만 개 셀(0)
# 9835건 거래 중에서 2513건 거래에 whole milk가 있음 

# (sizes) 아이템 1개만 이루어진 거래가 총 2159건 있음 
itemFrequency(groceries[,1:10]) #거래 비율 확인 
itemFrequency(groceries) #모든 상품의 거래 비율 확인
itemFrequency(groceries[,169]) #169번째 상품 거래비율
# itemFrequency() 함수로 거래 비율 확인 : support(지지도)

itemFrequencyPlot(groceries, support=0.08) #지지도를 만족하는 것만 시각화 (지지도가 0.1이상인것들만)
#이 옵션을 적절하게 사용해서 특정 지지도를 만족하는 것들만 추출할수있다. 
########################## ===참고 하자=== ############################
#https://ratsgo.github.io/machine%20learning/2017/04/08/apriori/
# https://medium.com/@unfinishedgod/연관규칙분석-apriori-알고리즘-in-r-236d12e3a74a
#######################################################################
itemFrequencyPlot(groceries, topN=20) # 지지도가 높은것부터 정렬 

image(groceries[1:5]) # 전체 데이터를 시각화 (가로 : 1번부터 169 아이템, transaction 5건)
image(groceries[1:169]) # 무엇을 확인? 어느족에 있는 상품들이 많이 구매가 되었는지? 많이 팔린것들이 어느쪽에 집중이 되어 있는지 확인 

help(apriori)
#data: 거래데이터 행렬,
#support: 요구되는 최소 규칙 지지도 
groceryRules<-apriori(groceries, parameter = list(support=0.1, confidence=0.8))
#support가 0.1 이상 이면서 confidence가 0.8 이상인 조건을 만족하는 연관규칙 생성 (없다..)
groceryRules<-apriori(groceries, parameter = list(support=0.005, confidence=0.25, minlen=2))
#support가 0.005 이상 이면서 confidence가 0.25 이상인 조건을 만족하는 연관규칙 생성
############
# support=0.005 : 전체 9835건 거래중에서 약 50건(9835*0.005) 이상의 거래가 있었던 아이템을 대상으로 연관규칙을 만들겠다는 의미 
############
# confidence=0.25 : 신뢰도 임계치 
# confidence(빵->우유) : support(빵, 우유)/support(빵) ||| (빵과 우유)를 동시에 빵보다 많이산경우는 있을수 없다.
#                                 0.05   /        0.1 => 빵을 구매 -> 우유도 구매 규칙의 신뢰도 
############
# minlen=2 : 2개 미만의 아이템을 갖는 규칙을 제외
# ex) {} -> {whole milk} 와 같은 규칙은 필요 없다 || 아이템이 최소한 바구니에 2개 있어야한다 (연관규칙 하려면)
############
groceryRules #set of 662 rules 조건을 만족하는 규칙의수 
#모두 사용하는게 하니고 662개중 향상도가 높은 규칙을 사용해야한다.
#summary를 사용하서 전체적인 요약을 확인 
summary(groceryRules) 
#max support 가 0.07이므로 0.1주면 당연히 연관규칙이 안나옴 
#lift : Max. :4.0855  연관규칙에서 최대값에 해당하는 것들이 중요한 지표임
###
# 규칙: 아이템(lhs) -> 아이템(rhs)  #left hand side | right hand side
# {빵}->{우유} : 길이가 2    빵을산사람이 우유도 사더라 
# {빵,우유}->{아이스크림} : 3
# {빵}->{우유,아이스크림} : 3
###
inspect(groceryRules[1:5]) #confidence도 봐야하지만 lift도 많이 봐야한다 일단 최소값 1보다 크다 
#지지도 0.4230769 캐익을 구매한 사람들 중에서 우유도 구매한 사람들의 비율이 40프로 정도이다. 
# lift : 향상도
# 생성된 규칙이 실제 효용가치가 있는지를 판별하는 데 사용되는 향상도는 아래와 같이 조건절과 결과절이 
# 서로 독립일 때와 비교해 두 사건이 동시에 얼마나 발생하는지 비율로 나타납니다. 
# 바꿔 말해 향상도가 1이라면 조건절과 결과절은 서로 독립임을 뜻합니다. 
# 규칙 사이에 유의미한 연관성이 없다는 걸로 받아들이면 될 것 같습니다. 
# 향상도가 2라면 두 사건이 독립이라는 걸 가정했을 때 대비 2배로 긍정적인 연관관계를 나타냅니다.
#####내림차순 (의미있음)
inspect(sort(groceryRules, by="lift")[1:5]) 
# lift 4.085493 일반적인사람들의 root vegetables거래 대비, 
# {citrus fruit,other vegetables,whole milk}물건들을 사는사람이 root vegetables 함께 사는 경우가 되게 높다 
#####오름차순 (의미없음)
inspect(sort(groceryRules, by="lift", decreasing=FALSE)[1:5])
################################################################
inspect(sort(groceryRules, by="lift")[1:20]) #이 결과를 출력하고 싶다 : write함수 사용 

#전략적으로 Berries 상품과 함께 향상도가 높은 상품들을 추출해서 -> 판매 
subset(groceryRules, items %in% "berries")
inspect(subset(groceryRules, items %in% "berries")) #lift(향상도가) 1 이상이면 의미있는 규칙이라고 생각!
berryRules<-subset(groceryRules, items %in% "berries")
write(berryRules, file="berryRules.csv", sep=",", row.names=FALSE) #row.names=FALSE 를 해주어야 컬럼명이 데이터와 같은열이된다.
berryDf<-as(berryRules, "data.frame")
str(berryDf)
#tip
inspect(subset(groceryRules, items %in% c("whole milk","yogurt")))

#ex) {...} -> {suicide} 어떤 동작을 보니까 자살하더라;; 이런 연관규칙 가능 