from django.urls import path
from . import views #.은 현재 폴더 의미

#'' : 경로명, view : 현재 폴더에 있는 views파일을 의미, index는 views파일에 있는 index함수 의미
# 관행적으로 views로 사용, 뒤 index는 쓰기 나름, views안에 있는 함수명
# myapp만 신경 쓰겠다.
#만약, blog. 이렇게 호출하면, 인덱스 1번이
#blog/abc이렇게 호출하면, index2가
#blog/abc/detail 이렇게 호출하면, index3이다.
urlpatterns = [
    path('', views.index),
    #name이라는 정적인 url이 아니다. 얘는 파라미터를 의미해서, name이라는 파라미터에 동적으로 매핑된다.
    #임의의 문자열을 만들 수 있다.
    #path('<name>/', views.index2),
    #이렇게 하면, 정수만 올 수 있다.
    #path('<int:pk>/detail', views.index3),
    #특정 URL이 들어오면, 함수를 호출하는 형태
    #/붙이고, 안붙이든 사용자가, 원활하게 이용할수 있도록 해야한다.
    #name을 지정하고, name을 지정할때 파라미터가 필요하냐 안하냐, 요청할때, 반드시파라미터를 요청해야한다.
    path('list', views.list, name = "list"),
    path('<int:pk>/detail', views.detail, name = 'detail'),
    #view파일에 postview라는 클래스에서 as_view라는 객체를 생성
    #path('list2', views.PostView.as_view()),
    #왼쪽의 login/대신에, name="login"으로 경로를 설정
    path('login/', views.LoginView.as_view(), name="login"),
    path('add/', views.PostView.as_view(), name="add"),
    path('<int:pk>/edit/', views.PostEditView.as_view(), name="edit"),
]
#/logins?id=ckt&pwd=ckt -> views.logins()
#req = {}
#views.logins(req)