from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter

#CREATING ROUTER OBJECT
router=DefaultRouter()


#REGISTER STUENT VIEWSET WITH ROUTERS
router.register('studentapi',views.Student_ViewSet,basename='student')
urlpatterns = [
       path('',include(router.urls))
    # # path('list/',views.student_list,name='student_list'),
    # # path('api/',views.api,name='api'),
    # # path('api/<int:pk>',views.api,name='api'),
    #   path('studentapi/',views.Student_List_Create.as_view(),name='api'),
    # #   path('studentapi/',views.Student_Post.as_view(),name='api'),
    # #   path('studentapi/<int:pk>',views.Student_Retrieve.as_view(),name='api'),
    # #   path('studentapi/<int:pk>',views.Student_Update.as_view(),name='api'),
    #   path('studentapi/<int:pk>',views.Student_Retrieve_Update_Destroy.as_view(),name='api'),
    #    path('studentapi/',views.List_Create.as_view(),name='api'),
    #    path('studentapi/<int:pk>',views.RetrieveUpdateDestroy.as_view(),name='api'),
]
