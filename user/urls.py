from .views import *
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', Tasklist.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='delete-task'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
    path(
            "favicon.ico",
            RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
        ),
]
