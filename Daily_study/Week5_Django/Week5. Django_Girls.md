Week4_Day3. Django Girls Tutorial
==

## 0. 목차
> 1. 이론
2. 실습
3. 정리

## 1. 실습
#### 1.1. 1단계. 준비
** Django 시작하기**

>- mkdir 로 저장할 공간 만들기
- cd 디렉토리명 으로 디렉토리 이동
- pyenv virtualenv 사용할 버전 이름
이 명령어로 가상환경 생성.
- pyenv local 가상환경명.
가상환경을 돌리는 명령어. local로 사용하겠다는 의미. .python-version 파일이 생성된다.
이후 , 해당 디렉토리에 들어갈 때마다 해당 디렉토리에 설정되어 있는 가상환경이 자동으로 실행되면서 앞에 (가상환경명)이 붙는다.
- pip install django 명령어로 장고설치
- 설치 후 django-admin startproject 프로젝트명 : 프로젝트 생성 명령어.
- django-admin startapp 앱명 : 앱 생성 명령어.
- editor을 설치하고 실행시킨 후(pycharm같은 프로그램) project interpreter를 설정해준다.
preference -> add local -> show all - > usr/local/var/pyenv/versions/가상환경명/bin/python
설정

** 현재 시간 추가하기 **<br>

/settings.py에서 설정 변경 가능.<br>

`웹사이트에 현재 시간 추가 : TIME_ZONE  = ' Asia/Seoul'`


**Database 생성하기**<br>
python manage.py migrate명령어를 통해 데이터베이스 생성.

 ```python
 ✗ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK```
  
  DB를 생성했다면 ./manage.py runserver 명령어를 통해 서버를 돌려보자.
  
```python
./manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
October 13, 2016 - 21:17:37
Django version 1.10.2, using settings 'PracticeGirls.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
127.0.0.1은 loopback ip , 즉 자기 자신의 ip를 의미하는데, runserver 명령어를 치면 자신의 pc를 서버로 해서 8000 포트를 열어서 접속하는 것이 된다.


#### 1.2. 2단계. DJango Model
**어플리케이션 제작하기**
포스트를 할 수 있는 블로그를 생성해볼 것이다.

`python manage.py startapp blog(어플리케이션 이름)`

startapp 명령어를 통해 어플리케이션을 생성해보자.

```python
drwxr-xr-x  6 Song  staff   204B 10 13 21:05 .
drwxr-xr-x  4 Song  staff   136B 10 13 19:32 ..
drwxr-xr-x  6 Song  staff   204B 10 13 21:11 .idea
drwxr-xr-x  7 Song  staff   238B 10 13 21:05 PracticeGirls
-rw-r--r--  1 Song  staff   128K 10 13 21:05 db.sqlite3
-rwxr-xr-x  1 Song  staff   811B 10 13 19:32 manage.py
(Practice_Girls) ➜  PracticeGirls git:(master) ✗ python manage.py startapp blog
(Practice_Girls) ➜  PracticeGirls git:(master) ✗ l
total 264
drwxr-xr-x  7 Song  staff   238B 10 13 21:30 .
drwxr-xr-x  4 Song  staff   136B 10 13 19:32 ..
drwxr-xr-x  6 Song  staff   204B 10 13 21:11 .idea
drwxr-xr-x  7 Song  staff   238B 10 13 21:05 PracticeGirls
drwxr-xr-x  9 Song  staff   306B 10 13 21:30 blog
-rw-r--r--  1 Song  staff   128K 10 13 21:05 db.sqlite3
-rwxr-xr-x  1 Song  staff   811B 10 13 19:32 manage.py
(Practice_Girls) ➜  PracticeGirls git:(master) ✗
```

전에 없던 blog폴더가 생성되어 있는 것을 볼 수 있다.

```python
blog 내에 생성된 파일 목록

drwxr-xr-x  9 Song  staff   306B 10 13 21:30 .
drwxr-xr-x  7 Song  staff   238B 10 13 21:30 ..
-rw-r--r--  1 Song  staff     0B 10 13 21:30 __init__.py
-rw-r--r--  1 Song  staff    63B 10 13 21:30 admin.py
-rw-r--r--  1 Song  staff    83B 10 13 21:30 apps.py
drwxr-xr-x  3 Song  staff   102B 10 13 21:30 migrations
-rw-r--r--  1 Song  staff    57B 10 13 21:30 models.py
-rw-r--r--  1 Song  staff    60B 10 13 21:30 tests.py
-rw-r--r--  1 Song  staff    63B 10 13 21:30 views.py
(Practice_Girls) ➜  blog git:(master) ✗
```

생성 후, setting.py에 install_apps에 'blog', 를 추가해줘야 한다.

이것은 setting.py에 blog라는 앱을 사용하겠다는 것을 알려주겠다는 의미이다.

