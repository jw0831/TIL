help(iconv)
sms_raw<-read.csv("Data/sms_spam_ansi.txt", stringsAsFactors = FALSE)
# sms_raw<-read.csv("Data/sms_spam_ansi.txt", stringsAsFactors = FALSE,header= FALSE, fileEncoding = "euc-kr")
# sms_raw <- iconv(sms_raw,"WINDOWS-1252","UTF-8") #에러 고치는 옵션 
str(sms_raw)
# Factor 로 변환 해야 할것을 따로 factor함수안에 넣어서 바꿔주자 
sms_raw$type<-factor(sms_raw$type)
str(sms_raw) #factor로 바뀐것을 확인
###
table(sms_raw$type)
#우도표
#sms data에서 중복되는 단어를 하나로 추출 (원래는 수고스럽게 우리가 해야하지만 대신해주는 유용한 라이브러리 txt mining:tm)
#tm패키지 -> 코퍼스(corpus 말뭉치) 구축 
# install.packages("tm") #텍스트마이닝 툴
library(tm)
# help -> tm -> tm::tm pdf 읽어보기
# corpus ? 특정 도메인에서 통용되는 단어 집합 
# ex) 법령코퍼스 
# 1. <특정분야>코퍼스 구축 (제일처음 단계)
###
stopwords("en") #불용어: 문맥을 파악하는데 있어서 도움이 되지 않는 단어들 (언어학자들이 만들어둔 사전)
#ex) stopwords함수 하나로 불용어 제거하는법
removeWords("of the people", stopwords("en"))
###
#######
IMDB<-read.csv("Data/IMDB-Movie-Data.csv")
str(IMDB)
summary(IMDB)

sum(is.na(IMDB$Metascore))
colSums(is.na(IMDB)) #각각의 열에대해 NA에대한 SUM을 구하고 싶을때
#결측치 제거
IMDB2<-na.omit(IMDB) #모든변수에 대해 결측값이 1개라도 있다면, 해당 행을 제거 (행단위)
colSums(is.na(IMDB2)) #결측치가 있는 행은 모두 제거됨을 확인 

#특정 변수에 결측값이 있는 경우 해당 행만 삭제
IMDB3<-IMDB[complete.cases(IMDB[,12]),] #12번째 열에 대해 결측값이 있는경우 해당행을 삭제하겠다. (좀더 섬세)
colSums(is.na(IMDB3))
colSums(is.na(IMDB))

IMDB$Metascore
IMDB$Metascore2<-IMDB$Metascore
IMDB$Metascore2[is.na(IMDB$Metascore)]<-50
IMDB$Metascore2[is.na(IMDB$Metascore)]
# na.rm=TRUE
mean(IMDB$Revenue..Millions., na.rm=TRUE)

#극단치 제거(IMDB$Revenue..Millions., Q1-1.5*IQR,Q3+1.5*IQR)
IMDB$Revenue..Millions.
Q1<-quantile(IMDB$Revenue..Millions.,probs=c(0.25), na.rm=TRUE)
Q3<-quantile(IMDB$Revenue..Millions.,probs=c(0.75), na.rm=TRUE)

LC=Q1-1.5*(Q3-Q1)
UC=Q1+1.5*(Q3-Q1)
boxplot(IMDB$Revenue..Millions.)$stats[2,] #LC 이방법도 있음.
boxplot(IMDB$Revenue..Millions.)$stats[4,] #UC

IMDB2<-subset(IMDB, IMDB$Revenue..Millions.>LC & IMDB$Revenue..Millions. < UC) #정상범위 데이터
boxplot(IMDB$Revenue..Millions.)$stats
####
IMDB$Actors[1] #"Chris Pratt, Vin Diesel, Bradley Cooper, Zoe Saldana"
substr(IMDB$Actors[1], 1, 5) #"Chris"

#문자열 붙이기
paste(IMDB$Actors[1], "_","A")
paste(IMDB$Actors[1], "_","A", sep="")
#문자열 분리
strsplit(IMDB$Actors[1], split=",")
#문자열 대체 (중요)
# ex) "우리나라 한국 대한민국 남한 코리아 남조선..." -> "대한민국" 일괄적인 변경 가능
IMDB$Genre2<-gsub(",", " ", IMDB$Genre)
IMDB$Genre2
##############################################################################
# 텍스트 마이닝 (자연어처리 절차 머리속에 잘 넣기) 중요!
##############################################################################
# 1. 코퍼스 생성 (말뭉치)
# 2. 단어(T)문서(D)행렬(M) (행에는 단어, 열에는 문서); TDM or (문서단어행렬 (행에는 문서, 열에는 단어); DTM)
# TDM -> Transpose -> DTM -> Transpose -> TDM 
# 3. 문자 전처리(불용어, 조사, 숫자 제거등...)
# 4. 분석/모델링
##############################################################################
# 1.
CORPUS<-Corpus(VectorSource(IMDB$Genre2)) #코퍼스 생성
# 3번과정이지만 현재 단계 에서진행 가능 
# 특수문자 제거, 숫자 제거, 소문자 통일
CORPUS_TM=tm_map(CORPUS, removePunctuation) #특수문자 제거
CORPUS_TM=tm_map(CORPUS_TM, removeNumers) #, 숫자 제거
CORPUS_TM=tm_map(CORPUS_TM, tolower) #, 소문자 통일

