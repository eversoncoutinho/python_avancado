from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('urlpai/', include('blog.urls')), #a url pai
    
]
