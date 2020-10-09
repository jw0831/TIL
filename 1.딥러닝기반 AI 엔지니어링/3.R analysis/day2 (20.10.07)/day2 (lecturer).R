library(dplyr)
# mpg 데이터를 이용해 분석 문제를 해결해 보세요.
# ??? Q1. 자동차 배기량에 따라 고속도로 연비가 다른지 알아보려고 합니다. 
# displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 알아보세요. 
mpg <- as.data.frame(ggplot2::mpg)
mpg
mpg4<-mpg %>% filter(displ<=4)
mpg5<-mpg %>% filter(displ>=5)

mean(mpg4$hwy)
mean(mpg5$hwy)
#배기량이 4이하인 자동차의 고속도로 연비가 좋다

# ??? Q2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 합니다. 
#"audi"와 "toyota" 중 어느 manufacturer(자동차 제조 회사)의 cty(도시 연비)가 평균적으로 더 높은지 알아보세요. 
mpga<-mpg %>% filter(manufacturer=="audi")
mpgt<-mpg %>% filter(manufacturer=="toyota")

mean(mpga$cty)
mean(mpgt$cty)
#도요다 시내 주행시 연비가 좋다

# ??? Q3. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 합니다. 
#이 회사들의 자동차를 추출한 뒤 hwy 전체 평균을 구해보세요.
mpga<-mpg %>% filter(manufacturer %in%  c("chevrolet", "ford", "honda") ) #c함수:벡터 생성
mean(mpga$hwy)


# ??? Q4. mpg 데이터는 11개 변수로 구성되어 있습니다. 이 중 일부만 추출해서 분석에 활용하려고 합니다. 
#mpg 데이터에서 class(자동차 종류), cty(도시 연비) 변수를 추출해 새로운 데이터를 만드세요. 
#새로 만든 데이터의 일부를 출력해서 두 변수로만 구성되어 있는지 확인하세요.
df <- mpg %>% select(class, cty)
head(df)

# ??? Q5. 자동차 종류에 따라 도시 연비가 다른지 알아보려고 합니다. 앞에서 추출한 데이터를 이용해서 class(자동차 종류)가 
#"suv"인 자동차와 "compact"인 자동차 중 어떤 자동차의 cty(도시 연비)가 더 높은지 알아보세요.
dfsuv<-df %>% filter(class=="suv")
dfcomp<-df %>% filter(class=="compact")
mean(dfsuv$cty)
mean(dfcomp$cty)

# ??? Q6. "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가 높은지 알아보려고 합니다.
#"audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는 자동차의 데이터를 출력하세요.
mpg %>% 
  filter(manufacturer=="audi") %>% 
  arrange(hwy) %>% 
  tail(5)

mpg %>% 
  filter(manufacturer=="audi") %>% 
  arrange(desc(hwy)) %>% 
  head(5)

# mpg 데이터는 연비를 나타내는 변수가 hwy(고속도로 연비), cty(도시 연비) 두 종류로 분리되어 있습니다. 
# 두 변수를 각각 활용하는 대신 하나의 통합 연비 변수를 만들어 분석하려고 합니다.
# ??? Q7. mpg 데이터 복사본을 만들고
# mpg <- as.data.frame(ggplot2::mpg)
# mpg_new <- mpg 
# cty와 hwy를 더한 '합산 연비 변수'를 추가하세요.
mpg <- as.data.frame(ggplot2::mpg)
mpg_new <- mpg 

mpg_new<-mpg_new %>% 
  mutate(total=hwy+cty)
mpg_new

# ??? Q8. 앞에서 만든 '합산 연비 변수'를 2로 나눠 '평균 연비 변수'를 추가세요.
mpg_new<-mpg_new %>% 
  mutate(mymean=total/2)
mpg_new

# ??? Q9. '평균 연비 변수'가 가장 높은 자동차 3종의 데이터를 출력하세요. 
mpg_new %>% 
  arrange(desc(mymean)) %>% 
  head(3)
