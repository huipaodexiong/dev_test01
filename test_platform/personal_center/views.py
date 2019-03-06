from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def say_hello(request):
    input_name = request.GET.get("name", "")
    if input_name == "":
        return HttpResponse("请输入name值")
    return render(request, "index.html", {"name": input_name})

def index(request):
    """
    登录首页
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "index.html")
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        print(username, password)
        if username == "" or password == "":
            # 账号或者密码有一个为空，则返回提示
            return render(request, "index.html", {"error": "用户名或密码为空"})

        # 系统自带校验登录账号和密码，返回的值
        user = auth.authenticate(username=username, password=password)
        print("user的值：", user)

        if user is None:
            # 如果user值为空，则账号密码不匹配
            return render(request, "index.html", {"error": "用户名或密码错误"})
        else:
            # 否则，账号密码匹配
            auth.login(request, user) # 记录用户的登录状态
            # return HttpResponse("登录成功")
            # return render(request, "manage.html")
            return HttpResponseRedirect('/manage/')
        # if username == "admin" and password == "123":
        #     return HttpResponse("登录成功")
        # else:
        #     return render(request, "index.html", {"error": "用户名或密码错误"})


@login_required()
def manage(request):
    # 登录成功，跳转到管理界面
    return render(request, "manage.html")

# 处理用户的退出
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

# def login_action(request):
#     """
#     处理登录get请求
#     :return:
#     """
#     username = request.GET.get("username", "")
#     password = request.GET.get("password", "")
#     print(username, password)
#     if username == "" or password == "":
#         return render(request, "index.html", {"error": "用户名或密码为空"})
#     if username == "admin" and password == "123":
#         return HttpResponse("登录成功")
#     else:
#         return render(request, "index.html", {"error": "用户名或密码错误"})

# def login_action(request):
#     """
#     处理登录POST请求
#     :return:
#     """
#     username = request.POST.get("username", "")
#     password = request.POST.get("password", "")
#     print(username, password)
#     if username == "" or password == "":
#         return render(request, "index.html", {"error": "用户名或密码为空"})
#     if username == "admin" and password == "123":
#         return HttpResponse("登录成功")
#     else:
#         return render(request, "index.html", {"error": "用户名或密码错误"})