# 2. 문서행렬 생성
DTM<-DocumentTermMatrix(CORPUS_TM) #DTM
DTM
# <<DocumentTermMatrix (documents: 1000, terms: 20)>> # DTM사이즈가 (1000*20 => 20000개 행렬 요소)
#   Non-/sparse entries: 2555(0이 아닌값)/17445(0) 0: 해당단어가 문서에 등장하지 않는다. dense <-> sparse(희소행렬)
# Sparsity           : 87% # (전체 데이터에서 0이 차지하는 비중)
# Maximal term length: 9
# Weighting          : term frequency (tf) 단어빈도수(tf) 로 weighting이 되어져 있다는 뜻

inspect(DTM) #문서행렬 관찰 
# Docs action adventure comedy crime drama horror mystery romance scifi thriller
# 1       1         1      0     0     0      0       0       0     1        0
IMDB$Genre2[1] #[1] "Action Adventure Sci-Fi"

DTM<-as.data.frame(as.matrix(DTM)) #문서(영화) : 1000, 단어(장르 종류):20 코퍼스 생성
head(DTM)

IMDB_GENRE<-cbind(IMDB, DTM)
###############################
# 3. 문자 전처리(불용어, 조사, 숫자 제거등...)
IMDB$Description #단어 중복, 조사, 동사, 명사, .. 
CORPUS<-Corpus(VectorSource(IMDB$Description)) # IMDB$Description에 등장하는 단어 집합으로 코퍼스를 구성
CORPUS_TM<-tm_map(CORPUS, stripWhitespace) #공백(엔터, 탭 문자)
CORPUS_TM<-tm_map(CORPUS_TM, removeNumbers) #숫자제거
CORPUS_TM<-tm_map(CORPUS, tolower) #소문자로 변환
CORPUS_TM<-tm_map(CORPUS, removePunctuation) #특수문자 제거

DTM<-DocumentTermMatrix(CORPUS_TM)
inspect(DTM)
# <<DocumentTermMatrix (documents: 1000, terms: 6044)>>
#   Non-/sparse entries: 20558/6023442 (낭비가 심하다)
# Sparsity           : 100%
# Maximal term length: 23
# Weighting          : term frequency (tf)

CORPUS_TM<-tm_map(CORPUS_TM, removeWords, c(stopwords("english"), "my", "custom", "words"))
# 불용어를 제거, 추가적으로  "my", "custom", "words" 단어들도 제거

TDM<-TermDocumentMatrix(CORPUS_TM)
m<-as.matrix(TDM)
m

# rowSums(m) #행단위로 합계구하기: 줄단위로 단어들에 대한 합계
#                  영화1....영화 1000
# control           0   ....     0       => 행 합계(rowSums:9)
# criminals
# ...
v<-sort(rowSums(m), decreasing = TRUE) #내림차순
names(v) #단어만 출력
d<-data.frame(word=names(v), freq=v)
######## wordcloud ########
# install.packages("SnowballC") #어근추출, runs, running, run, ... => run
library(SnowballC)
# install.packages("wordcloud")
library(wordcloud) 
# 화려한 시각화 (palette)
# install.packages("RColorBrewer")
library(RColorBrewer)

wordcloud(words=d$word, freq=v, min.freq = 5, 
          max.words = 200, random.order = FALSE, 
          colors = brewer.pal(8, "Dark2")) # random.order = FALSE로 하면 중심에 빈도수가 높은게 온다

#DTM / TDM 을 갖고 코사인 유사도도 구할수 있다. (영화분류 알고리즘)
library(tm)
Corpus(VectorSource(sms_raw$text))
sms_corpus<-VCorpus(VectorSource(sms_raw$text)) #한글이 덜깨짐
sms_corpus
inspect(sms_corpus[1:3])
sms_raw$text[3]
sms_corpus[[1]]
class(sms_corpus[[1]])

