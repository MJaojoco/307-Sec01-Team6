"""CSC307_LyncUp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path, include
from users import views as user_views
from LyncUp import views as LyncUp_views


#from django.conf.urls import include, url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('friends_list/', user_views.FriendListView.as_view(template_name = 'users/friends_list.html'), name="friends_list"),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('friends_list/addfriend/', user_views.add_friends, name='addfriend'),
    path('friends_list/removefriend/', user_views.remove_friends, name='removefriend'),
    #url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', user_views.add_friends, name='add_friends'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('LyncUp.urls')),
    path('', include('timetable.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

