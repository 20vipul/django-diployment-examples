from django.urls import path,include
from Basic_App import views
#Template URLS

app_name="Basic_App"

urlpatterns=[
    path("register/",views.register,name="register"),
    path("user_login/",views.user_login,name="user_login"),
]