from django.urls import path
from WOF import views

app_name = 'WOF'

urlpatterns = [
	path('', views.index, name='index')
]
