from django.urls import path
from sms_app import views
urlpatterns=[
    path('',views.Student_list,name="student_list"),
    path('add_student/',views.add_student,name="add_student")
]