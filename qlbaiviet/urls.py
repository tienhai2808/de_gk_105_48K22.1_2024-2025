from django.urls import path
from .views import *

urlpatterns = [
  path('', index),
  path('xembaiviet/<int:idbaiviet>/', xembaiviet, name='xembaiviet'),
  path('dsbaiviet/<int:idchuyenmuc>/', dsbaiviet),
  path('suabaiviet/<int:idbaiviet>/', suabaiviet),
  path('taobaiviet/', suabaiviet)
]