from django.contrib import admin
from django.urls import path, include
from todolistapp import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_views.index, name='index'),
    path('todolist/', include('todolistapp.urls')),
    path('contact', todolist_views.contact, name='contact'),
    path('about', todolist_views.about, name='about'),
    
]
