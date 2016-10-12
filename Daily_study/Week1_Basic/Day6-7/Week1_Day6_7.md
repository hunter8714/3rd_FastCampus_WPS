Week1_Day6~7. Git/ GitHub
==

## 0. 목차
>1. 실습
2. 정리

## 1. 실습

######Week1 6~7일차는 git생성과 그 사용법, 그리고 Markdown 작성 문법을 배우고 실습 위주로 진행하였습니다.

## 2. 정리
#### 2.1. push
- git init 으로 시작
- remote add origin 원격 저장소와 local 저장소를 연결하는 명령어.
- git add 명령어로 table에 commit.
- git commit 명령어 -m " " 옵션으로 직접 commit 메세지 입력 가능.
- git push origin master 명령어로 push 가능.

 - origin 은 remote에 있는 원격 저장소를 의미합니다. master 는 master branch를 의미합니다. 
 
#### 2.2. pull
- git clone url주소 명령어로 해당 url(원격저장소url) 에서 끌어올 준비를 한다.
- git pull origin master 명령어로 master branch에서 끌어온다. 

#### 2.3. branch : 가지치기
```
1. git branch
: 로컬 저장소의 branch 목록 보기
2. git branch -r
: 원격 저장소의 branch 목록 보기
3. git branch branch_name
: 새로운 branch 만들기
4. git checkout branch_name
: 작업 트리 이동
5. git merge branch_name
: 합치기 - merge
6. git branch -d branch_name
: merge된 branch 삭제
```

pull : 가져오자마자 mix(가공) 시킨 느낌. 서버에서 바뀐 것이 있는지 확인하고 가져오기까지. 

fetch : 데이터를 가져와서 서버에서 바뀐것이 있는지 확인하는 것. 가져오는 것 까진 하지만 merge를 하지 않는 것.

#### 2.4. checkout : 가지 이동 명령어
```
- commit log 보기

1. git reflog

2. git checkout (commit_id)

3. git checkout -b <name>

- branch 만들고 commit 상태 되돌리기 

1. git branch <name> (commit_id)

2. git checkout <name>
```

#### 2.5. reset : 되돌리기
```
- commit log 보기
1. git reflog

- HEAD 상태로 이동
git reset --soft HEAD~
: 바로 전 HEAD로 이동

2. git reset HEAD@{2} <file>
: 2번 HEAD로 이동

3. git reset HEAD <file>
:  스테이지로 이동된 변경사항 되돌리기


```

#### 2.6 Markdown

마크다운은 일반 텍스트 문서의 양식을 편집하는 문법이다. README 파일이나 온라인 문서, 혹은 일반 텍스트 편집기로 문서 양식을 편집할 때 쓰인다. 마크다운을 이용해 작성된 문서는 쉽게 HTML 등 다른 문서 형태로 변환이 가능하다.
```
문법 1. # 텍스트

- #을 하나 쓰면 HTML의 <h1> 태그를,
   #을 두개 쓰면 <h2>의 태그를 의미한다.

- 즉, #은 하나에서 여섯개까지 쓸 수 있고, #이 늘어날 때마다 제목의 수준은 내려간다. (보통 글씨 크기가 작아진다. )
```
```
문법 2. 리스트

1. 번호없는 리스트
  문법 : -/+/* 텍스트
2. 번호 없는 리스트
  문법 : 숫자, 텍스트
```
```
문법 3. 텍스트 강조
1. 이탤릭
 문법 : *텍스트* , _텍스트_

2. 볼드체
문법 : **텍스트**, __텍스트__

하나는 이탤릭, 두개는 볼드체
```

**인용**<br>
문법 : > 텍스트

```
링크
1. 인라인 링크
문법 : [텍스트] (링크주소)
2. 참조 링크
문법 : [텍스트][참조명]
          [참조명]:링크주소

3. 이미지
문법 : ![텍스트](이미지링크)

< 소스 코드 >

문법 : ` ` ` 언어
          코드
          ` ` `
 - 언어에는 소스코드에 해당되는 언어를 넣어준다. objective-c, python, sh, java 등..
 - 코드 내용의 문법에 맞게 색상이 자동 추가된다.
 ```