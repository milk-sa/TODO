from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)              # Required
    description = models.TextField()                      # Required
    due_date = models.DateField()                         # Required
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    """ The __str__ method in a Django model defines 
    how the object will be represented as a string.
     It is useful for displaying readable information 
     in the Django admin, shell, or when printing the object."""

