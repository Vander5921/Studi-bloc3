from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('deconnexion/', auth_views.LogoutView.as_view(next_page='home'), name='deconnexion'),
]
