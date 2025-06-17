from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Todo(models.Model):
    
    STATUS_TYPES = [
        'PENDING',
        'IN PROGRESS',
        'COMPLETED'
    ]
    
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField()
    status = models.CharField(choices=STATUS_TYPES)
    
    def __str__(self):
        return self.title
    

