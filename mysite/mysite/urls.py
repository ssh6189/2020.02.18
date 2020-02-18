"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#admin이라는 경로에서는 아랫줄이 실행됨
#어플리케이션 한개만 만들때는 여기를 더이상 건드릴일 없다.
urlpatterns = [
    #flask 와 다르게 '/'로 하면 안된다.
    #문자열, myapp이라는 폴더에 있는 urls파일을 포함해라, 실제 어플리케이션에서 사용할 url은 여기서 정의
    #앞의 경로 + myapp의 함수명, 즉 localhost:포트번호+첫번째 파라미터, 다만, 명이 들어가면, myapp urls에서 /를 표기, 없으면, 뺀다.
    path('', include('myapp.urls')),
    path('admin/', admin.site.urls), #실제 패키지 이름, 얘는 django가 기본적으로 가지고 있는 패키지다.
    path('ajax/', include('ajax.urls')),
    path('blog/', include('blog.urls')),

    #여기에는 내가 만든 앱들을 정의를 해주어야한다.
]
