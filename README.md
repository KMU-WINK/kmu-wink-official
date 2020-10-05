# WINK 공식 웹 사이트

# 프로젝트 소개

<img align="left" width="180" height="180" src="https://wink.kookmin.ac.kr/static/assets/logo/wink-color.png"></img>
**프로젝트 명 : WINK 공식 웹 사이트(kmu-wink-official)**
---
본 웹 사이트는 python django를 기반으로 하는 WINK 공식 웹 사이트이다. 본 웹 사이트는 동아리 내 정보 공유 및 프로젝트 성과 기록, 스터디 자료실, 동아리 소개를 목적으로 한다.

## 업무 진행 방식

### master branch

master branch는 항상 stable한 상태로 최신의 상태여야 합니다. 직접적으로 Product에 배포 되는 branch입니다.


### 새로운 issue 발생
issue를 기반으로 branch를 나눕니다.
각 branch간 confilct를 최소화 하기위해 철저히 기능을 구분합니다. 따라서 master에서만 pull을 받아 branch를 생성합니다.

issue가 생겼을 때의 작업 과정은 다음과 같습니다.
 1. issue를 생성하고, 제목에는 간단한 작업에 대한 명시, 내용에는 자세한 사항을 서술합니다.
 2. master에서 pull을 받아 branch를 생성합니다.
 3. 자신의 local branch에서 origin branch로 수시로 push를 합니다.
 4. 피드백을 받아야하거나 작업이 완료되어 merge를 해야할 때는 pull request를 생성합니다.
 5. 코드 리뷰와 피드백이 끝난 후 master로 merge합니다.
 6. CI 배포 자동화로 자동 배포.
 

### PyCharm Django setting
 #### 가상환경 세팅
  1. sudo python3 -m virtualenv [가상환경을 설치할 경로]
  2. source [경로]/bin/activate 를 하여 가상환경에 접속합니다.
 
 #### 설치
  1. settings.py를 프로젝트 내 outsourcing_solution/settings.py로 저장합니다.
  2. 가상환경에서 sudo pip3 install -r requirement.txt를 실행합니다.
    - mysqlclient가 설치되지 않을 때.
      - brew install mysql을 한 후 다시 설치를 시도합니다. 
      - brew 설치 가이드 -> https://brew.sh/index_ko
      

 #### 프로젝트 실행 
 1. 우측 상단의 edit configuration 버튼을 클릭합니다.
 2. 창이 새로 떳다면 좌측 상단의 + 버튼을 누르고 Django server를 클릭합니다.
 3. Host를 0.0.0.0으로 설정합니다.

# 윙크 공식 홈페이지 개발팀
## 팀원 소개

<img align="left" width="165" height="165" src="https://wink.kookmin.ac.kr/static/images/upload/ACF13837-13AE-4D45-878D-232B94553B24_1_105_c_lgyEbPJ.jpeg"></img>
```

17학번 이종휘

Role : 프로젝트 매니저, 백엔드 프로그래밍, 디자인
GitHub : https://github.com/bell2lee

```

<img align="left" width="165" height="165" src="https://wink.kookmin.ac.kr/static/images/upload/beauty_20190608195952.jpg"></img>
```

15학번 송준호

Role : 백엔드 프로그래밍, 퍼블리싱, 프로덕트 테스터
GitHub : https://github.com/Song-Joonho

```

<img align="left" width="165" height="165" src="https://wink.kookmin.ac.kr/static/images/upload/29365057.jpeg"></img>
```

17학번 김규리

Role : 백엔드 프로그래밍, 퍼블리싱, 디자인
GitHub : https://github.com/kimgyuri

```

<img align="left" width="165" height="165" src="https://wink.kookmin.ac.kr/static/images/upload/34D1B7FD-CB8E-428E-84E1-BC27E3F47B48.png"></img>
```

18학번 정소원
Role : 백엔드 프로그래밍, 퍼블리싱, 디자인, 기획
GitHub : https://github.com/sowish23

```

## 참조(Reference)

#### PAPER


## Contatc Us
``` Email : kmucs.wink@gmail.com ```