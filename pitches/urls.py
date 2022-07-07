from .views import ProjectPitchViewset
from rest_framework.routers import DefaultRouter

routes = DefaultRouter()

routes.register('pitches', ProjectPitchViewset, basename = 'pitches')

urlpatterns = [
    
    
]

urlpatterns += routes.urls



# from . import views
# from django.urls import path

# urlpatterns = [
#     path('pitches/', views.pitch_list),
#     path('pitches/<int:id>', views.pitch_detail),
# ]
