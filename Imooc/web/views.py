from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse
from django.shortcuts import render
import json

def Login(request):
    if request.method ==  "POST":
        result = {}
        username = request.POST.get('username')
        mobile = request.POST.get('password')
        # mobile = request.POST.get('mobile')
        # date = request.POST.get('data')
        result['user'] = username
        result['mobileNum'] = mobile
        # result['mobileNum'] = mobile
        # result['data'] = date
        result = json.dumps(result)
        return HttpResponse(result, content_type='application/json; charset=GB2312')
    else :
        return render(request,'login.html')


