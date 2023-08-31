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
    
    class Meta:
        ordering = ("-date_of_post", )# to be order from the latest
    
    def __str__(self):
        return f"{self.title} {self.date_of_post}"
    
    @property # you can access it like an attribute , just like the above attributes
    def total_likes(self):
        likes = Like.objects.filter(post=self, liked=True)  #post in class Like
        total = 0
        if likes:
            for like in likes: #likes in line 30
                total += like.likes  #likes in line 41
        return total
        
        
    
class Like(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    liked = models.BooleanField(default=False)
    varbose_name_plural = "Likes"  # varbose_name_plural more like a keyword, if you want you admin to have whatever name you have named
    
    def __str__(self):
        return f"Total likes for {self.post.title} {self.likes}"
    
    
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
    
    
    
    
    
    
    
