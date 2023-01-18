from django.urls import path
from . import views 

urlpatterns = [
    
    path('datapenarikan/', views.index, name='datapenarikan'),
    path('createpenarikan/', views.createpenarikan, name='createpenarikan'),
    path('updatepenarikan/<str:pk>', views.updatepenarikan, name='updatepenarikan'),
    path('deletepenarikan/<str:pk>', views.deletepenarikan, name='deletepenarikan'),
    
]