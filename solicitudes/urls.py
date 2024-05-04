from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

from . import views

urlpatterns = [
    path('solicitudes/', views.variable_list, name='solicitudesList'),
    path('solicitudes/<id>', views.single_variable, name='singleSolicitud'),
    path('solicitudcreate/', csrf_exempt(views.variable_create), name='solicitudCreate'),
]
