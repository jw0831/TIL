sms<-read.csv("Data/hamspamtest.txt", stringsAsFactors = FALSE, fileEncoding = "euc-kr", sep = ",", header = FALSE)
names(sms)<-c("type","text")
str(sms)

sms$type<-factor(sms$type) #구조를 factor로 변경
str(sms)
library(tm)
# 코퍼스 생성 (말뭉치)
CORPUS<-Corpus(VectorSource(sms$text))
# 문자 전처리(불용어, 조사, 숫자 제거등...)
CORPUS_TM<-tm_map(CORPUS, stripWhitespace) #공백(엔터, 탭 문자)
CORPUS_TM=tm_map(CORPUS_TM, removeNumbers) #, 숫자 제거
CORPUS_TM=tm_map(CORPUS_TM, tolower) #, 소문자 통일
CORPUS_TM=tm_map(CORPUS, removePunctuation) #특수문자 제거
CORPUS_TM<-tm_map(CORPUS_TM, removeWords, c(stopwords("en")))
# 문서행렬 생성
TDM<-TermDocumentMatrix(CORPUS_TM)
DTM<-DocumentTermMatrix(CORPUS_TM) #DTM
DTM
inspect(DTM) #문서행렬 관찰
m<-as.matrix(TDM)
m
v<-sort(rowSums(m), decreasing = TRUE) #내림차순
names(v) #단어만 출력
d<-data.frame(word=names(v), freq=v)
d
# 분석/모델링
library(SnowballC)
library(wordcloud)
library(RColorBrewer)
wordcloud(words=d$word, freq=v, min.freq = 5, 
          max.words = 200, random.order = FALSE, 
          colors = brewer.pal(8, "Dark2")) # random.order = FALSE로 하면 중심에 빈도수가 높은게 온다

sms_train_labels<-sms[1:7,]$type #트레이닝 데이터 정답
sms_tests_labels<-sms[8:10,]$type#테스트 데이터 정답

sms_dtm_train<-DTM[1:7,]
sms_dtm_test<-DTM[8:10,]


prop.table(table(sms_train_labels))

prop.table(table(sms_tests_labels))

wordcloud(CORPUS_TM, min.freq=50, random.order=FALSE)
spam<-subset(sms, type=="spam")
ham<-subset(sms, type=="ham")

wordcloud(spam$text, max.words = 50, random.order = FALSE)
wordcloud(ham$text, max.words = 50, random.order = FALSE)

library(e1071)
sms_dtm_train
sms_dtm_freq_train<-removeSparseTerms(sms_dtm_train, 0.999)
sms_dtm_freq_train

sms_dtm_train
sms_dtm_freq_train<-removeSparseTerms(sms_dtm_train, 0.98)
sms_dtm_freq_train

sms_freq_words<-findFreqTerms(sms_dtm_train, 2)
str(sms_freq_words) #1151개 단어 벡터 
sms_dtm_freq_train<-sms_dtm_train[ ,sms_freq_words]
sms_dtm_freq_test<-sms_dtm_test[ ,sms_freq_words]
#나이브베이즈

inspect(sms_dtm_freq_train)
inspect(sms_dtm_freq_test)

convertCounts<-function(x){
  x<-ifelse(x>0, "Yes","No")
}
sms_train<-apply(sms_dtm_freq_train, MARGIN =2, convertCounts)
# MARGIN = 1 은 행, 2는 열 
sms_train

sms_test<-apply(sms_dtm_freq_test, MARGIN =2, convertCounts)
# MARGIN = 1 은 행, 2는 열 
sms_test

smsClassifier<-naiveBayes(sms_train, sms_train_labels, laplace =1) #모델 완성
sms_test_pred<-predict(smsClassifier, sms_test)
sms_test_pred
library(gmodels)
CrossTable(sms_test_pred, sms_tests_labels, dnn = c("predicted", "actual"))


########################################################################################
#이지윤님 
new_test <- read.csv("Data/hamspamtest.txt", stringsAsFactors = F,header = F)
new_test 
names(new_test) <- c("type","text")
new_test$type<-factor(new_test$type)


# ----파일 전처리
test_corpus <- VCorpus(VectorSource(new_test$text))
test_corpus

test_corpus_clean <- tm_map(test_corpus, removeNumbers)
test_corpus_clean <- tm_map(test_corpus_clean, content_transformer(tolower))
test_corpus_clean <- tm_map(test_corpus_clean, removePunctuation)
test_corpus_clean <- tm_map(test_corpus_clean, removeWords, stopwords())
test_corpus_clean <- tm_map(test_corpus_clean, stemDocument) 
test_corpus_clean <- tm_map(test_corpus_clean, stripWhitespace) 


# ----매트릭스 생성
test_dtm <- DocumentTermMatrix(test_corpus_clean)
test_labels <- new_test$type
test_dtm_test <- test_dtm


# ----분석
# smsClassifier <- naiveBayes(sms_train,sms_train_labels, laplace = 1)  모델 
sms_test <- apply(test_dtm_test, MARGIN = 2, convertCounts)
new_test_pred <- predict(smsClassifier, sms_test)
new_test_pred

#----결과
CrossTable(new_test_pred, test_labels, dnn = c("predicted", "actual")

