from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user),
    path('list/',views.list_data),
    path('', RedirectView.as_view(url='list/')),
    path('login/authenticate', views.authenticate_login),
    path('logout/', views.logout_user),
    path('register/', views.register),
    path('register/submit', views.set_dados),
    path('delete/', views.delete_dados),
    path('delete/<slug:id>', views.delete)
]
