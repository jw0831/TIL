# AWS

EC2: Elastic Compute Cloud

- 아마존의 인스턴스(컴퓨터)를 임대하는 서비스

- 사용시 인스턴스를 잘 모니터링 해야함 (과금 우려)
- Azure (Microsoft) 유사서비스
- 생성이 되는지역과 안되는 지역이 구분되어있다.
- 거주하는 지역의 인스턴스가 가장 빠르다.

루트 사용자 (최고 관리자)

- IAM 사용자 



# 순서

1. AWS Management Console
   1. find service : EC2 dashboard
   2. 제한 tab
      1. ex: All G Spot instance Requests 현재 제한 `0vCPU` 일경우 1대 만 가능
   3. 인스턴스 tab
      1. 만들어 진것이 없을경우 : 이 리전에는 인스턴스가 없음
      2. 생성, 연결 (다양한 방법 : 직접/클라우드)
         1. Xshell 연결 프로그램을 통하여 연결 (`리눅스` 지식 필요)
      3. 생성하는법
         1. Amazon Machine Image (AMI) 선택
            1. 이미 만들어져 있는 환경 선택 (프리 티어 사용 가능: 일정 사용량 지나면 요금 부과, 기간 1년 제한)
            2. Ubuntu Server 20.04 LTS (Long Term Service) 64bit 선택
         2. 인스턴스 유형 선택
            1. 그룹 마다 특징이 있다. (Z, X, ... 특정 작업에 최적화 되어있는 용도가 그룹마다 다르다)
            2. vCPUs를 보아야한다 (가상환경 수)
            3. t2.micro 선택 (이유는 연습용)
         3. 인스턴스 세부 정보 구성
            1. 퍼블릭 IP 자동 할당 -> 활성화
         4. 스토리지 추가
            1. 용량 설정 (30gb)
         5. pass
         6. 보안 그룹 구성
            1. 기존에 생성된 것은 사용할 수 있음
            2. 보안그룹 이름 생성 testteam1, 설명 동일
         7. 인스턴스 시작 검토
            1. 시작버튼 클릭
            2. 기존 키 페어 선택 또는 새 키 페어 생성
               1. 퍼블릭(자물쇠)/프라이빗(열쇠) 키
               2. 퍼블릭키 (AWS 소유)
               3. 프라이빗키 (내소유)
            3. 새 키 페어 생성
               1. 키 페어 이름 : 지정 -> 키 페어 다운로드
            4. 인스턴스 시작!
         8. 시작 상태 검토 

## Xshell 

https://www.netsarang.com/ko/free-for-home-school/

- 새 세션 등록 정보
  - 사용자 인증 -> public key 만 체크
  - 사용자 이름 ubuntu
    - 설정 버튼 -> public key 설정 키 페어
  - 연결 버튼



### AWS

- anaconda 에서 linux version 의 링크 주소 복사 -> wget을 통해서 아마존 리눅스에 설치

실행:

순서 참고 : [설치 방법](https://assaeunji.github.io/aws/2020-03-20-aws-python/)

강사님에 강조 하신 부분:

sudo sh Anaconda3 정보 입력~. sh

please answer 'yes' or 'no' 나올때 까지 엔터

sudo /home/ubuntu/anaconda3/bin/pip install jupyter

![](https://assaeunji.github.io/images/aws-python-ipython.png)

중요!!! : 'shal:~~~~'

이 순서로 키보드를 누릅니다.

  1. `Shift+G`: `jupyter_notebook_config.py`의 파일의 끝 줄로 이동합니다.
  2. `o` (알파벳 소문자 o): 파일의 마지막 줄의 다음 줄로 이동하고 **입력 모드**로 바뀝니다. (창에 `--INSERT--`라 뜹니다!)
  3. 이 후 다음과 같이 입력합니다. 여기서 `c.NotebookApp.password`의 값은 `u'sha로 시작하는 Output 값'`을 써주셔야 합니다.

```shell
c = get_config() c.NotebookApp.password = u'sha1:c089616e1c09:fd4b51ff08d9bf6ef4b82d1a4fa3716cc640fb14' 
c.NotebookApp.ip = '*' 
c.NotebookApp.open_browser = False 
c.NotebookApp.port_retries = 8888 c.NotebookApp.notebook_dir = u'/home/ubuntu' 
```

  4. `Esc`: 입력모드에서 명령모드로 나오는 명령어입니다.
  5. `:wq` + `Enter`: 저장 후 `vi`모드를 종료하는 명령어입니다.

수정 후 `vi`편집기에서 나오면 다시 XShell 창에 다음과 같이 입력해서 Jupyter Notebook을 실행합니다.
    
```shell
sudo jupyter-notebook --allow-root& 
```


**네트워크 보안 그룹** 까지 예시를 따라하자!

주피터 노트북을 아무나 못 사용하게 하려면 **인바운드 규칙 편집** 필요





## 참고 사이트

- https://assaeunji.github.io/aws/2020-03-20-aws-python/
- https://assaeunji.github.io/aws/2020-03-16-aws-python/
- https://memoming.com/22

