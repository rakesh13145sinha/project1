from django.urls import path
from accounts import views
urlpatterns=[
    # path('signup/',views.signup, name='signup'),
    # path('profile/',views.profile,name='profile'),
    path('sign/',views.sign,name='profiles'),
    path('login/',views.customer_login,name='login'),
    path('otp/',views.otp,name='otp'),
    path('driver/',views.driver),
    
    

]