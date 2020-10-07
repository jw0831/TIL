library(dplyr)
library(readxl)
# Q1
raw_welfare<-read.spss(file="Data/Koweps_hpc10_2015_beta1.sav", to.data.frame = T)
welfare<-raw_welfare
welfare<-rename(welfare, 
                sex=h10_g3,
                birth=h10_g4,
                marriage=h10_g10,
                religion=h10_g11,
                income=p1002_8aq1,
                code_job=h10_eco9,
                cide_region=h10_reg7)
welfare$age<-2015-welfare$birth+1
welfare<-welfare %>% 
  mutate(ageg=ifelse(age<30,"young",
                     ifelse(age<=59, "middle", "old")))
welfare$ageg

welfare %>% 
  filter(cide_region==1) %>% 
  group_by(ageg) %>% 
  summarise(cnt=n()) %>% 
  mutate(tot_group=sum(cnt)) %>% 
  mutate(pct=round(cnt/tot_group*100,1))

# Q2
mpg <- as.data.frame(ggplot2::mpg)
mpg
mpg[c(65, 124, 131, 153, 212), "hwy"] <- NA
sum(is.na(mpg$drv))   # 0
sum(is.na(mpg$hwy))   # 5
mpg %>% 
  filter(!is.na(hwy)) %>% 
  group_by(drv) %>% 
  summarise(mean_hwy_drv=mean(hwy)) %>% 
  arrange(desc(mean_hwy_drv))

# Q3
mpg <- as.data.frame(ggplot2::mpg)
mpg[c(10, 14, 58, 93), "drv"] <- "k"
mpg[c(29, 43, 129, 203), "cty"] <- c(3, 4, 39, 42)
sum(is.na(mpg$drv))
sum(!is.na(mpg$drv))
sum(is.na(mpg$cty))
mpg<-mpg %>% 
  filter(mpg$drv!="k")
sum(!is.na(mpg$drv))

mpg$drv<-ifelse(welfare$drv %in% c(10,14,58,93), NA, drv)

boxplot(mpg$cty)
boxplot(mpg$cty)$stats
mpg$cty<-ifelse(mpg$cty<9 | mpg$cty>26, NA, mpg$cty)
table(is.na(mpg$cty))
mpg<-mpg %>% 
  filter(!is.na(mpg$cty))
boxplot(mpg$cty)

mpg %>% 
  filter(!is.na(drv) & !is.na(cty)) %>% 
  group_by(drv) %>% 
  summarise(mean_drv_cty=mean(cty))
