# script window
print('hello')

# install.packages("readxl") #install one time only!


# create vector
eng <- c(50,60,70) #vector
mat <- c(70,80,90)

df<-data.frame(eng, mat)
df

class<-c(1,1,2)
dfm<-data.frame(eng,mat,class)
dfm

mean(dfm$eng) #데이터프레임 $ 컬럼명

library(readxl)
read_excel("Data/excel_exam.xlsx")

read_excel("Data/excel_exam_novar.xlsx", col_names = F) #col_names = False

#if you need to specify sheet from many sheets
# default is sheet1, i want to read sheet3
read_excel("Data/excel_exam_sheet.xlsx", sheet = 3)

data<-read.csv("Data/csv_exam.csv")
str(data) #str = structure 구조 확인 할때 

write.csv(data, file="savefile.csv") # to save file in csv format

exam <- read.csv("Data/csv_exam.csv")
head(exam)
tail(exam)
View(exam) # capital V!!!

dim(exam) # .shape (20, 5)
dim(exam)[1]
dim(exam)[2]

summary(exam)

# install.packages("dplyr")
library(dplyr) # -> %>% 포함한다.
help(dplyr)

# exercise: create DataFrame and change names
exam

reexam<-rename(exam, eng=english)
reexam

reexam$plus_me<-reexam$math+reexam$eng
reexam

reexam$result=ifelse(reexam$math>=70, "pass", "fail") #(similar to) np.where 
reexam

install.packages("ggplot2")
library(ggplot2)
qplot(reexam$result)

#ifelse를 중첩시켜서 조건문을 완성. (math<=50 => 'C', math<=80 => 'B', math<=100 => 'A')
reexam$hakjum<-ifelse(reexam$math<=50, "C",
                      ifelse(reexam$math<=80, "B", "A"))
reexam

table(reexam$hakjum) #(similar to) pandas -> value_counts()

exam<-read.csv("Data/csv_exam.csv")
exam

exam %>% filter(class==1)  #cmd+shift+m (%>% pipeline)  filtering 
exam %>% filter(class!=1)
exam %>% filter(math>=70 & english>=70)
exam %>% filter(math>=70 | english>=70)

exam %>% filter(class==1 | class==3)
exam %>% filter(class %in% c(1,3,5))

exam %>% select(math)
exam %>% select(math, class)
exam %>% select(-math)
exam %>% select(-math, class)
exam %>% select(-math, -class)

exam %>% 
  filter(class==1) %>% 
  select(english)

exam %>% 
  select(id, math) %>% 
  head
##############################################################################
# 정렬
exam %>%
  arrange(math) #sort: default ascending

exam %>% 
  arrange(desc(math))

exam %>% 
  arrange(class, math)
##############################################################################
# 파생변수 추가 #feature engineering
exam %>% 
  mutate(total=math+english+science,
         mean=total/3) %>% 
  head

exam %>% 
  mutate(res=ifelse(science>=60, "pass", "fail")) %>% 
  head
##############################################################################
#집계
exam %>%  
  summarise(mean_math=mean(math))

#groupby -> 집계
exam %>% 
  group_by(class) %>% 
  summarise(mean_math=mean(math))

#groupby -> 집계
exam %>% 
  group_by(class) %>% 
  summarise(mean_math=mean(math),
            sum_math=sum(math),
            median_math=median(math),
            n=n()) #빈도
#max, min, sd(표준편차), var(분산),...
##############################################################################
ggplot2::mpg 
# 패키지명::데이터셋  패키지마다 연습용 데이터가 제공된다

mpg<-as.data.frame(ggplot2::mpg) #R 에서도 데이터프레임을 많이 사용한다.
str(mpg)  
mpga<-mpg %>% 
  filter(displ <=4)

mpgb<-mpg %>% 
  filter(displ >5)

mean(mpga$hwy)

a<-data.frame(id=c(1,2),
              test=c(50,90))

b<-data.frame(id=c(3,4),
              test=c(30,100))
##############################################################################
bind_rows(a,b) #merge/concat

exam

name<-data.frame(class=c(1,2,3,4,5),
           tea=c("kim","park","lee","cho","jung"))
name


# class 기준 exam과 name을 결합
left_join(exam, name, by='class')