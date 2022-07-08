from django.urls import include,path
from . import views
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)



router.register('users', views.UserViewSet)




urlpatterns = [
    path('api/', include(router.urls)),
    path('account/', include('django.contrib.auth.urls')),
    path('<username>/profile', views.user_profile, name='userprofile'),
    path('profile/<username>/', views.profile, name='profile'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
