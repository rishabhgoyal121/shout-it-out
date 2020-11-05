from django.contrib import admin
from django.urls import path
import shoutitout.api_views

urlpatterns = [
    path('api/v1/users/', shoutitout.api_views.UserList.as_view()),
    path('api/v1/users/new', shoutitout.api_views.UserCreate.as_view())
    path('api/v1/users/<int:id>/', shoutitout.api_views.UserRetrieveUpdateDestroy.as_view())
    path('admin/', admin.site.urls),
]