#??? Q9-1. 1~3번 문제를 해결할 수 있는 하나로 연결된 dplyr 구문을 만들어 출력하세요. 
#데이터는 복사본 대신 mpg 원본을 이용하세요.
mpg %>% 
  mutate(total=hwy+cty,
         mymean=total/2) %>% 
  arrange(desc(mymean)) %>% 
  head(3)

# ??? Q10. 회사별로(group_by) "suv"(filter) 자동차의 도시 및 고속도로 통합 연비 평균(mutate, summarise)을 구해 
#내림차순(arrange)으로 정렬하고, 1~5위까지 출력하기(head)
mpg %>% 
  group_by(manufacturer) %>%
  filter(class=="suv") %>% 
  mutate(tot=(cty+hwy)/2) %>% 
  summarise(meantot=mean(tot)) %>% 
  arrange(desc(meantot)) %>% 
  head(5)

# ??? Q11. mpg 데이터의 class는 "suv", "compact" 등 자동차를 특징에 따라 일곱 종류로 분류한 변수입니다. 
# 어떤 차종의 연비가 높은지 비교해보려고 합니다. class별 cty 평균을 구해보세요.
mpg %>% 
  group_by(class) %>% 
  summarise(meancty=mean(cty))

# ??? Q12. 앞 문제의 출력 결과는 class 값 알파벳 순으로 정렬되어 있습니다. 어떤 차종의 도시 연비가 높은지 쉽게 
#알아볼 수 있도록 cty 평균이 높은 순으로 정렬해 출력하세요. 
mpg %>% 
  group_by(class) %>% 
  summarise(meancty=mean(cty)) %>% 
  arrange(desc(meancty))

# ??? Q13. 어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려고 합니다. hwy 평균이 가장 높은 회사 세 곳을 출력하세요. 
mpg %>% 
  group_by(manufacturer) %>% 
  summarise(meanhwy=mean(hwy)) %>% 
  arrange(desc(meanhwy)) %>% 
  head(3)

# ??? Q14. 어떤 회사에서 "compact"(경차) 차종을 가장 많이 생산하는지 알아보려고 합니다. 
#각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력하세요.
# 
mpg %>% 
  filter(class=="compact") %>% 
  group_by(manufacturer) %>% 
  summarise(cnt=n()) %>% 
  arrange(desc(cnt))

df<-data.frame(gender=c("m","f",NA,"m","f"),score=c(5,4,3,4,NA))
df
is.na(df)

table(is.na(df))
table(is.na(df$gender))

sum(df$score)

df %>% 
  filter(is.na(score))

dfnew<-df %>% 
  filter(!is.na(score))

mean(dfnew$score)

df %>% filter(!is.na(score) & !is.na(gender))

na.omit(df)

sum(df$score, na.rm=T)

exam<-read.csv("csv_exam.csv")
exam[c(3,8,15),"math"]<-NA #여러 행 추출시에는 c함수로 벡터화해서 추출

#exam[5,"math"]
exam

exam %>% 
  summarise(meanm=mean(math, na.rm=T))

exam %>% 
  summarise(meanm=mean(math, na.rm=T),
            summ=sum(math, na.rm=T),
            mem=median(math, na.rm=T)
            )



exam$math
#퀴즈1. 
#결측값을 math의 평균값으로 대체하라

#코드 최적화(튜닝)
av<-mean(exam$math, na.rm=T)
#exam$math <- ifelse(is.na(exam$math), mean(exam$math, na.rm=T), exam$math)
exam$math <- ifelse(is.na(exam$math), av, exam$math)
exam
exam$math[is.na(exam$math)] <- mean(exam$math,na.rm=T)

table(is.na(exam$math))

#outlier 제거
#이상치(극단치)는 먼저 결측치로 처리(간주) -> 제외한 다음 분석

#성별변수 : 3가지 -> 1가지(결측처리)
#몸무게변수 : 변수값 200kg(정상범위설정 -> 결측처리)

ol<-data.frame(gen=c(1,2,1,2,3),
           score=c(5,4,1,3,4))
ol
table(ol$gen)

ol$gen<-ifelse(ol$gen==3, NA, ol$gen)
ol

