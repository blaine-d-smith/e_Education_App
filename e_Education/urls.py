from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from courses import views

urlpatterns = [
    path(
        'accounts/login/',
        views.login_user,
        name='login'
    ),
    path(
        'accounts/logout',
        views.logout_user,
        name='logout'
    ),
    path(
        'admin/',
        admin.site.urls
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
