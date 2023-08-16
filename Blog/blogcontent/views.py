from django.shortcuts import render

def postcontent(request):
    return render(request, 'postcontent.html')
