from django.urls import path
from . import views 

urlpatterns = [
    
    path('datanasabah/', views.index, name='datanasabah'),
    path('createnasabah/', views.createnasabah, name='createnasabah'),
    path('updatenasabah/<str:pk>', views.updatenasabah, name='updatenasabah'),
    path('deletenasabah/<str:pk>', views.deletenasabah, name='deletenasabah'),
    
]