from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, EmailAuthenticationForm, ProfileForm
from articles.models import Articles
from users.models import CustomUser, ProfileLike
from notification.models import Notification


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:login')
    else:
        form = RegisterForm()
    return render(request, "users/registration.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = EmailAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("articles:home")
    else:
        form = EmailAuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("users:login")


def update_profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = ProfileForm(instance=request.user)

    post_count = Articles.objects.filter(author=request.user).count()
    return render(request, "users/user_profile.html", {
        "form": profile_form,
        "post_count": post_count})


def get_profile(request, user_id):
    user_profile = get_object_or_404(CustomUser, id=user_id)
    post_count = Articles.objects.filter(author=user_profile).count()
    liked_user_ids = user_profile.profile_likes.values_list('user', flat=True)
    return render(request, "users/view_user_profile.html", {
        "user_profile": user_profile,
        "post_count": post_count,
        "liked_user_ids": liked_user_ids,
    })


def toggle_profile_like(request, profile_id):
    profile = get_object_or_404(CustomUser, id=profile_id)
    like, created = ProfileLike.objects.get_or_create(profile=profile, user=request.user)
    if created:
        if profile != request.user:
            Notification.objects.create(
                recipient=profile,
                sender=request.user,
                message=f"{request.user.username} лайкнул ваш профиль",
            )
    else:
        like.delete()

    return redirect('users:get_profile', user_id=profile_id)





