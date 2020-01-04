from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "mainblog"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>/", views.detail, name="detail"),
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="mainblog/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="mainblog/suc.html"),
        name="logout",
    ),
    path("account/<int:user_id>", views.account, name="account"),
    path("new_post/<int:user_id>", views.create_post, name="create_post"),
    path("del/<int:post_id>", views.del_post, name="del_post"),
]
