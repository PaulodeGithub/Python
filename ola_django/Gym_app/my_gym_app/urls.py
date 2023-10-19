from django.urls import path

from . import views


#  here we are mapping our functions from views.py to the url path

urlpatterns = [
    path("", views.home_html_render, name="home"),
    path("login/", views.login_html_render, name="render"),
    path("login/verify/", views.login_verify_view, name="login_view"),
    path("login/verification/", views.verification, name="verification"),
    path("login/login_error/", views.login_error, name="login_error"),
    path("register/", views.registration, name="registration"),
    path("register/sign_up/", views.reg_user_view, name="reg_user_view"),
    # path("register/reg_success/", views.reg_success, name="reg_success"),
    path("register/reg_success/", views.reg_user_view, name="reg_success"),
]