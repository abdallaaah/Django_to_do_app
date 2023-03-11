from django.db import models

# Create your models here.
from django.utils import timezone
from django.urls import reverse

def one_week_hence():

    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title = models.CharField(max_length=500, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title

class ToDoItem(models.Model):

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500,blank=True,null=True) 
    creation_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList,on_delete=models.CASCADE,related_name='items')

    def get_absolute_url(self):
        return reverse("item-update", args=[str(self.todo_list.id), str(self.id)])

    def __str__(self):
        return f"{self.title}: due {self.due_date}"
    
    class Meta:
        ordering  =  ['due_date']
    


    