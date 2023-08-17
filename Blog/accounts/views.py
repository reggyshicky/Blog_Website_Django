from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# views are functions that are incharge of processing a users request when they visit a certain url or endpoint in the website 
# func that posts to the view and view links the url to the db for storage, request is the http response. after all is done 
# The web page[index.html] will be loaded with the posted data ie posting a pic in fb
def post(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
        username = request.POST["user_name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, f"username already exists")
                return redirect("register")
            elif User.objects.filter(email = email).exists():
                messages.error(request, f"email already exist")
                return redirect("register")
            else:
                user = User.objects.create_user(first_name = firstname, last_name = lastname, username = username, email = email, password = password1)
                user.save()
                return redirect("content")
                
        else:
            messages.error(request, f"password not matching")
            return redirect("register")

    return render(request, "homepage.html")

