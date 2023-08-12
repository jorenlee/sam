from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('api/hello/', include('helloworld.urls')),
    path('admin/', admin.site.urls),
]
