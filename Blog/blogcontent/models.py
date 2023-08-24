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
    post_likes = models.ManyToManyField(User, blank=True, related_name="like") #tracks likes, blank=True,  its not a must for a blog to be liked
    liked = models.BooleanField(default=False)  # tracks if user has liked or not
    
    
    
    def __str__(self):
        return f"{self.title} {self.date_of_post}"

class Comment(models.Model):
    comment = models.TextField(max_length = 250)
    date_of_comment = models.DateField(auto_now_add = True) #means if a user comments, the time they commented shall always remain
    user = models.ForeignKey(User, on_delete=models.PROTECT) #protect means you can delete user who has comments, you have delete commnets first and the you can delete the user
    post_comment = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} {self.post_comment}"
    
class Review(models.Model):
    post_review = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date_of_review = models.DateField(auto_now_add = True)
    review = models.TextField(max_length=300)
    
    def __str__(self):
        return f"Review for {self.post_review} by {self.user.username}"
    
    
    
    
    
    
    
