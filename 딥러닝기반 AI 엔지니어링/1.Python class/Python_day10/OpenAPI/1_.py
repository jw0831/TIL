# The code 책을 읽어서 역사적인 흐름을 알면 앞으로의 미래를 (컴퓨터에관한) 예측할수 있다.
# pip install requests
# python 은 xml (Extensible Markup Language)과 잘 작동하기 위한 툴이 있다.
import requests
url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=keH9yQB4PoENO%2B1X167aMbP3mIsr9aKYUhdP%2FnmzgXXaHuZEJ7VbIZlUoR%2FRC%2Bf3aSSdIBH4WVVo8KobNzZ2DA%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20200310&endCreateDt=20200724&"

res = requests.get(url) #get 을 하면 변환값이 있다니까 반환값을 설정!
print(res.text)
