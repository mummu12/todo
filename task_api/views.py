from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from task_api.serializers import Todoserializer
from task.models import Todos
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.decorators import action

class TodoViewSetView(ViewSet):

    def list(self,request,*args,**kwargs):
        qs=Todos.objects.all()
        serializer=Todoserializer(qs,many=True)
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=Todoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Todos.objects.get(id=id)
        serailizer=Todoserializer(qs)
        return Response(data=serailizer.data)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Todos.objects.get(id=id)
        serializer=Todoserializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

  
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Todos.objects.filter(id=id).delete()
        return Response(data={"message":"student deleted"})

class TodoModelViewSetView(ModelViewSet):
    serializer_class=Todoserializer
    queryset=Todos.objects.all()


# localhost:8000/api/v3/todos/pending
# method=get
    @action(methods=["get"],detail=False)
    def pending(self,request,*args,**kwargs):
        qs=Todos.objects.filter(status=False)
        serializer=Todoserializer(qs,many=True)
        return Response(data=serializer.data)
    

    @action(methods=["get"],detail=False)
    def completed(self,request,*args,**kwargs):
        qs=Todos.objects.filter(status=True)
        serializer=Todoserializer(qs,many=True)
        return Response(data=serializer.data)

