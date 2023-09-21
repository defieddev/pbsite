from django.contrib import admin
from django.urls import path, include 
from about_us import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about_us, name='about_us'), # considered as the home page for now
    path('members/', views.members, name='members'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('create_announcement/', views.create_announcement, name='create_announcement'),
    path('announcement/<int:announcement_id>/', views.announcement_detail, name='announcement_detail'),
    path('search/', views.search, name='search'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

