# wink-official
국민대학교 소프트웨어융합대학 웹 학술동아리 WINK 공식 웹 사이트

# WINK Github-flow방식을 따릅니다.

## master branch

master branch는 항상 stable한 상태로 최신의 상태여야 합니다. 직접적으로 Product에 배포 되는 branch입니다.


## 새로운 issue 발생
issue를 기반으로 branch를 나눕니다.
각 branch간 confilct를 최소화 하기위해 철저히 기능을 구분합니다. 따라서 master에서만 pull을 받아 branch를 생성합니다.

issue가 생겼을 때의 작업 과정은 다음과 같습니다.
 1. issue를 생성하고, 제목에는 간단한 작업에 대한 명시, 내용에는 자세한 사항을 서술합니다.
 2. master에서 pull을 받아 branch를 생성합니다.
 3. 자신의 local branch에서 origin branch로 수시로 push를 합니다.
 4. 피드백을 받아야하거나 작업이 완료되어 merge를 해야할 때는 pull request를 생성합니다.
 5. 코드 리뷰와 피드백이 끝난 후 master로 merge합니다.
 6. CI 배포 자동화로 자동 배포.
 

## PyCharm Django setting
 #### 가상환경 세팅
  1. sudo python3 -m virtualenv [가상환경을 설치할 경로]
  2. source [경로]/bin/activate 를 하여 가상환경에 접속합니다.
 
 #### 설치
  1. settings.py를 프로젝트 내 outsourcing_solution/settings.py로 저장합니다.
  2. 가상환경에서 sudo pip3 install -r requirement.txt를 실행합니다.
    - mysqlclient가 설치되지 않을 때.
      - brew install mysql을 한 후 다시 설치를 시도합니다. 
      - brew 설치 가이드 -> https://brew.sh/index_ko
      

 ### 프로젝트 실행 
 1. 우측 상단의 edit configuration 버튼을 클릭합니다.
 2. 창이 새로 떳다면 좌측 상단의 + 버튼을 누르고 Django server를 클릭합니다.
 3. Host를 0.0.0.0으로 설정합니다.
