from django.urls import path
from remainder_api import views


urlpatterns=[
    path("v3/todos/register",views.UserCreationView.as_view()),

    
]