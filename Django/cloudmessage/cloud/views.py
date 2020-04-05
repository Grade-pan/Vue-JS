from django.shortcuts import render

from .models import Message


# Create your views here.

def BaiDu(request):
    return render(request, "baidu.html")


def QIDIAN(request):
    return render(request, "QiDian.html")


def Register(request):
    return render(request, "register.html")


def GetInformation(request):
    datalist = []
    if request.method == "POST":
        yourName = request.POST.get("yourName", None)
        yourTelephone = request.POST.get("yourTelephone", None)
        message = request.POST.get("information", None)
        otherName = request.POST.get("otherName", None)
        otherTelephone = request.POST.get("otherTelephone", None)
        color = request.POST.get("color", None)
        time = request.POST.get("time", None)
        # 写入数据库
        tc = Message(yourName=yourName, yourTelephone=yourTelephone, message=message, otherName=otherName,
                     otherTelephone=otherTelephone, color=color, time=time)
        tc.save()

    if request.method == "GET":
        # 查询信息
        yourName = request.GET.get("yourName", None)
        print(yourName)
        yourMessage = Message.objects.filter(yourName=yourName)
        i = 0
        objectLength = len(yourMessage)
        while objectLength > 0:
            d = {"yourName": yourMessage[i].yourName,
                 "yourTelephone": yourMessage[i].yourTelephone,
                 "information": yourMessage[i].message,
                 "otherName": yourMessage[i].otherName,
                 "otherTelephone": yourMessage[i].otherTelephone,
                 "color": yourMessage[i].color,
                 "time": yourMessage[i].time}
            datalist.append(d)
            i = i + 1
            objectLength = objectLength - 1

    return render(request, "note.html", {"data": datalist})
