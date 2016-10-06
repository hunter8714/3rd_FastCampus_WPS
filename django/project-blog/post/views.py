from django.shortcuts import render , render_to_response
from .models import post


#post_list라는 이름의 view
#post 인스턴스를 전부 가져와 posts라는 이름으로 'post_list.html' 템플릿에 전달해준다

def post_list(request):
    # ORM 을 이용해 post인스턴스를 전부 가져옵니다
    posts = post.objects.all()

    # 템플릿에 전달할 dictionary 객체
    ret = {
        # 테스트용 전달 값
        'title': '블로그 글 목록',
        # posts라는 key 값에 posts(Queryset)을 지정
        'posts': posts
    }




    # 해당 템플릿('post_list.html)에 전달할 데이터로 render한 값을 response해준다
    return render_to_response("post_list.html", ret)