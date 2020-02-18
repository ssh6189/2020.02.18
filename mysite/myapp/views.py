from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from myapp.models import User
# Create your views here.

#함수명과 변수명은 크게 신경 안써도 됨, 관행적으로 쓰는것, 여기서 request는 flask의 request와 같다.

#매핑정보(@ 같은것)가 없어서, 이것만 치면, 웹서버에서 결과를 확인할 수 없다. 그래서, 매핑을 해주어야 한다.
#mysite폴더의 urls 파일에 가서, 매핑을 정의해 준다.

def index(request):
    return HttpResponse("Hello Django")

#html파일을 웹사이트에 적용
#위의 HttpResponse보다 보통 render 함수를 자주 쓴다.
#mysite폴더에 template.html이 있고, 여기에 함수를 정의한다고 해서, 되는게 아니다. 에러가 난다.
#global 정의는 mysite -> mysite -> settings에서 한다.
#딕셔너리 형태로 정의해, template.html 파일의 message에 들어갈 값을 여기서 줄 수가 있다.
def test(request):
    return render(request, 'template.html', {"message":"안녕"})

def images(request):
    data = {"s":{"img":"test.png"}}
    return render(request, 'template.html', data)

def lists(request):
    data = {"s":{"img":"test.png"},
           "list":[1, 2, 3, 4, 5]}
    return render(request, 'template.html', data)

def login(request):
    id = request.GET["id"]
    pwd = request.GET["pwd"]

    if id == pwd:
        #어떤 유저가 로그인 했는지 표시
        request.session["user"] = id
        
        #네트워크를 한번 왕복
        #1. return HttpResponse("로그인 성공 <a href=service>서비스로</a>")

        #하이퍼링크 거치지 않고 바로 서비스 페이지로가려면?
        # #return값에 함수를 주어도 되지만, redirect개념을 써보자
        # 결과는 같은데, 주소창이 다르다.
        #네트워크를 두번 왕복
        return redirect("/service")

    else:
        #네트워크를 한번 왕복
        #1. return HttpResponse("로그인 실패 <a href=static/login.html>다시로그인</a>")
        #네트워크를 두번 왕복
        return redirect("/static/login.html")


    #차이점, 1번의 경우 접속을 한 상태에서, 새로고침을 하면, 다시 로그인 창으로 간다.
    #즉, 로그인 페이지를 요청한한다.
    #2번의 경우, redirect로 써주면, 새로고침을 해도, 접속이 유지된다.
    #즉, 서비스 페이지를 요청한다.
    #하지만, 2번도 문제가 있다. 로그인을 하지 않았는데, service페이지로 갈 수 있다.

#로그인 성공시, Main Service페이지로, 실패시, 다시 로그인 화면으로 이동
def service(req):
    #빈 문자열은 로그인을 하지 않은 상태
    if req.session.get("user", " ") == "":
        return redirect("/static/login.html")
    else:
        html = "Main Service<br>" + req.session.get("user") + "님 감사합니다."
        #1.return HttpResponse("Main Service")
        return HttpResponse(html)

def logout(request):
    request.session["user"]=""
    #request.session.pop["user"]
    return redirect("/static/login.html")
#세션은 글로벌 변수도 아니고, 로컬 변수도 아니다.        

#uploadimage 기능은 csrf문제 검사를 하지 않고 실행한다.
@csrf_exempt
def uploadimage(req):  
    file = req.FILES['file1']
    filename = file._name    
    fp = open(settings.BASE_DIR + "/static/" + filename, "wb")
    for chunk in file.chunks() :
        fp.write(chunk)
    fp.close()            
    html =  "ok :" + "^^" + filename   
    
    result = faceverification(settings.BASE_DIR + "/static/" + filename)
    if result != "":
        request.session["user"] = result
        return redirect("/service")
    else:
        return redirect("/static/login.html")
#    id = listData[len(listData)-1]["id"]+1
#    listData.append({"id":id, "img":filename, "title":title})

    #return HttpResponse("ok")

#데이터베이스를 몰라도, 또는 개념이 없어도, 다룰 수 있는 방법이다.
def listuser(request):
    if request.method == "GET":
        q = request.GET.get("q", "")
        if userid != "":
            User.objects.all().get(userid=userid).delete()
            return redirect("/listuser")
        q = request.GET.get("q", "")
        data = User.objects.all()
        if q!= "":
            data = User.objects.all().filter(name__contains=q)
        return render(request, 'template2.html', {"data":data})
    else:
        userid = request.POST.get("userid")
        name = request.POST["name"]
        age = request.POST["age"]
        hobby = request.POST["hobby"]
    
        #db insert
        return redirect("/listuser")

    u = User(userid = userid, name = name, age = age, hobby = hobby)
    u.save()
    #user.objects.create()
    return redirect("/listuser")