from django.urls import path
from dashboard import views
urlpatterns=[
    #path('social/',views.map,name='map'),
    path('home/',views.index,name='home'),
    path('location/',views.google_map,name='location'),
    path('match/',views.otp_match,name='match')


]   