as.character(sms_corpus[[1]]) #확인
lapply(sms_corpus[1:3], as.character) #sms_corpus[1:3] text에대한 내용을 확인

sms_corpus_clean<-tm_map(sms_corpus, removeNumbers)
sms_corpus_clean<-tm_map(sms_corpus_clean, content_transformer(tolower)) #tolower 다른방식
# sms_corpus_clean<-tm_map(sms_corpus_clean, toString #인터넷 검색 특수문자
sms_corpus_clean<-tm_map(sms_corpus_clean, removePunctuation) #특수문자 제거                      
# removePunctuation -> help -> regex 정규표현식 
# Punctuation characters:
  # ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~.
sms_corpus_clean<-tm_map(sms_corpus_clean, removeWords, stopwords())

###
removePunctuation("hello..., ; : @#$)hihihi")

myReplace<-function(x){
  gsub("[[:punct:]]+", " ", x) #removePunctuation -> help -> regex 정규표현식 
}
myReplace("hello..........world")
wordStem(c("learn","learned", "learning","learns")) #snowballC 함수: 어근만 추출 
###
sms_corpus_clean<-tm_map(sms_corpus_clean, stemDocument) #sms_corpus_clean 에 있는 단어들에 대해 어근 추출 (wordStem) 
sms_corpus_clean<-tm_map(sms_corpus_clean, stripWhitespace) #"a     b     c" => "a b c" 공백을 하나로 만들어준다.

lapply(sms_corpus[1:3], as.character)
# $`1`
# [1] "Hope you are having a good week. Just checking in"
# $`2`
# [1] "K..give back my thanks."
# $`3`
# [1] "Am also doing in cbe only. But have to pay."
lapply(sms_corpus_clean[1:3], as.character)

sms_dtm<-DocumentTermMatrix(sms_corpus_clean)
sms_dtm
############## 여기까지 데이터 전처리 ##############
# 1. 트레이닝/ 테스트 분할
# 2. 워드클라우드(시각화, 스팸/햄) 하나는 스팸/ 하나는 햄 

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

wordcloud(spam$text, max.words = 50, random.order = FALSE)
wordcloud(ham$text, max.words = 50, random.order = FALSE)

# sms_dtm_train => sms_train_labels
# sms_dtm_test => sms_tests_labels

# install.packages("e1071") #베이지안 필터기 라이브러리중 하나 
library(e1071)

sms_dtm_train
sms_dtm_freq_train<-removeSparseTerms(sms_dtm_train, 0.999)
sms_dtm_freq_train #sparsity가 99퍼센트로 줄었다. 0이 너무 많은 term들을 제거해준다. (거의언급 안된 단어는 제거)

sms_dtm_train
sms_dtm_freq_train<-removeSparseTerms(sms_dtm_train, 0.98)
sms_dtm_freq_train

sms_freq_words<-findFreqTerms(sms_dtm_train, 5)
#5번이상 언급된 단얻르의 목록

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
sms_train<-apply(sms_dtm_freq_train, MARGIN =2, convertCounts)
# MARGIN = 1 은 행, 2는 열 
sms_train

sms_test<-apply(sms_dtm_freq_test, MARGIN =2, convertCounts)
# MARGIN = 1 은 행, 2는 열 
sms_test

#library(e1071) 사용한 모델링
smsClassifier<-naiveBayes(sms_train, sms_train_labels, laplace =1) #모델 완성/ laplace를 더해서 0이될뻔한것을 1로 바꾸어준다.
# 단어: 1151개, 이메일: 5569편
# 1151개 단어로 -> 우도표 생성 
sms_test_pred<-predict(smsClassifier, sms_test)

# install.packages("gmodels") #cross table 교차테이블 예측과 실제값 테이블로 보여주는 함수
library(gmodels)
CrossTable(sms_test_pred, sms_tests_labels, dnn = c("predicted", "actual"))

#정확도
print((1202+154)/1390)

###에러고치기.. 줄수가 안맞음 전처리 에러 

#내일 연습문제 
# 새로운 이메일 제목 -> "free cash ... night club ,,," -> 힘/스팸? (smsClassifier)
# sms_test_pred <- predict(smsClassifier,sms_test)

#sms_test
#free cash ...
#yes  yes

#추가설명
# sms_test_pred 하면 분류된값이 나온다.
sms_test가 matrix이다. 

# 형님 급하게 필요하게 됐습니다. $10000 입금 부탁드립니다. 
# (여기서 숫자는 변하지만, $기호가 의미가 있다. 무조건 특수문자를 제거하면 곤란하다.)
