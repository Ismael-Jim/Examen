from django.contrib import admin
from django.urls import path
from appnota3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('appnota3/', views.appnota3, name='appnota3'),
    path('appnota3/', views.appnota3_completed, name='appnota3_completed'),
    path('appnota3/crear/', views.crear_tarea, name='crear_tarea'),
    path('appnota3/<int:task_id>/', views.task_detail, name='task_detail'),
    path('appnota3/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('appnota3/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
