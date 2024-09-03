from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("<int:num1>",views.course_number,name="coursenumber"),
    path("<int:num1>-<int:num2>",views.carp,name="carp"),
    path("<str:item>",views.course,name="course"),
    path("<int:num1>/<int:num2>/",views.multiply_view,name="multiply"),
    
]