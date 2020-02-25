from django.shortcuts import render,redirect,HttpResponse
from accounts.forms import Profileform,DriverForm
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import Profiles
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static
import requests
from django.http import JsonResponse


# customer signup form
def sign(request):
    form=Profileform()
    if request.method=='POST':
        
        form=Profileform(request.POST)
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        mobile=request.POST['mobile']
        if password1==password2:

            if Profiles.objects.filter(user=username).exists():
                print("user exist")
                return redirect('profiles')
            elif Profiles.objects.filter(email=email).exists():
                print("user email exist our data base")
                return redirect('profiles')
            else:
                form.save() 
                return redirect('login')
        else:
            print("password is not same")
            return redirect('profiles')        
    return render(request,'templates/accounts/register.html')



''' for customer login views'''


'''customer login'''
def customer_login(request):

    if request.method=='POST':
        mobile_no=request.POST['mobile_no']
        user=Profiles.objects.filter(mobile=mobile_no).exists()
        if user:
           
           url=('https://2factor.in/API/V1/e2620bdd-53bb-11ea-9fa5-0200cd936046/SMS/'+mobile_no+'/AUTOGEN')
           response = requests.get(url)
           data = response.json()
           print(data)
            
           request.session['otp_session_data']=data['Details']
           
           print(request.session['otp_session_data'])
           
        
           return redirect('otp')
        else:
            return HttpResponse('No such mobile no exist:-'+mobile_no+'sorry')
    else:   
        return render(request,'registration/login.html')
    return render(request,'registration/login.html')


''' for otp for check user is authentic or not and the main purpose is register  mobile veryfication '''
def otp(request):
   
    if request.method=='POST':
    
        password=request.POST['otp']
        print(type(password))
        request.session['otp_session_data']
        print(request.session['otp_session_data'])
        url=('https://2factor.in/API/V1/e2620bdd-53bb-11ea-9fa5-0200cd936042/SMS/VERIFY/'+ request.session["otp_session_data"] +'/'+ otp +'')
        response = requests.get( url)	
        data = response.json()
        print(data)
        if data['Status'] == "Success":
            logged_user.is_active = True
            response_data = {'Message':'Success'}
            return redirect('home')
        else:
            return redirect('login')
        # else:
        #     return render(request,'registration/otp-module.html')
  


            
   
    return render(request,'registration/otp-module.html')


''' for driver signup form views'''

def driver(request):
    if request.method=='POST':
        dform=DriverForm(request.POST,request.FILES)

        if dform.is_valid():
            dform.save()
            return HttpResponse('submit')
    else:
        dform=DriverForm()
    return render(request,'templates/accounts/driver.html',{'dform':dform})


#     context={
        
#         api_key:'e2620bdd-53bb-11ea-9fa5-0200cd936042',
#         mobile_no:'mobile_no'
        
#     }
#    otp=https://2factor.in/API/V1/e2620bdd-53bb-11ea-9fa5-0200cd936042/SMS/8464841764/AUTOGEN
#'https://2factor.in/API/V1/{api_key}/SMS/VERIFY/{session_id}/{otp_entered_by_user}
# apk=settings.API_KEY
    # web=settings.WEBSITE_NAME
    #if request.session.has_key('is_login'):
    #requests.get('https://2factor.in/API/V1/e2620bdd-53bb-11ea-9fa5-0200cd936042/SMS/VERIFY/'+the_id+'/'+otp+'')

#if not request.session.session_key:
    # request.session.create()
    # s_key=request.session.session_key
    # print(s_key)
      #print(request.session.session_key)
      #response = get_response(request)
