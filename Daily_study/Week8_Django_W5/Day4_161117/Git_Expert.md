Week8_Day4. Git Expert
==



## 0. 목차
> 1. 이론 - GIT의 목표/개념/명령어
> 2. 실습 - 협업



## 1. 이론

#### 1.1. GIT의 목표
- 빠른 속도 / 단순한 구조
- 비선형적인 개발(수천 개의 동시 다발적인 브랜치)
- 완벽한 분산

#### 1.2. 개념& 명령어

##### 1.2.1. Git을 구성하는 3가지 object<br>

- Blob —> Git에서는 모든 파일을 Blob이라는 단위로 관리. Blob은 텍스트 파일일 수도 있
고 이미지 파일일 수도 있음<br>
- Tree —> Blob들을 모아 놓은 것을 Tree<br>
  Tree에는 Blob뿐만 아니라 Tree가 있을 수도 있음
- Commit<Br>
author, committer —> commit을 최초 작성한사람, 수정한 사람을 나타냄. 이 값에 시
간이 timestamp값으로 들어가 있어 commit의 해시 값이 중복되지 않을 수 있음.<br><br>
repo tree —> Git으로 관리하는 repository의 tree. 즉, 최상위 폴더의 tree이다.<br><br>
parent commit —> 부모 commit의 해시 값을 가지고 있음
• 이렇게 세가지의 요소가 있는데 모두 고유의 SHA-1해시 값을 ID처럼 사용

1.2.2. 명령어

> -Commit

> - Repository

> - Checkout

> - Pull

> - Branch

> - Merge - 3way Merge / Fast Forward Merge



## 2. 실습

#### 협업 - conflict / pull request / rebase & merge / 


