from django.contrib import admin
from django.urls import path, include 
from about_us import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from about_us.views import logout_view
from django.contrib.auth.views import LoginView
from about_us.views import birthday_view, occupation_view, height_view, weight_view, age_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about_us, name='about_us'), # considered as the home page for now
    path('members/', views.members_view, name='members'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('create_announcement/', views.create_announcement, name='create_announcement'),
    path('announcement/<int:announcement_id>/', views.announcement_detail, name='announcement_detail'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile_view, name='profile'),
    path('update-birthday/', views.birthday_view, name='update_birthday'),
    path('update-occupation/', views.occupation_view, name='update_occupation'),
    # path('update-yearjoined/', update_yearjoined, name='update_yearjoined'),
    path('update-height/', views.height_view, name='update_height'),
    path('update-weight/', views.weight_view, name='update_weight'),
    path('update-age/', views.age_view, name='update_age'),
    path('update-tin/', views.tin_view, name='update_tin'),
    path('update-jerseynum/', views.jerseynum_view, name='update_jerseynum'),
    path('update-gcashnum/', views.gcashnum_view, name='update_gcashnum'),
    path('update-team/', views.team_view, name='update_team')
    # path('update-jerseynumpic/', views.jerseynum_view, name="update_jerseynumpic"),
    # path('profile/', views.UserProfile, name='profile'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

