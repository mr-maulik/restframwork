from django.contrib import admin
from django.urls import path,include
from apiapp import views
from .views import getid
from .views import deleteid
from .views import savedata


urlpatterns = [
    path('getall/',views.getall),
    path('getid/<int:id>/', getid, name='getid'),
    path('deleteid/<int:id>/', deleteid, name='deleteid'),
    path('savedata/', savedata, name='savedata'),
]
