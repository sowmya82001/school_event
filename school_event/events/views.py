from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Event, EventRegistration
from .forms import SignupForm, EventForm

# Signup View
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('event_list')
    else:
        form = SignupForm()
    return render(request, 'events/signup.html', {'form': form})

# Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('event_list')
    return render(request, 'events/login.html')

# Logout View
def user_logout(request):
    logout(request)
    return redirect('login')

# List Events
@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

# Create Event (Admin Only)
@login_required
def create_event(request):
    if request.user.role != 'admin':
        return redirect('event_list')

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()

    return render(request, 'events/create_event.html', {'form': form})

# Register for Event (Student Only)
@login_required
def register_event(request, event_id):
    event = Event.objects.get(id=event_id)
    EventRegistration.objects.create(event=event, student=request.user)
    return redirect('event_list')

def home(request):
    return render(request, 'events/home.html')