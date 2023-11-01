from django.urls import path
from task_api import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("v1/todos",views.TodoViewSetView,basename="v2todos")
router.register("v2/todos",views.TodoModelViewSetView,basename="v3todos")


urlpatterns=[

    
]+router.urls