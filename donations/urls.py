
from .views import DonationsViewset
from rest_framework.routers import DefaultRouter

routes = DefaultRouter()

routes.register('donations', DonationsViewset, basename = 'donations')

urlpatterns = [
    
    
]

urlpatterns += routes.urls






# from . import views
# from django.urls import path, include
# from django.conf.urls.static import static

# urlpatterns =[
#     path('api/donations/', views.DonationsViewset.as_view(), name='donations'),

# ]