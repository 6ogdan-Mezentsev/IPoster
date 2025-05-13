from django.urls import path
from .views import register_view, login_view, logout_view, update_profile, get_profile, toggle_profile_like

app_name = 'users'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registration/', register_view, name='registration'),
    path('logout/', logout_view, name='logout'),
    path('profile/', update_profile, name='profile'),
    path('profile/<int:user_id>/', get_profile, name='get_profile'),
    path('profile/<int:profile_id>/like/', toggle_profile_like, name='toggle_profile_like')
]
