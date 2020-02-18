from django.urls import path
from . import views #.은 현재 폴더 의미

#'' : 경로명, view : 현재 폴더에 있는 views파일을 의미, index는 views파일에 있는 index함수 의미
# 관행적으로 views로 사용, 뒤 index는 쓰기 나름, views안에 있는 함수명
# myapp만 신경 쓰겠다.
urlpatterns = [
    #여기 이름은 같을 필요 없다.
    path('', views.index),
    path('calcform', views.calcform),
    path('calc', views.calc),
    path('loginform', views.loginform),
    path('login', views.login),
    path('uploadform', views.uploadform),
    path('upload', views.upload),
    path('runpythonform', views.runpythonform),
    path('runpython', views.runpython),
]

#form에서 요청을 해서 연산을 한다.
#/logins?id=ckt&pwd=ckt -> views.logins()
#req = {}
#views.logins(req)