from django.urls import path,include
from . import views

urlpatterns = [
    
    
    path('',views.login_page, name='login_page'),
    path('register/',views.Register, name='Register'),
    path('welcome/',views.welcome,name='welcome'),
]
