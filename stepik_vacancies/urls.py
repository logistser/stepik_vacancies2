"""stepik_vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from vacancies.views import MainView, AllVacanciesView, SpecialtyVacanciesView, CompanyView, VacancyView,\
    ApplicationView, LoginView, LogoutView, SignupView, custom_handler404, custom_handler500

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('vacancies/', AllVacanciesView.as_view(), name='vacancies'),
    re_path(r'^vacancies/cat/([\w-]+)/', SpecialtyVacanciesView.as_view(), name='specialization'),
    re_path(r'^companies/([\d-]+)/', CompanyView.as_view(), name='company'),
    re_path(r'^vacancies/([\d-]+)/send/', ApplicationView.as_view(), name='application'),
    re_path(r'^vacancies/([\d-]+)/', VacancyView.as_view(), name='vacancy'),
    path('register/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = custom_handler404
handler500 = custom_handler500
