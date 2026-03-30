from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import UserProfile

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            try:
                profile = user.userprofile
            except UserProfile.DoesNotExist:
                return render(
                    request,
                    'login.html',
                    {'error': 'Your account is not activated yet. Please contact admin.'}
                )

            if profile.role == 'teacher':
                return redirect('teacher_dashboard')

            elif profile.role == 'student':
                return redirect('student_dashboard')

        return render(
            request,
            'login.html',
            {'error': 'Invalid username or password'}
        )

    return render(request, 'login.html')


def teacher_dashboard(request):
    return render(request, 'teacher.html')

def student_dashboard(request):
    return render(request, 'student.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AssignmentForm

@login_required
def create_assignment(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.teacher = request.user
            assignment.save()
            return redirect("teacher_assignments")  # redirect after save
    else:
        form = AssignmentForm()

    return render(request, "create_assignment.html", {
        "form": form
    })


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Assignment
from .forms import AssignmentForm


@login_required
def assignment_list(request):
    assignments = Assignment.objects.filter(teacher=request.user).order_by("-created_at")
    return render(request, "assignment_list.html", {
        "assignments": assignments
    })


@login_required
def edit_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, teacher=request.user)

    if request.method == "POST":
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect("teacher_assignments")
    else:
        form = AssignmentForm(instance=assignment)

    return render(request, "edit_assignment.html", {
        "form": form,
        "assignment": assignment
    })


@login_required
def delete_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, teacher=request.user)

    if request.method == "POST":
        assignment.delete()
        return redirect("teacher_assignments")

    return render(request, "delete_assignment.html", {
        "assignment": assignment
    })


from django.shortcuts import render
from .models import Assignment

def student_assignments(request):
    assignments = Assignment.objects.all().order_by("due_date")
    return render(request, "student_assignment.html", {
        "assignments": assignments
    })
