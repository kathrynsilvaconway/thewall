
from django.urls import path, include

urlpatterns = [
    path('', include('login_reg.urls')),
    path('wall/', include('project_app.urls'))
]
