from django.shortcuts import render,redirect,HttpResponse
from django.contrib.sessions.models import Session

# def map(request):
#     mapbox_access_token='pk.eyJ1IjoicmFrZXNoc2luaGExMzE0NSIsImEiOiJjazZ1Yms1dTcwN2dkM2ltc2J3Z211am40In0.aWsRIXURT7dw_NT20Jrapw'
#     return render(request, 'templates/social/home.html',{'mapbox_access_token':mapbox_access_token} )



def index(request):
    if request.session.has_key('is_login'):
        request.session.set_expiry(20)
        return render(request,'templates/dashboard/500.html')
    else:
        return HttpResponse('<h2>session closed</h2>')
    return redirect('login')
    

def google_map(request):
    if request.session.has_key('is_login'):
        request.session.set_expiry(20)
        api_key='AIzaSyA2QMoOFLVZFMwPrhnWqDqzmf01QrxBLKQ'
        return render(request,'templates/dashboard/map.html',{'api_key':api_key})
    else:
        return redirect('login')

def otp_match(request):
    return render(request,'templates/dashboard/test.html')
    

