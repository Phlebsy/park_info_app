from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.addCode, name="addCode"),
    path('addCode', views.addCode, name='addCode'),
    path('viewAll', views.viewAll, name="viewAll"),
    path('viewCode/<str:parkcode>', views.viewCode, name="viewCode"),
    path('clearData', views.clearData, name="clearData")
]
