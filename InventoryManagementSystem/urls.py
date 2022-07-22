from django.contrib import admin
from django.urls import path, include
from user import views as user_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('register/', user_view.register, name='user-register'),

]
