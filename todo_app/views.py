from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import ToDoList,ToDoItem
from django.urls import reverse_lazy
from .forms import TodoItemForm
# Create your views here.
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
class ListView(ListView):
    model = ToDoList
    template_name = 'todo_app/index.html'

        
    def get_queryset(self):
        return ToDoList.objects.all()
        return ToDoItem.objects.all()

class ItemListView(ListView):
    
    model = ToDoItem
    template_name = 'todo_app/todo_list.html'

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id = self.kwargs['list_id'])  ### coming form url <int:list_id> ###
    
    def get_context_data(self):
        context = super().get_context_data()
        context ['todo_list'] = ToDoList.objects.get(id= self.kwargs['list_id'])
        return context

class ListCreate(CreateView):

    model = ToDoList
    fields = '__all__'
    template_name = 'todo_app/todo_create.html'
    success_url = reverse_lazy('index')

    # def get_queryset(self):
    #     return 

    

# class ItemCreate(CreateView):

#     # model = ToDoItem
#     form = TodoItemForm
#     fields = '__all__'
#     template_name = 'todo_app/todo_create.html'
#     # success_url = reverse_lazy('index')

#     def get_context_data(self):
#         context = super(ItemCreate,self).get_context_data()
#         context['title'] = "xx"
#         return context

def ItemCreate(request, pk=None):
    list = ToDoList.objects.get(id=pk)
    print(list)
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list', pk)

    else: 
        form=TodoItemForm(initial={"todo_list":list})
    context={
        'form': form,
      
        
    }
    return render(request,"todo_app/itemcreat_form.html",context)

class UpdateList(UpdateView):
    model = ToDoList
    fields = '__all__'
    template_name = 'todo_app/todo_create.html'
    success_url = reverse_lazy('index')

class UpdateItem(UpdateView):
    model = ToDoItem
    fields = '__all__'
    template_name = 'todo_app/todo_create.html'
    success_url = reverse_lazy('index')


class DeleteList(DeleteView):
    model = ToDoList
    context_object_name = "list"
    success_url = reverse_lazy('index')

class DeleteItem(DeleteView):
    model = ToDoItem
    context_object_name = "list"
    template_name = "todo_app/todolist_confirm_delete.html"
    success_url = reverse_lazy('index')

    # def get_queryset(self):
    #     return ToDoList.objects.get(id = self.kwargs['list_id'])  ### coming form url <int:list_id> ###

    # def get_context_data(self):
    #     context = super().get_context_data()
    #     context ['item'] = ToDoList.objects.get(id= self.kwargs['list_id'])
    #     return context
    








# class ItemCreate(CreateView):
#     Model = ToDoItem
#     fields = ['todo_list',
#                'title',
#                'description',
#                'due_date',
#             ]

#     template_name = ''
        
