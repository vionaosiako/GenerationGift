from .views import TrainingViewset
from rest_framework.routers import DefaultRouter

routes = DefaultRouter()

routes.register('trainings', TrainingViewset, basename = 'trainings')

urlpatterns = [
    
]

urlpatterns += routes.urls