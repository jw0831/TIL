sms_raw<-read.csv("sms_spam_ansi.txt", stringsAsFactors = FALSE)
str(sms_raw)

sms_raw$type<-factor(sms_raw$type)
str(sms_raw)

table(sms_raw$type)

#tm패키지 -> 코퍼스(corpus, 말뭉치) 구축

install.packages("tm") #텍스트마이닝 툴
library(tm)

# corpus? 특정 도메인에서 통용되는 단어 집합
# ex) 법령코퍼스

stopwords("en") #불용어

removeWords("of the people",stopwords("en"))

IMDB<-read.csv("IMDB-Movie-Data.csv")
str(IMDB) #numeric > integer
summary(IMDB)

sum(is.na(IMDB$Metascore))
colSums(is.na(IMDB))

#결측치 제거
IMDB2<-na.omit(IMDB) #모든 변수에 대해 결측값이 1개라도 있다면, 해당 행을 제거
colSums(is.na(IMDB2))

#특정 변수(12번 열)에 대해 결측값이 있는 경우 해당 행을 삭제
IMDB3<-IMDB[complete.cases(IMDB[,12]),]
colSums(is.na(IMDB3))
colSums(is.na(IMDB))

IMDB$Metascore2<-IMDB$Metascore
IMDB$Metascore2[is.na(IMDB$Metascore2)]<-50

#na.rm=TURE

mean(IMDB$Revenue..Millions., na.rm=TRUE)


#극단치 제거(IMDB$Revenue..Millions., Q3+1.5*IQR, Q1-1.5*IQR)

#1분위수
Q1<-quantile(IMDB$Revenue..Millions., probs=c(0.25), na.rm=TRUE)
#3분위수
Q3<-quantile(IMDB$Revenue..Millions., probs=c(0.75), na.rm=TRUE)

LC=Q1-1.5*(Q3-Q1)
UC=Q3+1.5*(Q3-Q1)

IMDB2<-subset(IMDB, IMDB$Revenue..Millions.>LC & IMDB$Revenue..Millions. < UC) #정상범위 데이터

IMDB$Actors[1] #"Chris Pratt, Vin Diesel, Bradley Cooper, Zoe Saldana"
substr(IMDB$Actors[1],1,5)

#문자열 붙이기
paste(IMDB$Actors[1], "_", "A", sep="") 
#문자열 분리
strsplit(IMDB$Actors[1], split=",")
#문자열 대체
IMDB$Genre2<-gsub(",", " ", IMDB$Genre)

#  gsub함수 이용하여, "우리나라 한국 대한민국 남한 코리아 남조선..." => "대한민국"
IMDB$Genre2

#텍스트마이닝#
#1)코퍼스생성 -> 2) 단어(T)문서(D)행렬(M);TDM or(문서단어행렬;DTM) -> 3)문자 전처리(불용어, 조사, 숫자 제거 등...)-> 분석/모델링
#
#     문서1 문서2... 문서N
# hello
# hi
# sky
# ...
# TDM -> Transpose -> DTM

CORPUS=Corpus(VectorSource(IMDB$Genre2)) #코퍼스 생성
CORPUS_TM=tm_map(CORPUS, removePunctuation) #특수문자 제거
CORPUS_TM=tm_map(CORPUS_TM, removeNumbers)#숫자 제거
CORPUS_TM=tm_map(CORPUS_TM, tolower)#소문자 통일

#문서행렬 생성
DTM<-DocumentTermMatrix(CORPUS_TM)
DTM

# 
# DTM(1000*20 => 20000개 행렬 요소)
# documents: 1000, terms: 20
# Non-/sparse entries: 2555(0이 아님)/17445(0)
# Sparsity(0이 차지하는 비중:87%)
# #dense<->sparse(희소행렬)

inspect(DTM)

IMDB$Genre2[1]
inspect(DTM)
IMDB$Genre2[1]

DTM<-as.data.frame(as.matrix(DTM)) #문서(영화):1000, 단어(장르 종류):20 코퍼스 생성
head(DTM)

IMDB_GENRE<-cbind(IMDB, DTM)


IMDB$Description #단어 중복, 조사, 동사, 명사,...
#불용어 제거
CORPUS<-Corpus(VectorSource(IMDB$Description)) #IMDB$Description에 등장하는 단어 집합으로 코퍼스를 구성
CORPUS_TM<-tm_map(CORPUS, stripWhitespace) #공백(엔터, 탭 문자)
CORPUS_TM<-tm_map(CORPUS_TM, removeNumbers) #숫자제거거
CORPUS_TM<-tm_map(CORPUS_TM, tolower) #소문자
CORPUS_TM<-tm_map(CORPUS_TM, removePunctuation) #구두점 제거거

DTM<-DocumentTermMatrix(CORPUS_TM)
inspect(DTM)

#IMDB$Description[155]

CORPUS_TM<-tm_map(CORPUS_TM, removeWords, c(stopwords("english"), "my", "custom", "words"))
#불용어를 제거, 추가적으로 "my", "custom", "words" 단어들도 제거


TDM<-TermDocumentMatrix(CORPUS_TM)

m<-as.matrix(TDM)
m

rowSums(m)
#IMDB$Description
#                 영화1 ... 영화1000
# control           0   ...      0     =====> 행 합계(rowSums:9)
# criminals         
# ...

v<-sort(rowSums(m), decreasing = TRUE) #내림차순

