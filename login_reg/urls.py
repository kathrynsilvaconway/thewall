from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('process_reg', views.process_reg),
    path('process_login', views.process_login),
    path('success/<int:user_id>', views.render_success_page),
    path('logout', views.log_out),

]
