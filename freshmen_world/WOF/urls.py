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
	path('selector/course/<slug:course_name_slug>/delete_course', views.delete_course, name='delete_course'),
	path('selector/course/<slug:course_name_slug>/', views.show_course, name='show_course'),
	path('selector/course/<slug:course_name_slug>/uni_course_info.txt', views.get_course_info, name='get_course_info'),
	path('selector/university/<slug:university_name_slug>/', views.show_university, name='show_university'),
	path('taskmanager/', views.task_manager, name='task_manager'),
	path('taskmanager/add_task/', views.add_task, name="add_task"),
	path('taskmanager/server/', views.find_tasks_month, name='find_tasks'),
	path('logout/', views.user_logout, name='logout'),
	path('error/', views.error, name="error"),
	path('team/', views.team_members, name='team'),
	path('profile/', views.profile, name='profile'),
	path('profile/delete_university/', views.delete_university, name="delete_university"),
]
