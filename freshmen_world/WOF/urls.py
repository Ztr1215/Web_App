from django.urls import path
from WOF import views

app_name = 'WOF'

urlpatterns = [
	path('', views.index, name='index'),
	path('base/', views.base, name='base'),
	path('login/', views.user_login, name='user_login'),
	path('register/', views.user_register, name='user_register'),
	path('course_selector/', views.selector, name='selector'),
	path('taskmanager/', views.task_manager, name='task_manager'),
	path('logout/', views.user_logout, name='logout'),
	path('team/', views.team_members, name='team'),
	path('profile/', views.profile, name='profile')
]
