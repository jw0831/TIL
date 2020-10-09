# R언어도 대소문자 구분이 있다 <주의!!!>
df<-data.frame(gender=c("m","f",NA,"m","f"), score=c(5,4,3,4,NA)) #<꺽세>로 NaN 구분
df

is.na(df)

table(is.na(df))
table(is.na(df$gender))

sum(df$score) #all comes with NA if there is NA, so we need to take it out

df %>% 
  filter(is.na(score))

dfnew <- df %>% 
  filter(!is.na(score))
mean(dfnew$score)

df %>% 
  filter(!is.na(score) & !is.na(gender))

na.omit(df) #function to remove NA

mean(df$score, na.rm=T) #option: if there is NA, remove and calculate
#we can use this into summarize function

exam <- read.csv("Data/csv_exam.csv")
exam[c(3,8,15),"math"]

#force NA
exam[c(3,8,15),"math"]<-NA
# summarize with NA
exam %>% 
  summarise(meanm=mean(math))
# summarize by removing NA
exam %>% 
  summarise(meanm=mean(math, na.rm=T))
##########
exam %>% 
  summarise(meanm=mean(math, na.rm=T),
            summ=sum(math, na.rm=T),
            mem=median(math, na.rm=T))
###### quiz 1 ######
exam$math
# 결측값을 math의 평균값으로 대체하라
# exam$math <- ifelse(is.na(exam$math), mean(exam$math, na.rm=T), exam$math) 
#전체 대이터에 대해서 평균구하는 함수를 계속 수행함으로 퍼포먼스 측면에서 떨어진다.
# Better Way (tuned code)
av=mean(exam$math, na.rm=T)
exam$math <- ifelse(is.na(exam$math), av, exam$math)
##### another way
exam$math[is.na(exam$math)] <- mean(exam$math, na.rm=T)
#### cheking
table(is.na(exam$math))
####################
# outlier 제거
# 이상치 (극단치)는 먼저 결측치로 처리(간주) -> 제외한 다음 분석

# ex) 성별변수 : 3가지 -> 1가지 (결측처리)
# ex) 몸무개 변수: 변수값 200kg (정상범위 설정 -> 결측처리)
ol<-data.frame(gen=c(1,2,1,2,3), score=c(5,4,1,3,4))
ol
table(ol$gen)

ol$gen<-ifelse(ol$gen==3, NA, ol$gen)
ol

#score값이 4초과시 이상치 간주
ol$score<-ifelse(ol$score==4, NA, ol$score)
ol

ol %>% 
  filter(!is.na(gen) & !is.na(score)) %>% 
  group_by(gen) %>% 
  summarise(ms=mean(score))

# 데이터전처리 -> 머신러닝/딥러닝
# 1만시간 법칙 : 판다스, 넘파이에 1만시간 투자 

# 정상범위: 논리적(통계적) 판단 근거
# 논리적? 성인 몸무게는 40kg~150kg
# 통계적? 상하위 0.3% 극단치 or boxplot에서 iqr*1.5배 벗어나면 극단치 
library(dplyr)
library(ggplot2)
mpg<-ggplot2::mpg
boxplot(mpg$hwy)

boxplot(mpg$hwy)$stats #이용해서 값을 확인할 수 있다.
# 12보다 작으면, 37보다 크면 이상치라는 것을 확인 
mpg$hwy<-ifelse(mpg$hwy<12 | mpg$hwy>37, NA, mpg$hwy)
table(is.na(mpg$hwy)) #3 outliers

mpg %>% 
  group_by(drv) %>% 
  summarise(mh=mean(hwy, na.rm=T))

#########################################################################################################
# 한국인의 삶의 질 분석
# koweps_hpc10_2015_beta1.sav
# sav 확장자는 SPSS 통계 파일

install.packages("foreign")
library(foreign)
library(readxl)
library(ggplot2)
raw_welfare=read.spss(file="Data/Koweps_hpc10_2015_beta1.sav", to.data.frame=T)
#복사본
welfare<-raw_welfare
head(welfare)
tail(welfare)
View(welfare)
## 습관처럼 실행 ##
dim(welfare)
str(welfare)
summary(welfare)
###################
welfare<-rename(welfare, 
                sex=h10_g3,
                birth=h10_g4,
                marriage=h10_g10,
                religion=h10_g11,
                income=p1002_8aq1,
                code_job=h10_eco9,
                code_region=h10_reg7)

#성별에 따른 월급 차이?
table(welfare$sex)
table(is.na(welfare$sex)) #결측치 없음
#ifelse사용 sex = 1 => male, sex=2 => female 값 변경
welfare $sex<-ifelse(welfare$sex==1, "male", "female")
table(welfare$sex)
qplot(welfare$sex)

welfare$income #NA 가 많다. 공개하기를 꺼려해서 많이 없다. 
summary(welfare$income)
#na 대체값, na 제외
qplot(welfare$income)
#수입이 1000정도까지만 보고싶은 경우 x축 한계 설정
qplot(welfare$income)+xlim(0, 1000)
#이상치에 대한 부분을 NA로 간주해보자
welfare$income<-ifelse(welfare$income %in% c(0, 5000), NA, welfare$income)
table(is.na(welfare$income))

#NA가 아닌 데이터에 대해 성별에 따른 급여 평균 조사
#퀴즈2
sex_income<-filter(welfare, !is.na(income)) %>% select(income, sex) %>% group_by(sex) %>% summarise(mean_income=mean(income))
# PLOT
ggplot(data=sex_income, aes(x=sex, y=mean_income))+geom_col()
# 성별에 다른 급여 차이가 있음 (결론) 2015년 데이터

