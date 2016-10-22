Week4_Day2
==

10/4

## 0. 목차
> 1. 이론 
> 2. 실습
> 3. 정리


## 1. 이론

#### 1.1. Runserver
1일 차에 했던 내용을 살짝 복습하면,

프로젝트를 실행할 폴더로 이동해서

virtualenv -> local 명령어로 가상환경 설정 후 장고를 설치하고

`django-admin startproject 프로젝트명`

명령어를 실행하게 되면 , 프로젝트가 생성된다.

그렇게 되면 manage.py 파일과 함께 해당 프로젝트 이름으로된 디렉토리가 생성되며 그 안에 

4개의 파일이 더 생성된다.

>- __init__.py : 별 의미 없는 파일이지만 이 디렉토리가 파이썬 패키지라는 것을 알려주는 역할을 한다.
>- setting.py : 파이썬 프로젝트의 환경설정을 포함한 각종 설정들을 조절할 수 있다.
>  - ex) app이 추가되면 그것을 사용하기 위해 setting.py의 INSTALLED_APPS에 app을 선언해줘야 하는 식.
>- urls.py : 프로젝트의 url에 대한 선언 들이 포함되어 있다.
>- wsgi.py : 어플리케이션 서버와 프로젝트 내에서 작성한 코드를 연결해주는 연할을 한다.
>- manage.py : 장고 프로젝트에게 명령을 내릴 수 있고 자기가 원하는 작업을 할 수 있도록 도와주는 파일.

INSTALLED_APPS : 
장고에서 사용할 모든 어플리케이션이 선언(등록)된다.

>- django.contrib.admin – 관리자 사이트. superuser 설정 후 domain/admin/으로 접속가능.
>- django.contrib.auth – 인증 프레임워크
>- django.contrib.contenttypes – 컨탠츠 타입을 위한 프레임워크
>- django.contrib.sessions – 세션 프레임워크
>- django.contrib.messages – 메세지 프레임워크
>- django.contrib.staticfiles – static 파일을 관리하는 프레임워크

이 어플리케이션들은 데이터베이스 테이블이 적어도 하나 필요하므로 우리가 맨처음 하나 만들어주어야 한다.

`python manage.py migrate`

migrate 명령어는 INSTALLED_APPS 세팅을 살펴본 뒤 데이터베이스 테이블을 만든다. 보통 처음을 제외하고는 models.py에서 변경점이 발생하지 않는 이상 먹히지 않는 명령어다. 대신, 변경 부분이 생기면 그 때마다 migrate를 해줘야 제대로 작동한다.


자, 그럼
여기까지 왔다면 서버를 돌려볼 시간이다.

콘솔창에서

`python manage.py runserver`

라고 입력해보자.

서버를 돌리기 시작하면 기본적으로 8000번 포트를 통해 루프백 ip로 접속할 수 있게된다.

디버그 모드를 사용하고 싶을 때는 runserver 중이라면 잠시 꺼두고 실행시켜야 한다.

#### 1.2. start APP

이제 어플리케이션(이하 앱)설치 단계까지 왔다. 콘솔창에서 다음과 같은 명령어를 통해 앱을 생성할 수 있다. 

`django-admin startapp 어플명`

프로젝트는 앱과 그 프로젝트에 대한 설정 등을 모두 총괄하는 역할이라 생각하면 되고, 앱들은 해당 앱 고유의 기능을 가지고 있다. 

따라서, 한 프로젝트 안에 여러가지의 앱이 들어갈 수 있으며 startapp 명령어를 통해 해당 앱 안에는 다음과 같은 파일들이 생성된다.

>- __init__.py
>- admin.py
>- apps.py
>- migrations
>	- __init__.py
>- models.py
>- tests.py
>- views.py



#### 1.3. app내 파일들의 기능

**views.py**<br>
 model(기능 부분)의 내용과 template(출력되는 부분)을 연결해주는 역할을 한다.
 
 view가 실행되기 위해서는 url과 연결되어 있어야 하며, 그러기 위해서 app폴더에 urls.py를 생성해야 한다. app/urls.py에 매핑을 완료했다면 프로젝트(root)의 urls.py에도 역시 내용을 추가해줘야 한다.

**urls.py**<br>
django.conf.url의 메소드를 사용한다. 

