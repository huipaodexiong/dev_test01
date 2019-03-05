from django.shortcuts import render
from django.http import HttpResponse
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
            return render(request, "index.html", {"error": "用户名或密码为空"})
        if username == "admin" and password == "123":
            return HttpResponse("登录成功")
        else:
            return render(request, "index.html", {"error": "用户名或密码错误"})


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

"""
数据库（user表） --- pymysql驱动 --- python链接 --- 增删改查
"""