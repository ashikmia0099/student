from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomeView ),
    path('all_course_page/',views.AllcoursePage, name='all_course_page'),
    path('category_page/',views.CategoryPage, name='category_page'),
    path('seminer_page/',views.SeminerPage, name='seminer_page'),
    path('video_page/',views.VideoPage, name='video_page'),
    
]
