from django.urls import re_path, include
<<<<<<< HEAD
=======
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> 68ab61a7 (conf)

urlpatterns = [
    re_path(r'^suyo/', include('apps.users.urls')),
    re_path(r'^suyo/', include('apps.locations.urls')),
<<<<<<< HEAD
]
=======
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
>>>>>>> 68ab61a7 (conf)
