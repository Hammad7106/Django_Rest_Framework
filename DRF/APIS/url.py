from . import views
from django.urls import path
urlpatterns = [

    # path('list/',views.student_list,name='student_list'),
    # path('api/',views.api,name='api'),
    # path('api/<int:pk>',views.api,name='api'),
      path('studentapi/',views.Student_List_Create.as_view(),name='api'),
    #   path('studentapi/',views.Student_Post.as_view(),name='api'),
    #   path('studentapi/<int:pk>',views.Student_Retrieve.as_view(),name='api'),
    #   path('studentapi/<int:pk>',views.Student_Update.as_view(),name='api'),
      path('studentapi/<int:pk>',views.Student_Retrieve_Update_Destroy.as_view(),name='api'),
]
