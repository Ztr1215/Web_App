from django.urls import path
from WOF import views

app_name = 'WOF'

urlpatterns = [
	path('', views.index, name='index'),
	path('login/', views.user_login, name='user_login'),
	path('register/', views.user_register, name='user_register'),
	path('selector/', views.selector, name='selector'),
	path('selector/add_university', views.add_university, name='add_university'),
	path('selector/add_course/', views.add_course, name='add_course'),
	path('selector/course/<slug:course_name_slug>/', views.show_course, name='show_course'),
	path('selector/course/<slug:course_name_slug>/uni_course_info.txt', views.get_course_info, name='get_course_info'),
	path('selector/university/<slug:university_name_slug>/', views.show_university, name='show_university'),
	path('taskmanager/', views.task_manager, name='task_manager'),
	path('logout/', views.user_logout, name='logout'),
	path('team/', views.team_members, name='team'),
	path('profile/', views.profile, name='profile'),

]
