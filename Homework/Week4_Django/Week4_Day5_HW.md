Pyenv재설치, Django 설정하기
====

##**1. 목표**
- pyenv 를 완전히 삭제하고 초기설정 부터 django 설치 및 설정까지 완료.

<br><br>

## 2. 과정
> - pyenv전체삭제 
> - pyenv재설치
> - pyenv에 파이썬 3.4.3설치 
> - 가상환경생성 
> - pip로 장고설치 
> - 장고프로젝트생성 
> - 파이참으로 프로젝트폴더 열기 
> - 해당 프로젝트에 가상환경 인터프리터 세팅

<br><br>

## 3. 실습
###pyenv 삭제
`rm-rf ~/.pyenv`
명령어를 통해 pyenv폴더를 날려버린다.<br>

```
➜  ~ git:(master) ✗ cd ~/.pyenv
cd: no such file or directory: /Users/Song/.pyenv
```

mac유저는 brew로 설치를 진행했기 때문에 삭제를 할때도 brew를 통해서 삭제를 해야한다. 
/usr/local/var/pyenv/에 저장이 되기 때문.
<br>
`✗ brew uninstall pyenv` 
```
Uninstalling /usr/local/Cellar/pyenv/1.0.1... (517 files, 2.2M)
pyenv:11: command not found: pyenv```

###pyenv 재설치
homebrew를 이용해 재설치를 진행한다.<br><br>
`
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
<br><br>
다운로드가 끝나면 설치를 진행한다.
```
brew update
brew install pyenv
```
설치가 끝나고 pyenv를 쳐보면 설치가 완료 되어있음을 볼수있다.
```  
~ git:(master) ✗ pyenv
pyenv 1.0.2
Usage: pyenv <command> [<args>]```


~/.bash_profile을 열어서 다음과 같은 문장을 넣어준다.
```
 export PYENV_ROOT=/usr/local/var/pyenv

if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi

if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi```

###virtualenv 가상환경 만들기
virtualenv를 설치해주자.

`~ git:(master) ✗ brew install pyenv-virtualenv`

사용하기 편하도록 도와주는 xcode와 readline을 설치해주자. <br>

`
xcode-select --install`

`brew install openssl readline xz
`

콘솔창을 다시 실행시킨 후 pyenv의 버전을 확인한다.

`pyenv versions`

```
➜  ~ git:(master) ✗ pyenv versions
  system (set by /usr/local/var/pyenv/version)```

기본버전만 설치되어있다는 것을 확인할 수 있다.
그렇다면 사용할 pyenv의 버전을 골라 설치해보자.

`pyenv install 3.4.3`

pyenv versions로 제대로 설치가 완료된 것을 확인했다면 가상환경을 지정할 디렉토리를 만들어줘야한다.
<br>

mkdir명령어로 만든 폴더로 이동한 후 로컬 명령어를 통해 그 가상환경을 돌려주자.

`pyenv local django2`

```
➜  ~ git:(master) ✗ pyenv local django2
(django2) ➜  ~ git:(master) ✗
```
다음과 같이 앞에 django2라는 이름이 붙은 것을 볼 수 있다.

이제 여기에 pip명령어를 통해 django를 설치해주자.

`pip install django`

django가 설치되었다면 이제 프로젝트를 생성한다.

`django-admin startproject mysite`

앱을 추가하고 싶다면 project대신에 app을 써주면 된다.

이제 pycharm을 실행시켜주고 open으로 자신이 만들었던 디렉토리를 열어준다.

>- 왼쪽 상단에 root directory를 우클릭하고 mark directory as 에서 source root를 클릭해준다. 이 설정은 새로 생성되는 앱들이 항상 루트 디렉토리 아래쪽로 생성되게 해준다.
>- 왼쪽 상단에 pycharm글자를 눌러주고 preference를 눌러준다.
>- Preference -> Project -> Project Interpreter -> show all -> add local -> /usr/local/var/pyenv/versions/자신이 지정한 이름/bin/python을 선택해주면 처음 설정이 끝난다.
