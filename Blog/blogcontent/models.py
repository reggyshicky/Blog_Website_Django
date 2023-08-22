from django.db import models
from  datetime import date
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length = 100)
    
    def __str__(self):
        return f"{self.category}"
# Our blogs wil belong to this categories, a category may have more than one blog- One to many relationship, will use FK   



class Blog(models.Model):
    title = models.CharField(max_length = 200)
    post = models.TextField() # TextField is the type of the post, which is text
    name = models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE- if user is deleted, there posted content is deleted as well
    date_of_post = models.DateField(default=date.today) 
    description = models.TextField(max_length = 200)
    image = models.ImageField(upload_to = "images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # 1 represents to the PK of our default category
    
    def __str__(self):
        return f"{self.title} {self.date_of_post}"
    
    
    
    
