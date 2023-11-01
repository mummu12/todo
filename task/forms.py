from django import forms
from task.models import Todos

class TodoCreateForm(forms.Form):
    title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    user=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    due_date=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"date"}))



# class TodoChangeForm(forms.Form):
#     title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     due_date=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"date"}))
#     status=forms.BooleanField()



class TodoChangeForm(forms.ModelForm):
    
    class Meta:
        model = Todos
        fields = ["title","status","due_date"]

        widgets={
            "tittle":forms.TextInput(attrs={"class":"form-control"}),
            "due_date":forms.TextInput(attrs={"class":"form-control","type":"date"})
        }