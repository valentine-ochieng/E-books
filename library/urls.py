from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('subscribe/',views.subscription, name='subscription'),
    path('register/', views.register, name='register'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search_results, name='search'),
    path('post_book/',views.post_book, name='post_book'),
    path('library/',views.library, name='library'),
    path('post_newbook/',views.newbook, name='newbook'),
    path('about/', views.service, name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)