from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from blog.models import Post
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.
#DB때와 거의 유사, UI를 간접적으로 만들어 주는것
from django.forms import Form
from django.forms import CharField, Textarea, ValidationError

# Create your views here.

#기본적으로 html을 리턴하려면, HttpResponse를 사용한다.
def index(requst):
    return HttpResponse("ok")

#매핑관계
def index2(request, name):
    return HttpResponse("ok" + name)

def index3(request, pk):
    #pk는 설계자가 만든 parameter, pk가 pk인것을 찾아준다. 즉, 사용자가 django에서 입력한대로 찾아준다.
    #p = Post.objects.get(pk=pk)
    p = get_object_or_404(Post, pk=pk)
 
    #return HttpResponse("ok" + str(pk))
    return HttpResponse("ok" + p.title)

def list(request):
    username = request.session["username"]
    user = User.objects.get(username=username)
    #data = Post.objects.all()
    data = Post.objects.all().filter(author=user)
    context = {"data":data, "username":username}
    return render(request, "blog/list.html", context)

def detail(request, pk):
    p = get_object_or_404(Post, pk=pk)
    return render(request, "blog/detail.html", {"d":p})

class PostView(View):
#get방식이던, post방식이건, 다 받아서 처리할 수 있도록 생성
    def get(self, request):
        return render(request, "blog/edit.html")

    def post(self, request):

        title = request.POST.get("title")
        text = request.POST.get("text")
        username = request.session["username"]
        user = User.objects.get(username=username)
        Post.objects.create(title=title, text=text, author=user)
        return redirect("list")
        #return HttpRespnse("post ok~")

class LoginView(View):
    def get(self, request):
        return render(request, "blog/login.html")

    #post 방식일때는, 아이디와 비번이 맞을때와 다를때 구분해서 return 한다.
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user == None:
            #경로명이 아니라, 이름이다.
            return redirect("login")
            #return HttpResponse("암호 틀림")
            #return HttpResponse("ok")
            #global 변수가 아니라, session 변수에 누가 로그인을 했는지에 대한 정보를 담을 수 있다.
        
        else:
            request.session["username"] = username
            return redirect("list")

class PostForm(Form):
    title = CharField(label='제목', max_length=20)
    #widget의 default값은 Text
    text = CharField(label="내용", widget=Textarea)

class PostEditView(View):
#get방식이던, post방식이건, 다 받아서 처리할 수 있도록 생성
    def get(self, request, pk):
        #초기값 저장
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(initial={'title':post.title, 'text':post.text})
        
        return render(request, "blog/edit.html", {"form":form, "pk":pk})

    def post(self, request, pk):
        form = PostForm(request.POST)
        if form.is_valid():
            post = get_object_or_404(Post, pk=pk)
            post.title = form['title'].value()
            post.text = form['text'].value()
            post.publish()
            return redirect("list")
        return render(request, "blog/edit.html", {"form": form, "pk": pk})

#def post(self, request, pk):
#    form = PostForm(request.POST)
#    post = get_object_or_404(Post, pk=pk)
#    post.title = form['title'].value()
#    post.text = form['text'].value()
#    post.publish()
#    return redirect("list")