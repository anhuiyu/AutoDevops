from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO
import random
# Create your views here.
def login(request):
    error=""
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect("/index/")
        else:
            error="用户名或密码错误"
            return render(request, "login.html", {"error": error})
    return render(request,"login.html",{"error":error})
def index(request):
    return render(request,"index.html")
def get_valid_img(request):
    #获取随机颜色的函数
    def get_random_color():
        return random.randint(0,255),random.randint(0,255),random.randint(0,255)
    img_obj=Image.new(
        'RGB',
        (220,35),
        get_random_color()
    )
    draw_obj = ImageDraw.Draw(img_obj)
    font_obj = ImageFont.truetype("static/font/kumo.ttf", 28)
    tmp_list = []
    for i in range(5):
        u = chr(random.randint(65, 90))
        l = chr(random.randint(97, 122))
        n = str(random.randint(0, 9))
        tmp = random.choice([u, l, n])
        tmp_list.append(tmp)
        draw_obj.text((20+40*i, 0), tmp, fill=get_random_color(), font=font_obj)
    request.session["valid_code"] = "".join(tmp_list)
    io_obj=BytesIO()
    img_obj.save(io_obj,"png")
    data=io_obj.getvalue()
    return HttpResponse(data)