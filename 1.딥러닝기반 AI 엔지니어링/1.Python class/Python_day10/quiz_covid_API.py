# 시험은 목요일:

# * 코로나바이러스감염증 감염현황 조회 서비스
########################################
#1. 기간별 조회
#2. 사망자 조회
#3. 종료
########################################
# 메뉴를 선택해주세요. (1-3):
'''
# 기간은 20200303부터 20200723일 까지임.
# 1. 선택시
# 시작기간을 입력해주세요. : 20200301
# 종료기간을 입력해주세요. : 20200304
# 2. 선택시
# 사망자가 몇명이상 되는 경우: 20(명이상)
# 3. 선택시 종료
# %Tkinter UI로 작성해도 가능함.
<item>
<accDefRate>0.9383340224</accDefRate>
<accExamCnt>1510327</accExamCnt>
<accExamCompCnt>1489768</accExamCompCnt>
<careCnt>864</careCnt>
<clearCnt>12817</clearCnt>
<createDt>2020-07-24 11:05:47.968</createDt>
<deathCnt>298</deathCnt>
<decideCnt>13979</decideCnt> #확진자 수 
<examCnt>20559</examCnt>
<resutlNegCnt>1475789</resutlNegCnt>
<seq>209</seq>
<stateDt>20200724</stateDt>
<stateTime>00:00</stateTime>
<updateDt>null</updateDt>
</item>
'''
import time
import requests
import xml.etree.ElementTree as xml


class appManager():
    def schByPeriod(self, p1, p2):
        self.period1 = p1
        self.period2 = p2
        url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=keH9yQB4PoENO%2B1X167aMbP3mIsr9aKYUhdP%2FnmzgXXaHuZEJ7VbIZlUoR%2FRC%2Bf3aSSdIBH4WVVo8KobNzZ2DA%3D%3D&pageNo=1&numOfRows=10&startCreateDt={}&endCreateDt={}&".format(self.period1, self.period2)
        res = requests.get(url)
        root = xml.fromstring(res.text)
        # for item in root:
        #     print(item.tag)
        data = [] #list
        for items in root.iter("items"):
            for item in items:
                j={} #dictionary in list!
                for i in item:
                    j[i.tag] = i.text
                data.append(j)
        
        # print(data[0])
        
        #이걸
        for itemGet in data[0]:
            print(itemGet)

        #한방에 하려면 list.conf 사용한다!

        names = [itemGet for itemGet,_ in data[0]] # _언더스코어의 의미는 뒤에꺼 안본다는 뜻 / 알맞게 사용하는법 알아보기
        print(names)

        # len(data)
        # print(data['decideCnt'])
        # print("{}~{} 확진자수: ".format(self.period1, self.period2))
        
    def schDth(self):
        pass
    

class mainApp():
    def run(self):
        self.clientSvc = appManager()

        while True:
            print("* 코로나바이러스감염증 감염현황 조회 서비스")
            print("########################################")
            print("#1. 기간별 조회")
            print("#2. 사망자 조회")
            print("#3. 종료")
            print("########################################")
            sel = input("# 메뉴를 선택해주세요. (1-3): ")
            print(sel, "번 입력하였습니다.")
            if sel == '1':
                print("기간별 조회를 시작합니다.")
                self.p1 = input("시작기간을 입력해주세요. ex) 20200302: ")
                self.p2 = input("종료기간을 입력해주세요. ex) 20200724: ")
                self.clientSvc.schByPeriod(self.p1, self.p2)
                time.sleep(1)
                print("")

            elif sel == '2':
                print("사망자 조회를 시작합니다.")
                
                time.sleep(1)
                print("")
            elif sel == '3':
                print("종료합니다~")
                time.sleep(1)
                break
            else:
                print("잘못입력했어요")
                print("")    
        
if __name__ == "__main__":
    app = mainApp()
    app.run()

