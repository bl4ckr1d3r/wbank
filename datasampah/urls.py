from django.urls import path
from . import views 

urlpatterns = [
    
    path('datasampah/', views.index, name='datasampah'),
    path('createsampah/', views.createsampah, name='createsampah'),
    path('updatesampah/<str:pk>', views.updatesampah, name='updatesampah'),
    path('deletesampah/<str:pk>', views.deletesampah, name='deletesampah'),
    
]