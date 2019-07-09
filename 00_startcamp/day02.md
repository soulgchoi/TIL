# day02

# Git

## what is git

git : **scm** (source code manager) / **vcs** (version control system)

git; 버전관리를 해주는 감시카메라

1. 폴더의 버전관리

   - `git init` > 폴더 관리 시작

   ![1562632906322](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562632906322.png)

   - (master) > 폴더가 관리되고 있음

   - `git add OO` > 감시카메라에 등록!

   - `git status` 로 등록 확인

     - 변경사항이 없을 때와 있을 때 차이

     빨간색 메세지가 뜬다 > 사진 찍을 준비가 안됐다! 

     이때 잠깐만! 의 의미가 **add** 

     add 하고 commit 가능

     - 윗줄은 add 한 상태, 아래는 안된 상태

     ​	![1562635621419](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562635621419.png)

     ​	이 때 commit 하면 위에만 남음

   - 메세지를 남겨놓으면 왜 버전을 나눴는지 알 수 있을 것임

     `git commit -m '~~~했음'`

     - git에서 user 등록 필요

       `git config --global use.email(/name)`

     사진찍기(버전 남기기)

   - 갤러리는 어디에 있나요?

     - `git log`

   - **순서대로 정리하기**

     `git init`

     `git add <filename>`

     `git commit -m '<message>'`

     변경사항 저장

     `git add <filename>`

     `git commit -m '<message>'`

     ...

     `git status`; 상태 물어보는 명령어

     `git log`; 사진(commit)들 로그를 보여줌

     

   * 상위폴더를 관리하면 하위폴더는 자동으로 관리된다.

   * `git add -A`=`git add .`; 통째로 관리하기

   

2. 다른 명령어

   - `cd (..)` > 한 단계 상위로 나가기

   - `cd OO` > 폴더 이동

   - `mkdir OO` > OO폴더(==디렉토리) 만들기

   - 대충 입력하다 탭탭 > 입력하다 탭 > 자동완성

   - `touch OO.확장자` > 생성

   - `rm OO` > 삭제

   - `ls` > 리스트

   - <u>띄어쓰기로 구분</u>

3. github에 백업하기

   `git remote add origin https://github.com/soulgchoi/practice_git.git`

   `git push -u origin master`



* github/bitbucket/gitlab