#score가 4초과시 이상치 간주
ol$score<-ifelse(ol$score>4, NA, ol$score)
ol

ol %>% 
  filter(!is.na(gen) & !is.na(score)) %>%
  group_by(gen) %>% 
  summarise(ms=mean(score))


# 데이터전처리 -> 머신러닝/딥러닝
# 10000시간 법칙

#정상범위 : 논리적(통계적) 판단 근거 
#논리적? 성인 몸무게는 40kg~150kg
#통계적? 상하위 0.3% 극단치 or boxplot에서 iqr*1.5배 벗어나면 극단치

boxplot(mpg$hwy)


boxplot(mpg$hwy)$stats

#boxplot(mpg$hwy)$stats[1]
#boxplot(mpg$hwy)$stats[5]

#12보다 작으면,  37보다 크면 => 아웃라이어

mpg$hwy<-ifelse(mpg$hwy<12 | mpg$hwy>37, NA, mpg$hwy)
table(is.na(mpg$hwy))

mpg %>% 
  group_by(drv) %>% 
  summarise(mh=mean(hwy, na.rm=T))

###########################################################################
#한국인 삶의 질 분석#

#Koweps_hpc10_2015_beta1.sav
#sav파일은 SPSS 파일

install.packages("foreign")
library(foreign)
library(readxl)
library(ggplot2)

raw_welfare<-read.spss(file="Koweps_hpc10_2015_beta1.sav", to.data.frame = T)
#복사본
welfare<-raw_welfare
head(welfare)
tail(welfare)
View(welfare)

dim(welfare)
str(welfare)
summary(welfare)


welfare<-rename(welfare, 
       sex=h10_g3,
       birth=h10_g4,
       marriage=h10_g10,
       religion=h10_g11,
       income=p1002_8aq1,
       code_job=h10_eco9,
       code_region=h10_reg7
       )

#성별에 따른 월급 차이?

table(welfare$sex)

table(is.na(welfare$sex)) #결측치 없음

#ifelse사용 sex=1 => male, sex=2 => female 값 변경
welfare$sex<-ifelse(welfare$sex==1, "male", "female")
table(welfare$sex)
qplot(welfare$sex)

summary(welfare$income)
#na 대체값, na 제외

qplot(welfare$income)

qplot(welfare$income)+xlim(0,1000)


welfare$income<-ifelse(welfare$income %in% c(0, 5000), NA, welfare$income)
table(is.na(welfare$income))

#na가 아닌 데이터에 대해 성별에 따른 급여 평균 조사
#퀴즈2
welfare %>% group_by(sex) %>% filter(!is.na(income)) %>% summarise(mean = mean(income))

welfare %>% 
  group_by(sex) %>% 
  summarise(meani = mean(income, na.rm = T))


sex_income <- welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(sex) %>%
  summarise(mean_income=mean(income))
sex_income  

ggplot(data=sex_income, aes(x=sex, y=mean_income))+geom_col()

#성별에 따른 급여 차이가 있음


#몇살때 가장 많은 급여를 받을까?
#나이에 따른 평균 월급

welfare$birth
summary(welfare$birth)
qplot(welfare$birth)

table(is.na(welfare$birth))

welfare$birth<-ifelse(welfare$birth==999, NA, welfare$birth)
table(is.na(welfare$birth))

#퀴즈3.
#age 열 추가
#age는 2015-birth+1 값으로 함
#summary, qplot출력

welfare$age<-2015-welfare$birth+1
summary(welfare$age)
qplot(welfare$age)

#나이에 따른 급여 평균
age_income<-welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(age) %>% 
  summarise(mean_income=mean(income))


ggplot(data=age_income, aes(x=age, y=mean_income))+geom_col()

ggplot(data=age_income, aes(x=age, y=mean_income))+geom_line()

#연령대(young(<30) / middle(<60) / old(>=60))

welfare<-welfare %>% 
  mutate(ageg=ifelse(age<30,"young",
                     ifelse(age<=59,"middle","old")))
welfare

table(welfare$ageg)
qplot(welfare$ageg)