**url 함수 인자 ( regex, view )**<br>
1. regex : 매핑할 url을 찾을 정규표현식이다. 정규표현식은 URLconf 모듈이 처음 로드될 때 자동으로 컴파일 된다.<br>
2. view : 정규표현식으로 매핑되고 나면 장고는 특정한 view 함수를 호출한다.

**models.py**<br>

#### 1.4. python shell

`python manage.py shell`

일반 쉘과는 달리 manage.py가 DJANGO_SEETINGS_MODULE 환경 변수를 집어넣고 그 변수는 장고에게 settings.py 파일을 임포트 할 수 있는 경로를 주게 된다.

파이썬의 API를 이용할 수 있다.

import를 통해 Question, Choice Question 모델에 접근하여 q변수에 Question의 값을 넣어준다.

q = Question(question_text = "What's new?", pub_date = timezone.now())<br>
q.save()


#### 1.5. superuser 생성

`python manage.py createsupersuer`

명령어를 통해 슈퍼 유저를 생성한다.

그 이후 브라우저 주소창에 url/admin를 입력하면 관리자 화면으로 들어갈 수 있다.

앱이 관리자 파일에서 추가되게 하려면 admin.py에 설정을 해줘야한다.

`admin.site.register(Question)`

#### 1.6. View

```python

    urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
    
```

url함수의 첫 번째 인자는 정규표현식, 두번째는 호출할 뷰, 세번째는 나중에 호출할 수 있는 이름이다.

뷰에 대해서 알아보기 이전에 정규표현식에 대해서 간단하게 언급하자면,

정규표현식(regular expressions)를 줄여서 reg라고 하며 아주 많은 검색 패턴을 가지고 있으므로 만드는 규칙이 정해져 있다.

```
정규표현식 표기법
^ : 문자열이 시작할떄
$ : 문자열이 끝날 때
\d : 숫자
w : 워드
+ : 한 글자가 아니라 여러 글자가 반복 될 때
() : 패턴의 부분을 저장할 때 (인자를 전달할 때 필요하다)

ex) ^post/(\d+)/$
post로 시작해서 슬래쉬 안쪽에 역슬래쉬 안쪽에 한 자리 이상의 숫자가 들어간다는 의미.
```
뷰를 찾으면 해당 뷰가 다음과 같이 실행된다.

```python
detail(request = <HttpRequest object>, question_id ='34')

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('index.html')
	context = {
		'latest_question_list' : latest_question_list,
	}
	return HttpResponse(template.render(context, request))
	
```
다음은 url을 통해 호출될 index뷰	이다.
1. Question 테이블에서 pub_date 필드를 내림차순으로 5개 정렬해 뽑아온 후 보낼 템플릿을 만든다.
2. 템플릿과 latest_question_list 값이 담긴 context라는 딕셔너리를 response로 함께 보낸다.

render함수는 request, 템플릿이 될 페이지 ,context를 차례로 받은 뒤,
페이지를 템플릿으로 로드해서 context와 같이 포장하여 response로 보내는 것을 해주는 함수이다.


다음은 index를 통해 접근할 수 있는 detail.html이다.

```
<h1>{{ question.question_text}}</h1>
<ul>
{%for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```
h1에 해당 id(question_text) 값을 갖는 question을 받아서 질문 내용으로 한다.
for 문을 통해 question.choice_set.all로 불러온 choice들을 하나씩 호출한다.

#### 1.7. namespace

detail.html으로 링크 거는 방법은 만약 경로가 바뀐다면 모든 템플릿을 수정해줘야 한다는 단점을 가지고 있다. 그렇기에 namespace를 이용하여 자동으로 변경된 경로를 가리킬 수 있도록 한다.

`<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>`

url 뒤에 'detail'이라고 이름을 적어줌으로써 해당 뷰에 있는 question.id라는 것을 말해줄 수 있다.

네임스페이스를 이용하면 해당 뷰가 위치한 경로도 표기할 수 있다.

`<li><a href="{% url 'polls_name:detail' question.id %}">{{ question.question_text }}</a></li>`

위와 같이 미리 지정한 polls_name이라는 네임스페이스를 통해 해당 네임스페이스의 detail 뷰를 실행한다는 것을 알려준다.

#### 1.8. form tag 구현

```python
<h1>{{qustion.question.

```

#### 1.9. filter


## 2. 실습
>- 뷰를 통해 template를 context으로 받아서 response.
>- namespace
>- form 구현
>- vote page 구현


