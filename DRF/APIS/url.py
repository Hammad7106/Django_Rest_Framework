from . import views
from django.urls import path
urlpatterns = [

    path('list/',views.student_list,name='student_list'),
    path('student_api/',views.student_api,name='student_api'),
]
