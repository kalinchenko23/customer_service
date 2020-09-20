"""customer_s URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from users.views import PdfCreateView,PdfListView,PdfUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/update_profile/', user_views.update_profile),
    path('pdf_files/', PdfListView.as_view(), name='pdf-list'),
    path('pdf_files/<int:pk>/login', user_views.send_email_pdf, name='pdf_email'),
    path('pdf_files/<int:pk>/', user_views.deleate_pdf, name='pdf_deleate'),
    path('pdf_files/<int:pk>/update', PdfUpdateView.as_view(), name='pdf_update'),
    path('register/',user_views.register, name="register"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('profile/',PdfCreateView.as_view(), name='pdf-create'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('',include('cs_app.urls')),

]
if settings.DEBUG:

    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)