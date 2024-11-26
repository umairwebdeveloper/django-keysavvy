from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('works/', views.works, name='works'),
    path('buy/', views.buy, name='buy'),
    path('auth/', views.auth, name='auth'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
