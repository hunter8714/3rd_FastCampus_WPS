Week4_Day1. Django
-----

<br>
#### <i class="icon-file"></i> **이론**

##### <i class="icon-pencil"></i> **Model-View-Controller(MVC) Pattern**
- Model 
데이터베이스의 테이블에 대응
전체 데이터의 구조를 결정

- View
클라이언트에 보여지는 부분을 담당
HTML/CSS/JavaScript 

- Controller
사용자의 요청에 따라 Model에서 데이터를 얻어와서 View에 전달하는 역할
<br>
<br>

#####  <i class="icon-pencil"></i> **Django의 MTV(Model-Template-View)패턴에 매칭되는 각 MVC(Model-View-Controller)요소**
- MVC의 Model -> MTV의 Model
- MVC의 View -> MTV의 Template
- MVC의 Controller -> MTV의 View
<br>
<br>

>#### <i class="icon-refresh"></i> **실습**
- Initial setup for running Django 
- Startproject 
 => **manage.py** - A command-line utility 
 => **__init__.py** - Top-level package make Python treat the directories as containing packages
 => **setting.py** - Settings/configuration for this Django project
 => **urls.py** - Package to import anything inside it 
 =>  **wsgi.py** - Python standard for web servers and applications
- Running server, site 
- Models and the admin site
- View and templates

