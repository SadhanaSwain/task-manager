from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.utils import timezone
from django.core.paginator import Paginator
from django.core.serializers.json import DjangoJSONEncoder
import json

from .models import Task
from .forms import TaskForm

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')


# ---------------------------
# DASHBOARD VIEW
# ---------------------------

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)

    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    category_filter = request.GET.get('category', '')
    tag_filter = request.GET.get('tags', '')
    sort_by = request.GET.get('sort_by', 'due_date')

    # ✅ Filter by search query
    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    if status_filter:
        tasks = tasks.filter(status=status_filter)

    if category_filter:
        tasks = tasks.filter(category=category_filter)

    if tag_filter:
        tasks = tasks.filter(tags__icontains=tag_filter)

    # ✅ Validate sort field
    valid_sort_fields = ['due_date', '-due_date', 'created_at', '-created_at', 'priority', '-priority', 'title', '-title']
    if sort_by not in valid_sort_fields:
        sort_by = 'due_date'

    tasks = tasks.order_by(sort_by)

    # ✅ Pagination
    paginator = Paginator(tasks, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'status_filter': status_filter,
        'category_filter': category_filter,
        'tag_filter': tag_filter,
        'sort_by': sort_by,
    })


@login_required
def create_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('dashboard')
    return render(request, 'create_task.html', {'form': form})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'edit_task.html', {'form': form})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('dashboard')
    return render(request, 'delete_task.html', {'task': task})


@login_required
def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if task.status == 'Completed':
        task.status = 'In Progress'
        task.completed_at = None
    else:
        task.status = 'Completed'
        task.completed_at = timezone.now()
    task.save()
    return redirect('dashboard')


@login_required
def analytics_dashboard(request):
    tasks = Task.objects.filter(user=request.user)

    status_data = tasks.values('status').annotate(count=Count('status'))
    category_data = tasks.values('category').annotate(count=Count('category'))

    status_json = json.dumps(list(status_data), cls=DjangoJSONEncoder)
    category_json = json.dumps(list(category_data), cls=DjangoJSONEncoder)

    return render(request, 'analytics.html', {
        'status_data': status_json,
        'category_data': category_json,
    })