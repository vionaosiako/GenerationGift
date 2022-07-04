from django.urls import include,path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)


urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
