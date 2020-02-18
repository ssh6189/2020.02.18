from django.urls import path
from . import views #.은 현재 폴더 의미

#'' : 경로명, view : 현재 폴더에 있는 views파일을 의미, index는 views파일에 있는 index함수 의미
# 관행적으로 views로 사용, 뒤 index는 쓰기 나름, views안에 있는 함수명
# myapp만 신경 쓰겠다.
urlpatterns = [
    path('', views.index),
    path('test', views.test),
    path('images', views.images),
    path('lists', views.lists),
    path('login', views.login),
    path('service', views.service),
    path('logout', views.logout),
    path('uploadimage', views.uploadimage),
    path('listuser', views.listuser),
]

#/logins?id=ckt&pwd=ckt -> views.logins()
#req = {}
#views.logins(req)