## 몇살때 가장 많은 급여를 받을까?
# 나이데 따른 평균 월급
welfare$birth
summary(welfare$birth)
qplot(welfare$birth)
table(is.na(welfare$birth))
ifelse(welfare$birth==999, NA, welfare$birth)
table(is.na(welfare$birth))
# quiz 3: age열 추가
# age는 2015-birth+1값으로 함
# summary, qplot 출력
welfare$age<-2015-welfare$birth+1
summary(welfare$age)
qplot(welfare$age) #pipe를 활용하게되면 잘 안되는것 같다

#나이에 따른 급여 평균
age_income<-welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(age) %>% 
  summarise(mean_income=mean(income))

ggplot(data=age_income, aes(x=age, y=mean_income))+geom_col()
ggplot(data=age_income, aes(x=age, y=mean_income))+geom_line()

# 연령대(young(<30) / middle(<60) / old(>=60))
welfare<-welfare %>% 
  mutate(ageg=ifelse(age<30,"young",
         ifelse(age<=59,"middle","old")))
welfare$ageg
table(welfare$ageg)
qplot(welfare$ageg)

#연령대별 월급 평균 출력
ageg_income<-welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(ageg) %>% 
  summarise(mean_income=mean(income))
ggplot(data=ageg_income, aes(x=ageg, y=mean_income))+geom_col()

# 막대그래프 정렬: 
ggplot(data=ageg_income, aes(x=ageg, y=mean_income))+geom_col()+
  scale_x_discrete(limits=c("young","middle","old"))

#성별에 따른 월급 차이가 연령대별로 다를까 비슷할까?
sex_income<-welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(ageg, sex) %>% 
  summarise(mean_income=mean(income))

ggplot(data=sex_income, aes(x=ageg, y=mean_income, fill=sex))+geom_col()+
  scale_x_discrete(limits=c("young","middle","old"))

ggplot(data=sex_income, aes(x=ageg, y=mean_income, fill=sex))+geom_col(position="dodge")+
  scale_x_discrete(limits=c("young","middle","old"))

#ggplot 설정함수
#geom_col 출력함수

sex_age<-welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(age, sex) %>% 
  summarise(mean_income=mean(income))
sex_age
ggplot(data=sex_age, aes(x=age, y=mean_income))+geom_line() #남녀가 섞여서 그려진다
ggplot(data=sex_age, aes(x=age, y=mean_income, col=sex))+geom_line() #분리해서 그리기

#어떤 직업군이 급여를 많이받고 적게 받을까?
#직업군 <-> 급여 비교
welfare$code_job #직업 코드
table(welfare$code_job)

library(readxl) #excel file reading library
list_job<-read_excel("Data/Koweps_Codebook.xlsx", col_names = T, sheet = 2)
list_job
dim(list_job) #직종코드 149개 확인
## 집중!!!
welfare$code_job
welfare<-left_join(welfare, list_job, id="code_job")
#welfare에 list_job을 연결해라(code_job 공통 컬럼 값으로)
welfare$code_job
list_job$code_job

str(welfare)

welfare %>% filter(!is.na(code_job)) %>% 
  select(code_job, job)

#quiz 3
#직업별 월급 평균 출력
job_income<-welfare %>% filter(!is.na(income)) %>% 
  select(code_job,job,income) %>% 
  group_by(job) %>% 
  summarise(mi=mean(income))
job_income

top20<-job_income %>% 
  arrange(desc(mi)) %>% 
  head(20)
top20

ggplot(data=top20, aes(x=job,y=mi))+geom_col()+coord_flip()

bottom10<-job_income %>% 
  arrange(mi) %>% 
  head(10)
bottom10

ggplot(data=bottom10, aes(x=job,y=mi))+geom_col()+coord_flip()+
  ylim(0,500)

#퀴즈4
#남성 직업 빈도 상위 10개 출력
job_male<-welfare %>% 
  filter(sex=="male" & !is.na(job)) %>% 
  group_by(job) %>% 
  summarise(cnt=n()) %>% 
  arrange(desc(cnt)) %>% 
  head(10)
job_male
job_female<-welfare %>% 
  filter(sex=="female" & !is.na(job)) %>% 
  group_by(job) %>% 
  summarise(cnt=n()) %>% 
  arrange(desc(cnt)) %>% 
  head(10)
job_female

#종교가 있는 사람이 이혼을 더/덜할까???
#종교 유/무에 따른 이혼율 조사
welfare$religion
table(welfare$religion) #모름: 9 없다.
welfare$religion<-ifelse(welfare$religion==1, "yes","no")
table(welfare$religion)
qplot(welfare$religion)

welfare$marriage
table(welfare$marriage)
#이혼 여부 변수 생성
welfare$group_marriage<-ifelse(welfare$marriage==1,"marriage",
       ifelse(welfare$marriage==3,"divorce",NA))
table(welfare$group_marriage)
table(is.na(welfare$group_marriage))
qplot(welfare$group_marriage)

religion_marriage<-welfare %>% 
  filter(!is.na(group_marriage)) %>% 
  group_by(religion, group_marriage) %>% 
  summarise(cnt=n()) %>% 
  mutate(tot_group=sum(cnt)) %>% 
  mutate(pct=round(cnt/tot_group*100,1))

divorce=religion_marriage %>% 
  filter(group_marriage=="divorce") %>% 
  select(religion, pct)
divorce
