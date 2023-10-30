from . import views
from django.urls import path
urlpatterns = [

    path('list/',views.student_list,name='student_list'),
    path('api/',views.api,name='api'),
    path('api/<int:pk>',views.api,name='api'),
]
