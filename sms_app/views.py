from django.shortcuts import render, redirect
from .models import Student

# Display all students
def Student_list(request):
    students = Student.objects.all()
    return render(request, "index.html", {"students": students})


# Add a new student
def add_student(request):
    if request.method == "POST":
        ID = request.POST['id']
        NAME = request.POST['name']
        Dept = request.POST['dept']

        Student.objects.create(
            id=ID,
            name=NAME,
            dept=Dept
        )

        return redirect("student_list")

    return render(request, "add_student.html")