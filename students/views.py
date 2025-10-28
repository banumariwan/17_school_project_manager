from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import StudentForm
from .models import Student






def students_list(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', {'students': students})






def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})




def update_student(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})







def delete_student(request, id):
    student = get_object_or_404(Student,id=id)
    if request.method == "POST":
        student.delete()
        return redirect('students_list')
    return render(request, 'delete_student.html', {'student': student})



def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register_user.html', {'form': form})




def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('students_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login_user.html', {'form': form})



def logout_user(request):
        logout(request)
        return redirect('login')

