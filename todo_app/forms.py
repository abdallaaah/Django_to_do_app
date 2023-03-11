from django import forms
from .models import ToDoItem

class TodoItemForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = ToDoItem
        fields = ['title','description','todo_list','due_date']
        # fields_order = ['title','description','todo_list']