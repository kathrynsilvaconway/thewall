from django.urls import path

from . import views

urlpatterns = [
    path('', views.project_index),
    path('add_message', views.add_message),
    path('add_comment/<int:message_id>', views.add_comment),
    path('profile', views.open_profile),
    path('delete_post/<int:id>', views.delete_post)
]