#연령대별 월급 평균 출력
ageg_income<-welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(ageg) %>% 
  summarise(mean_income=mean(income))
ggplot(data=ageg_income, aes(x=ageg, y=mean_income))+geom_col()

#막대 정렬
ggplot(data=ageg_income, aes(x=ageg, y=mean_income))+geom_col()+
  scale_x_discrete(limits=c("young", "middle", "old"))

#성별에 따른 월급 차이가 연령대별로 다를까 비슷할까?

sex_income<-welfare %>% 
  filter(!is.na(income)) %>%
  group_by(ageg, sex) %>% 
  summarise(mean_income=mean(income))

ggplot(data=sex_income, aes(x=ageg, y=mean_income, fill=sex))+geom_col()+
  scale_x_discrete(limits=c("young", "middle", "old"))

ggplot(data=sex_income, aes(x=ageg, y=mean_income, fill=sex))+geom_col(position = "dodge")+
  scale_x_discrete(limits=c("young", "middle", "old"))



sex_age<-welfare %>% 
  filter(!is.na(income)) %>%
  group_by(age, sex) %>% 
  summarise(mean_income=mean(income))
sex_age

ggplot(data=sex_age, aes(x=age, y=mean_income, col=sex))+geom_line()
  
#직업군 <-> 급여 비교

welfare$code_job
table(welfare$code_job)

welfare$code_job


library(readxl)
list_job <-read_excel("Koweps_Codebook.xlsx", col_names = T, sheet=2)
list_job
dim(list_job) #직종코드 : 149개


welfare$code_job
welfare<-left_join(welfare, list_job, id="code_job")
#welfare에 list_job을 연결해라(code_job 공통 컬럼 값으로 )

str(welfare)


welfare %>% 
  filter(!is.na(code_job)) %>% 
  select(code_job, job) %>% 
  head(10)

#퀴즈3.
#직업별 월급 평균 출력

job_income<-welfare %>%  
  filter(!is.na(job) & !is.na(income)) %>% 
  group_by(job) %>%  #142개 그룹
  summarise(mi=mean(income))

job_income

top20<-job_income %>% 
  arrange(desc(mi)) %>% 
  head(20)

top20

ggplot(data=top20, aes(x=job, y=mi)) + geom_col() +
  coord_flip()


bottom10<-job_income %>% 
  arrange(mi) %>% 
  head(10)

bottom10
ggplot(data=bottom10, aes(x=job, y=mi)) + geom_col() +
  coord_flip()+ylim(0,500)


#퀴즈4
#남성 직업 빈도 상위 10개 출력
job_male<-welfare %>% 
  filter(sex == "male" & !is.na(job)) %>% 
  group_by(job) %>% 
  summarise(cnt = n()) %>% 
  arrange(desc(cnt)) %>% 
  head(10)

job_male

job_female<-welfare %>% 
  filter(sex == "female" & !is.na(job)) %>% 
  group_by(job) %>% 
  summarise(cnt = n()) %>% 
  arrange(desc(cnt)) %>% 
  head(10)

job_female

#종교가 있는 사람이 이혼을 더/덜할까???
#종교 유/무에 따른 이혼율 조사

table(welfare$religion)

welfare$religion<-ifelse(welfare$religion==1, "yes", "no")
table(welfare$religion)
qplot(welfare$religion)

table(welfare$marriage)

#이혼 여부 변수 생성
welfare$group_marriage<-ifelse(welfare$marriage==1, "marriage", 
       ifelse(welfare$marriage==3, "divorce", NA))
table(welfare$group_marriage)

table(is.na(welfare$group_marriage))

qplot(welfare$group_marriage)


religion_marriage<-welfare %>% 
  filter(!is.na(group_marriage)) %>% 
  group_by(religion, group_marriage) %>% 
  summarise(cnt=n()) %>% 
  mutate(tot_group=sum(cnt)) %>% 
  mutate(pct=round(cnt/tot_group*100,1))


divorce<-religion_marriage %>% 
  filter(group_marriage =="divorce") %>% 
  select(religion, pct)

divorce





