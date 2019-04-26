from django.conf.urls import include
from django.urls import path
from FolderingAuthServer import views


urlpatterns = [
    # 회원가입      [POST]     /api/signup
    path('',views.UserCreateView.as_view()),
]