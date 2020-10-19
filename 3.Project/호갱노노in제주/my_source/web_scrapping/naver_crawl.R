install.packages("rvest")

install.packages("RSelenium")
install.packages("httr")
library(rvest)
library(RSelenium)
library(httr)
help(httr)

pJS <- wdman::phantomjs(port = 4567L)
# pC <- wdman::chrome(port = 4445)

# remDr <- remoteDriver(remoteServerAdd="localhost", port=4445, browserName="chrome")
remDr <- remoteDriver(port=4567L, browserName="phantomjs") #시작
remDr$open() #시작 

remDr$navigate("https://m.place.naver.com/restaurant/35014081/review/visitor?entry=plt") #페이지 이동
remDr$getTitle()[[1]]
# url<-"https://map.naver.com/v5/search/88%EB%8F%BC%EC%A7%80/place/35014081?c=14079796.1564148,3960520.1268538,15,0,0,0,dh&placePath=%3F%2526"
# con <- httr::GET(url)
# tt<-httr::content(con, "text")
# tt

html <- remDr$getPageSource()[[1]] #list ▶ vector형식으로 추출

#동적 ▶ 정적 리로드
html <- read_html(html) #library(rvest)필요.

sWord <- html_nodes(html,"span.WoYOw")
View(sWord)
rank <- html_text(sWord)
rank
length(rank)

#정지 
remDr$close()
#종료
pJS$stop()
# R 에서 동적 추출하면 