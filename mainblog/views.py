import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import RegisterForm, PostCreate


@login_required(login_url="login/")
def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "mainblog/index.html", context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(
                password=form.cleaned_data["password1"],
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
            )
            new_user.save()
            return render(request, "mainblog/suc.html")
        else:
            return render(
                request,
                "mainblog/register.html",
                {"error_message": "Account already exist"},
            )
    else:
        form = RegisterForm()
        return render(request, "mainblog/register.html", {"form": form})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "mainblog/post.html", {"post": post})


def account(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, "mainblog/account.html", {"user": user})


def create_post(request, user_id):
    if request.method == "POST":
        form = PostCreate(request.POST)
        user = get_object_or_404(User, pk=user_id)
        if form.is_valid():
            new_post = Post.objects.create(
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"],
                pub_date=datetime.datetime.now(),
                author=user,
            )
            new_post.save
            return HttpResponseRedirect(reverse("mainblog:index"))
    else:
        form = PostCreate()
    return render(request, "mainblog/new_post.html", {"form": form})


def error_not_found(request, exception=None):
    return render(request, "mainblog/404.html", status=404)


def del_post(request, post_id):
    if request.method == "POST":
        Post.objects.filter(id=post_id).delete()
        return HttpResponseRedirect(reverse("mainblog:index"))
    else:
        return detail(request, post_id)


# Create your views here.
