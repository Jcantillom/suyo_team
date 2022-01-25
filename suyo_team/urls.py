from django.urls import re_path, include

urlpatterns = [
    re_path(r'^suyo/', include('apps.users.urls')),
    re_path(r'^suyo/', include('apps.locations.urls')),
]
