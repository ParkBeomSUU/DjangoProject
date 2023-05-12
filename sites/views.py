from django.shortcuts import render, redirect
from .models import Omo, PredResults
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.models import User
import pandas as pd
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


def home(request):
    values = Omo.objects.all().order_by('-pk')

    return render(
        request,
        'sites/home.html',
        {
            'values': values
        }
    )


def predict(request):
    return render(request, 'sites/predict.html')


def predresults(request):
    values = Omo.objects.all().order_by('-pk')

    return render(
        request,
        'sites/predresults.html',
        {
            'values': values
        }
    )


def product(request):
    values = Omo.objects.all().order_by('-pk')

    return render(
        request,
        'sites/product.html',
        {
            'values': values
        }
    )


def loginView(request):
    if request.method == "POST":
        username = request.POST.get('user_id')
        password = request.POST.get('user_pw')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user=user)
            return redirect('/home')

        else:
            return render(request, 'sites/login.html')
    else:
        return render(request, 'sites/login.html')


def logoutView(request):
    auth.logout(request)
    return redirect('/home')


def detail(request, pk):
    pk_num = Omo.objects.get(id=pk)

    context = {
        'detail': pk_num,
        'update': pk_num,
        'graph': pk_num,

    }
    return render(request, 'sites/detail.html', context)


def graph(request, pk):
    pk_num = Omo.objects.get(id=pk)

    context = {
        'graph': pk_num
    }
    return render(request, "sites/graph.html", context)


def result(request):
    if request.method == "POST":
        data = Omo()
        data.battery = request.POST.get("battery")
        data.bat_status = request.POST.get("bat_status")
        data.buzzer = request.POST.get("buzzer")
        data.r_led = request.POST.get("r_led")
        data.g_led = request.POST.get("g_led")
        data.b_led = request.POST.get("b_led")
        data.r_rpm = request.POST.get("r_rpm")
        data.l_rpm = request.POST.get("l_rpm")
        data.headlight = request.POST.get("headlight")
        data.content = request.POST.get("content")
        data.writer = request.user
        data.save()
        print("DB 입력 완료")
        values = Omo.objects.all().order_by('-pk')
        return redirect("/home/result/")  # render(request, 'sites/result.html')
        # 입력을 마치면  POST요청을 주면 바로

    values = Omo.objects.all().order_by('-pk')

    context = {
        'values': values,
    }

    return render(request, 'sites/result.html', context)


def edit(request):
    if request.method == "POST":
        data = Omo()
        data.battery = request.POST.get("battery")
        data.buzzer = request.POST.get("buzzer")
        data.r_led = request.POST.get("r_led")
        data.g_led = request.POST.get("g_led")
        data.b_led = request.POST.get("b_led")
        data.r_rpm = request.POST.get("r_rpm")
        data.l_rpm = request.POST.get("l_rpm")
        data.headlight = request.POST.get("headlight")
        data.content = request.POST.get("content")
        data.writer = request.user
        data.save()
        print("DB 입력 완료")
        print(request.user)
        return redirect("/home/result/")
        # render(request, 'sites/result.html')
        # 입력을 마치면  POST요청을 주면 바로

    else:
        return render(request, 'sites/edit.html')


def delete(request, pk):
    pk_num = Omo.objects.get(id=pk)
    pk_num.delete()

    return redirect("/home/result/")


#
# # error 랜더링
# def page_not_found(request, exception):
#     return render(request, 'common/404.html', {})
def predict_chances(request):
    if request.POST.get('action') == 'post':
        # Receive data from client
        battery = float(request.POST.get('battery'))
        rpm = float(request.POST.get('rpm'))
        headlight = float(request.POST.get('headlight'))
        buzzer = float(request.POST.get('buzzer'))

        # Unpickle model
        # 경로 맞는지 재확인 필요
        model = pd.read_pickle(r'PredResults_model.pickle')
        # Make predictionredResults_model.pickle'
        result = model.predict([[battery, rpm, headlight, buzzer]])

        led = result[0]
        PredResults.objects.create(battery=battery, rpm=rpm, headlight=headlight, buzzer=buzzer, led=led)
        return JsonResponse({'result': led, 'battery': battery,
                             'rpm': rpm, 'headlight': headlight, 'buzzer': buzzer},
                            safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "sites/predresults.html", data)


def update(request,pk):
    pk_num=Omo.objects.get(id=pk)
    context={
        'update':pk_num,
        
    }
    return render(request,"sites/update.html",context)

@csrf_exempt
def update_a(request,pk,num):
    print(pk)
    print(num)
    pk_num=Omo.objects.get(id=pk)

    if request.method =="POST":
        if num==1:
            print("ajax요청")
            json_data=json.loads(request.body)
            print("json_data:",json_data["battery"])
            print(pk_num.battery)
            pk_num.battery=json_data["battery"]
            print(pk_num.battery)
            pk_num.save()
            
        # pk_num.r_led=request.POST.get("r_led")
        # pk_num.g_led=request.POST.get("g_led")
        # pk_num.b_led=request.POST.get("b_led")
        # pk_num.r_rpm=request.POST.get("r_rpm")
        # pk_num.l_rpm=request.POST.get("l_rpm")
            context={
                'battery': json_data['battery'],

            }
            print("DB저장 완료")
            return JsonResponse(context)
        
        elif num==2:
            print("ajax요청")
            json_data=json.loads(request.body)
            print("json_data:",json_data)
            pk_num.r_led= json_data['r_led']
            pk_num.g_led = json_data['g_led']
            pk_num.b_led = json_data['b_led']
            pk_num.save()
            context={
                'r_led': json_data["r_led"],
                'g_led': json_data["g_led"],
                'b_led': json_data["b_led"],

            }
            print("DB저장 완료")
            return JsonResponse(context)
        
        elif num==3:
            print("ajax요청")
            json_data=json.loads(request.body)
            print("json_data:",json_data)
            pk_num.r_rpm= json_data['r_rpm']
            pk_num.l_rpm = json_data['l_rpm']
            pk_num.save()
            context={
                'r_rpm': json_data["r_rpm"],
                'l_rpm': json_data["l_rpm"],
            }
            print("DB저장 완료")
            return JsonResponse(context)
