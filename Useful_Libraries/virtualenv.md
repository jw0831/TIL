# Python virtualenv 정리 (MacOS, Linux / Windows)

팀이 2개가 있다고 가정하자. 나는 2 팀을 이동하며 프로젝트를 진행해야 한다. 그런데 팀 1은 파이썬 버전이 2.7 이고 팀 2는 3.8일때 매번 재설치가 필요할까? 답은 아니오다.

개발환경에는 가상환경을 제공한다. 파이썬 사용자는 이제, VS-Code 활용을 추천한다~~ 왜냐하면 파이썬 창시자인 귀도 반 로섬 께서 마이크로 소프트로 입사를 하셨기 때문이다.

다음은 설치를 하기위한 사이트에서 그대로 참고 하였다.

[linux/windows 가상환경 설치 방법 정리](https://dgkim5360.tistory.com/entry/python-virtualenv-on-linux-ubuntu-and-windows)

#### 리눅스(ubuntu) 환경

ubuntu의 현재 최신 LTS 버젼인 ubuntu 16.04 LTS는 운영체제에 기본적으로 python 2.7 버젼과 3.5 버젼이 모두 탑재되어있다. 그리고 각 버젼의 실행은 다음 명령어를 통해 할 수 있다.
    
     $ python Python 2.7.12 (default, Jul 1 2016, 15:12:24) [GCC 5.4.0 20160609] on linux2 Type "help", "copyright", "credits" or "license" for more information. >>> $ python3 Python 3.5.2 (default, Sep 10 2016, 08:21:44) [GCC 5.4.0 20160609] on linux Type "help", "copyright", "credits" or "license" for more information. >>> 

그리고 python과 함께 딸려오는 것이 있는데 pypi (python package installer)이다. pip install ... 로 익숙한 그것이다. 마찬가지로 python 버젼에 따라 다음과 같이 실행하고 --version 옵션을 통해 그 버젼을 확인해볼 수 있다.  


     $ pip --version pip 8.1.2 from /home/user/.local/lib/python2.7/site-packages (python 2.7) $ pip3 --version pip 8.1.2 from /home/user/.local/lib/python3.5/site-packages (python 3.5) 

그럼 이제 가상환경을 사용하기 위한 가상환경 모듈 virtualenv를 설치하자. 아마도 sudo와 함께 써야할 것이다.  


     # python 2.7 $ pip install virtualenv # python 3.5 $ pip3 install virtualenv 

이제 virtualenv가 설치되었고, 바로 쉘에서 다음과 같이 가상환경을 시작할 수 있다.
    
     $ virtualenv venv Running virtualenv with interpreter /usr/bin/python New python executable in /home/don/venv/bin/python Installing setuptools, pip, wheel...done. 

위 작업이 완료되면 내가 지정했던 venv라는 폴더가 생성되고 그 안에 새로 python이 설치되어있음을 알 수 있다. 이제 venv를 가동시키고, 정말로 새로운 python 환경이 생겼는지 확인해보겠다.
    
     $ source venv/bin/activate (venv) $ pip list pip (8.1.2) setuptools (28.7.1) wheel (0.30.0a0) 

여기서 두 가지를 확인할 수 있다. 첫 번째로, source 명령어를 통해 venv 가상환경의 activate를 실행하니 그 다음부터는 쉘 명령창 앞부분에 (venv)가 따라 붙어다니는 것을 볼 수 있다. 이는 이제부터 venv 가상환경 안에 있는 거라고 말해주는 것이다. 두 번째로, venv 안에서 설치된 모듈을 pip list 명령을 통해 확인한 결과... 아무것도 없다는 것이다. pip, setuptools, wheel은 가상환경을 시작할 때 기본으로 설치된 것이다. (이미 pip list를 쓰고 있지 않은가)

한 가지 궁금증이 생길 법한 것이 있는데, 다시 한 번 버젼 문제이다. 2버젼, 3버젼의 python 가상환경을 쓰려면 어떻게 해야하나? 다음과 같은 방안을 쭉 나열해본다. 맘에 드는 방법으로 쓰면 된다.
    
     # python 2 $ python -m virtualenv venv $ virtualenv venv --python=python $ virtualenv venv --python=python2.7 # python 3 $ python3 -m virtualenv venv $ virtualenv venv --python=python3 $ virtualenv venv --python=python3.5 

이제 내가 사용하고자 하는 모듈을 맘대로 설치하면 된다. 그 설치한 목록은 다음 명령어를 통해 정확한 리스트로 저장해두자.
    
     (venv) $ pip freeze > requirements.txt 

이제 requirements.txt 파일에서 설치된 모듈과 그 버전이 리스트되어 저장되어 있음을 알 수 있다.  


가상환경을 나가고 싶으면 간단히 `deactivate`라고 명령하면 된다.

  


#### 윈도우 환경

사실 윈도우라고 다를 것은 없다. 기본적으로 python을 설치하면, 자동적으로 pypi가 함께 설치되기 때문에 위 리눅스일 때와 동일하게 virtualenv를 설치하고 시작할 수 있다.  


     > pip install virtualenv > virtualenv venv 

이제 activate해야 하는데, 여기서는 `source` 대신 `call`
    
     > call venv/scripts/activate (venv) > pip list 

가상 환경이 잘 시작되었음을 확인할 수 있을 것이다.

  

출처: [https://dgkim5360.tistory.com/entry/python-virtualenv-on-linux-ubuntu-and-windows](https://dgkim5360.tistory.com/entry/python-virtualenv-on-linux-ubuntu-and-windows) [개발새발로그]

위 사이트와 같이 가상환경 시스템이 구축 되었다면, 이제 파이썬 버전을 이동해 가면서 개발을 순조롭게 진행할 수 있다.