from django.shortcuts import render, redirect
from .models import Blog, Comment, Review
from .models import Category
from .forms import CommentForm


def postcontent(request):
    posts = Blog.objects.all() #objects.all fetch everything from the db and will store it in posts
    context = {
        "posts": posts # the first post is our key, returned from  Blog.objects.all(), and the second 
        # post is the one in the html file {% for post in (posts) %} for loopinig as we print the values 
        # of the key
    }
    return render(request, 'postcontent.html', context)

def detail_page(request, pk):  # PK is the primary key
    post = Blog.objects.get(pk=pk) #get() returns only one
    comments = Comment.objects.filter(post_comment = pk)
    context = {
        "post": post,
        "comments": comments
    }
    
    return render(request, "details_page.html", context)

def all_categories(request):
    categories = Category.objects.all()
    context = {
        "categories" : categories,
    }
    return render(request, 'category.html', context)

def each_category(request, the_category):
    
    posts = Blog.objects.filter(category__category = the_category) #category__category access the attr on the Blog
    
    context = {
        "posts" : posts,
        "cat" : the_category,
    }

    return render(request, 'each_category.html', context)
# categories on the homepage

def comment(request, pk): #pk -id of the post being commented on 
    post = Blog.objects.get(pk=pk) #second pk the arg in function, the fi
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data["comment"] #secondcomment is in html. 
            user = request.user
            post_comment = post
            
            comment = Comment.objects.create(comment=comment,
                                             user = user,
                                             post_comment = post_comment
                                             )
            comment.save()
        else:
            print(form.errors)
    return redirect("details", pk)

def review(request, pk): #pk  -id of the post being commented on
    
    postreview = Blog.objects.get(pk=pk) # get gets one object/instance of the pk passed
    all_reviews = Review.objects.filter(post_review = postreview)
    
    if request.method == "POST":
        user_review = request.POST.get("review", "") # review is name on the html page, we extracting the review from user 
        if user_review:
            reviews = Review.objects.filter(user=request.user, post_review=postreview)
            
            if reviews.count() > 0:  # user has to review a blog once
                first_review = reviews.first()
                first_review.review = user_review # review of the current user, the first review we extract from our objects
                first_review.save()
                
            else: #creates  a new instance of review
                first_review = Review.objects.create(
                    post_review = postreview,
                    user = request.user,
                    review = user_review
                )
                
        return redirect("review", pk=postreview.pk)
    context = {
        "postreview" : postreview,
        "user" : request.user,
        "all_reviews" : all_reviews
    }
                
    return render(request, "review.html", context)

    