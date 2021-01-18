# [주피터노트북(맥북/윈도우) 한글깨짐 방지 코드](https://velog.io/@seonj102/jupyter-notebook-그래프-한글-폰트-설정)

- 참고 사이트 : [jupyter notebook - 그래프 한글 폰트 설정](https://velog.io/@seonj102/jupyter-notebook-그래프-한글-폰트-설정)

### 코드1-platform

```python
# 파이썬 시각화 패키지 불러오기
import matplotlib.pyplot as plt
%matplotlib inline


# 사용자 운영체제 확인
import platform
platform.system()


# 운영체제별 한글 폰트 설정
if platform.system() == 'Darwin': # Mac 환경 폰트 설정
    plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows': # Windows 환경 폰트 설정
    plt.rc('font', family='Malgun Gothic')

plt.rc('axes', unicode_minus=False) # 마이너스 폰트 설정


# 글씨 선명하게 출력하는 설정
%config InlineBackend.figure_format = 'retina'
```

### 코드2-os

```python
# 파이썬 시각화 패키지 불러오기
import matplotlib.pyplot as plt
%matplotlib inline


# 사용자 운영체제 확인
import os
os.name


# 운영체제별 한글 폰트 설정
if os.name == 'posix': # Mac 환경 폰트 설정
    plt.rc('font', family='AppleGothic')
elif os.name == 'nt': # Windows 환경 폰트 설정
    plt.rc('font', family='Malgun Gothic')

plt.rc('axes', unicode_minus=False) # 마이너스 폰트 설정


# 글씨 선명하게 출력하는 설정
%config InlineBackend.figure_format = 'retina'
```

## folium 한글깨짐 (pop-up)

```python
#### folium pop-up 한글 깨짐발생 할경우 설치!
pip install git+https://github.com/python-visualization/branca.git@master
```

### matplotlib로 한글 검색해서 표시하는 방법

```python
import matplotlib.font_manager as font_manager
font_list = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
font_list[:200]
```

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'NanumBarunGothic'
plt.hist(np.random.normal(50, 10, 1000))
plt.title('한글표시')
plt.show()
```

