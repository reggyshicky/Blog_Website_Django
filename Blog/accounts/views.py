from django.shortcuts import render

# func that posts to the view and view links the url to the db for storage, request is the http response. after all is done 
# The web page[index.html] will be loaded with the posted data ie posting a pic in fb
def post(request):
    return render(request, "index.html")

def home(request):
    return render(request, "homepage.html")

