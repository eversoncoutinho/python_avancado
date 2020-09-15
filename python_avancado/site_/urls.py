from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('urlpai/', include('blog.urls')), #a url pai
]
