from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    
    def __str__(self):
        return self.name


class Todo(models.Model):
    
    class StatusTypes(models.TextChoices):
        PENDING = "Pending"
        IN_PROGRESS = "In Progress"
        COMPLETED = "Completed"
    
    
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True)
    status = models.CharField(choices=StatusTypes.choices, default= StatusTypes.PENDING)
    
    
    @property
    def duration(self):
        date = self.completed_at - self.created_at
        return date.total_seconds
        
        
    
    def __str__(self):
        return self.title
    

