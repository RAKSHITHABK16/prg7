from django.urls import path
from myapp import views
app_name="myapp" #is used to create a namespce\

urlpatterns = [
    path('trial/',views.trial,name="Trial"),
    path('profile/',views.profile,name="profile"),
]
