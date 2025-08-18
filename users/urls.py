from django.urls import path
from users.apps import UsersConfig
from users.views import CustomUserCreateView
from django.contrib.auth.views import LoginView, LogoutView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', CustomUserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:product_list'), name='logout'),
]
