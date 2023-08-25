"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('blogcontent.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


















"""
In Django's URL routing system, the path function takes two arguments: the URL pattern to match and the view 
function to execute when that pattern is matched. In this case, path('', include('blogcontent.urls')) means 
that when a user visits the root URL of your website (e.g., http://example.com/), the URL routing system will 
look into the blogcontent.urls URL configuration to determine which view function should handle this request.
So, the '' in the path function is not a space but rather an empty string that represents the base URL of your 
application. It's a way of saying "when the user visits the main page of the website (root URL), use the URL 
patterns defined in 'blogcontent.urls' to determine the appropriate view to render.
"""