from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('books/',include('books.urls')),
    path('comments/',include('comments.urls'))
]
