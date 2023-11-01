from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from remainder.forms import RegistrationForm,LoginForm,TodoCreateForm,TodoChangeForm
from django.views.generic import View,TemplateView,FormView,ListView,DetailView,UpdateView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from remainder.models import Todos
from django.utils.decorators import method_decorator
# Create your views here.



def login_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session please login!!!")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
        
    return wrapper




class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"signup.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registration completed succesfully")
            return redirect("signin")
        else:
            messages.error(request,"registration failed")
            return render(request,"signup.html",{"form":form})
            #User.objects.create_user(**form.cleaned_data)

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(uname,pwd)
            usr=authenticate(request,username=uname,password=pwd)
            print(usr)
            if usr:
                login(request,usr)
                messages.success(request,"login success")
                return redirect("index")
            else:
                messages.error(request,"invalid credentails!!!")
                return render(request,"login.html",{"form":form})
            

@method_decorator(login_required,name="dispatch")
class IndexView(View):
    template_name="index.html"

    def get(self,request,*args,**kwargs):
        form=TodoCreateForm()
        qs=Todos.objects.filter(user=request.user)
        return render(request,self.template_name,{"form":form,"todos":qs})
    def post(self,request,*args,**kwargs):
        form=TodoCreateForm(request.POST)
        if form.is_valid():
            Todos.objects.create(**form.cleaned_data,user=request.user)
            return redirect("index")
        else:
            return redirect("index")
        


# --------------------------------------------
#   template_name="index.html"
#   form_class=TodoCreateForm
#   contex_object_name="todos"
#   success_url=reverse_lazy('index')
#   model="todos"
# def form_valid(self,form):
#     form.instance.user=request.user
#     return super().form_valid(form)
# ----------------------------------------------
# def post():
#     form=TodoCreateForm(request.POST)
#     if form.is_valid():
#         form.instance.user=request.user
#         form.save()
#         return redirect("index")
# -----------------------------------------------
# def get_queryset(self):
#     qs=-Todos.objects.filter(self.request.user)
#     return qs
# -------------------------------------------------
        
    



# class TodoCreateView(FormView):
#     template_name="remainder/todo_add.html"
#     form_class=TodoCreateForm
@method_decorator(login_required,name="dispatch")
class TodoCreateView(View):
    def get(self,request,*args,**kwargs):
        form=TodoCreateForm()
        return render(request,"remainder/todo_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=TodoCreateForm(request.POST)
        if form.is_valid():
            #form.save(user=request.user)
            Todos.objects.create(**form.cleaned_data,user=request.user)
            messages.success(request,"todo added successfully")
            return redirect("list-todo")
        
        else:
            messages.error(request,"operation failed")
            return render(request,"remainder/todo_add.html",{"form":form})
        
@method_decorator(login_required,name="dispatch")
class TodoListView(ListView):
    template_name="remainder/todo_list.html"
    context_object_name="todos"
    model=Todos
    
    def get_queryset(self):
        qs=Todos.objects.filter(user=self.request.user)
        return qs

    
    # def get(self,request,*args,**kwargs):
    #     qs=Todos.objects.all()
    #     return render(request,self.template_name,{"todos":qs})

@method_decorator(login_required,name="dispatch")
class TododetailView(DetailView):
    template_name="remainder/todo_detail.html"
    context_object_name="todo"
    model=Todos


# lh:8000/v1/todos/v1/change/
@method_decorator(login_required,name="dispatch")
class TodoUpdateView(UpdateView):
    template_name="remainder/todo_edit.html"
    form_class=TodoChangeForm
    model=Todos
    success_url=reverse_lazy("list-todo")





# def get(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         obj=Todos.objects.get(id=id)
#         form=TodoChangeForm(instance=obj)
#         return render(request,self.template_name,{"form":form})

#     def post(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         obj=Todos.objects.get(id=id)
#         form=TodoChangeForm(request.POST,instance=obj)
#         if form.is_valid():
#             form.save()
#             return redirect("list-todo")
#         else:
#             return render(request,"todo_edit.html",{"form":form})
        
        


@login_required   
def remove_todo(request,*args,**kwargs):
    id=kwargs.get("pk")
    Todos.objects.filter(id=id).delete()
    return redirect("list-todo")





