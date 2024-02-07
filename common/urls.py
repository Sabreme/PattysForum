from django.urls import path

from . import views
app_name = 'common'

urlpatterns = [
    path('metrics/', views.metrics, name='metrics')
]
