from django.urls import include,path
from . import views
from rest_framework import routers

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
