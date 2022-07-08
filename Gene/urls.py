from .views import EmployerViewset
from rest_framework.routers import DefaultRouter

routes = DefaultRouter()

routes.register('employer', EmployerViewset, basename = 'employer')

urlpatterns = [
    
    
]

urlpatterns += routes.urls