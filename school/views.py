from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm, StaffForm, GuardianForm

def home(request):
    return render(request, 'home.html')

def create_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_guardian')
    else:
        form = StudentForm()
    form_name = form.__class__.__name__.replace('Form', '')  # Remove 'Form' and add space
    context = {"form": form, "form_name": form_name}
    return render(request, "student.html", context)

def create_staff(request):
    form = StaffForm()
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StaffForm()
    form_name = form.__class__.__name__.replace('Form', '')  # Remove 'Form' and add space
    context = {"form": form, "form_name": form_name}
    return render(request, "staff.html", context)

def create_guardian(request):
    form = GuardianForm()
    if request.method == 'POST':
        form = GuardianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = GuardianForm()
    form_name = form.__class__.__name__.replace('Form', '')
    context = {"form": form, "form_name": form_name}
    return render(request, 'guardian.html', context)

def success_page(request):
    return render(request, 'success.html')

