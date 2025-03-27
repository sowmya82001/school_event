from django.urls import path
from .views import home, signup, user_login, user_logout, event_list, create_event, register_event

urlpatterns = [
    path('', home, name='home'),  # Home Page
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('events/', event_list, name='event_list'),
    path('events/create/', create_event, name='create_event'),
    path('events/register/<int:event_id>/', register_event, name='register_event'),
]
