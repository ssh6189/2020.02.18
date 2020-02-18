from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import sys
from io import StringIO

# Create your views here.
def index(request):
    return HttpResponse("Hello ajax!!!^^^") #HttpResponse : Http를 리턴

#ajax폴더 밑에 있는 calc.html을 가져와 달라, default는 템플릿 폴더, 
# 즉, template밑에 ajax폴더가 있어야하고, ajax폴더 밑에 calc.html이 있어야한다.
# 여기서, ajax폴더는 템플릿 밑에 있는 동명의 다른 폴더이다. 착각하지 말자.

def calcform(request):
    return render(request, "ajax/calc.html")

def calc(request):
    op1 = int(request.GET["op1"])
    op2 = int(request.GET["op2"])

    result = op1 + op2

    #return HttpResponse(f"result = {result}")
    #return HttpResponse("{'result'"+str(result) + "}")
    #문자열이 아니라, 딕셔너리로 넣어주면, 딕셔너리를 JSON 형식으로 바꾸어준다.
    return JsonResponse({'error':0, 'result':result})

def loginform(request):
    return render(request, "ajax/login.html")

#많은 부분을 서버쪽이 아닌, 클라이언트쪽으로 넘겨버린다.
def login(request):
    id = request.GET["id"]
    pwd = request.GET["pwd"]

    if id == pwd:
        request.session["user"] = id
        return JsonResponse({'error':0})
    else:
        return JsonResponse({'error': -1, 'message':'id/pwd를 확인해주세요.'})

def uploadform(request):
    return render(request, 'ajax/upload.html')

def upload(request):
    file = request.FILES['file1']
    filename = file._name
    fp = open((settings.BASE_DIR + "/static/") + filename, "wb")
    for chunk in file.chunks():
        fp.write(chunk)
    fp.close
    return HttpResponse("upload~")

def runpythonform(request) :
    return render(request, "ajax/runpython.html")

glo = {}
loc = {}

#GET방식으로 호출
def runpython(request) :
    code = request.GET["code"]

    original_stdout = sys.stdout
    sys.stdout = StringIO()
    exec(code, glo, loc)
    contents = sys.stdout.getvalue()
    sys.stdout = original_stdout
    contents = contents.replace("\n", "<br>")
    return HttpResponse(contents)
'''
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
        '''
        
#    id = listData[len(listData)-1]["id"]+1
#    listData.append({"id":id, "img":filename, "title":title})

    #return HttpResponse("ok")