names(v)
d<-data.frame(word=names(v), freq=v)

install.packages("SnowballC") #어근추출,  runs, running, run,... => run
library(SnowballC)
install.packages("wordcloud")
library(wordcloud)
install.packages("RColorBrewer")
library(RColorBrewer)


wordcloud(words=d$word, freq=d$freq, min.freq=5,
          max.words=200, random.order=FALSE,
          colors=brewer.pal(8, "Dark2"))






Corpus(VectorSource(sms_raw$text))



sms_corpus<-VCorpus(VectorSource(sms_raw$text))
sms_corpus
inspect(sms_corpus[1:3])

sms_raw$text[3]

as.character(sms_corpus[[1]])
lapply(sms_corpus[1:3], as.character)
#sms_corpus[1:3] text에대한 내용을 확인

sms_corpus_clean<-tm_map(sms_corpus, removeNumbers)
sms_corpus_clean<-tm_map(sms_corpus_clean, content_transformer(tolower))
sms_corpus_clean<-tm_map(sms_corpus_clean, removePunctuation)
sms_corpus_clean<-tm_map(sms_corpus_clean, removeWords, stopwords())

removePunctuation("hello..., ; :hihihi")

myReplace<-function(x){
  gsub("[[:punct:]]+" , " ", x)
}
myReplace("hello......world")

wordStem(c("learn", "learned", "learning", "learns"))

sms_corpus_clean<-tm_map(sms_corpus_clean, stemDocument) #sms_corpus_clean에 있는 단어들에 대해 어근 추출(wordStem)
sms_corpus_clean<-tm_map(sms_corpus_clean, stripWhitespace) #sms_corpus_clean에 있는 단어들에 대해 어근 추출(wordStem)


#stripWhitespace : "a     b     c" => "a b c"

lapply(sms_corpus[1:3], as.character)
"Hope you are having a good week. Just checking in"
"K..give back my thanks."
"Am also doing in cbe only. But have to pay."

lapply(sms_corpus_clean[1:3], as.character)
"hope good week just check"
"kgive back thank"
"also cbe pay"

sms_dtm<-DocumentTermMatrix(sms_corpus_clean)
sms_dtm

#5559*6906 요소38390454
#38347198+43256=5559*6906

##################여기까지 데이터 전처리##################

# 1. 트레이닝/ 테스트 분할
# 2. 워드클라우드(시각화, 스팸/햄)


sms_train_labels<-sms_raw[1:4169,]$type #트레이닝 데이터 정답
sms_tests_labels<-sms_raw[4170:5559,]$type#테스트 데이터 정답

sms_dtm_train<-sms_dtm[1:4169,]
sms_dtm_test<-sms_dtm[4170:5559,]


prop.table(table(sms_train_labels))

prop.table(table(sms_tests_labels))

#트레이닝 데이터 -> 베이지안 필터기 -> 테스트 데이터 -> 분류결과(예측)와 실제결과(정답) 비교
#-> 모델 평가


wordcloud(sms_corpus_clean, min.freq=50, random.order=FALSE)

spam<-subset(sms_raw, type=="spam")
ham<-subset(sms_raw, type=="ham")
ham

wordcloud(spam$text, max.words=50, random.order=FALSE)
wordcloud(ham$text, max.words=50, random.order=FALSE)



# sms_dtm_train => sms_train_labels
# sms_dtm_test  => sms_tests_labels

install.packages("e1071") #베이지안 필터기 라이브러리
library(e1071)


sms_dtm_train
sms_dtm_freq_train<-removeSparseTerms(sms_dtm_train, 0.999)
sms_dtm_freq_train

sms_freq_words<-findFreqTerms(sms_dtm_train, 5)
#5개 이상 문서(이메일)에서 언급된 단어들의 목록

str(sms_freq_words) #1151개 단어 벡터

sms_dtm_freq_train<-sms_dtm_train[ ,sms_freq_words]
sms_dtm_freq_test<-sms_dtm_test[ ,sms_freq_words]

#나이브베이즈 분류기는 범주형 데이터에 대해 훈련
#현재 희소행렬(단어횟수, 숫자) -> 범주형 변환
#셀의 값이 1 이상 -> yes, 아니면 -> no

inspect(sms_dtm_freq_train)
inspect(sms_dtm_freq_test)

convertCounts<-function(x){
  x<-ifelse(x>0, "Yes","No")
}

sms_train<-apply(sms_dtm_freq_train, MARGIN = 2, convertCounts)
#MARGIN=1은 행, 2는 열
sms_train

sms_test<-apply(sms_dtm_freq_test, MARGIN = 2, convertCounts)
sms_test

smsClassifier<-naiveBayes(sms_train,sms_train_labels, laplace = 1) #모델 완성
# 단어:1151개, 이메일:5569편
# 
# 1151개 단어로 -> 우도표 생성
#             tmr         toclaim        ... 1151개단어       
#         예   아니오    예   아니오
# 스팸
# 햄

sms_test_pred<-predict(smsClassifier, sms_test)

install.packages("gmodels")
library(gmodels)

CrossTable(sms_test_pred, sms_tests_labels, dnn = c("predicted", "actual"))

print((1202+154)/1390)

sms_test_pred



#내일 연습문제
#새로운 이메일 제목 -> "free cash ... night club ,,,"->햄/스팸?(smsClassifier)
#sms_test_pred<-predict(smsClassifier, sms_test)

# sms_test
# free cash ...
# Yes   Yes ...









