from django.contrib import admin
from django.urls import include, path

app_name = 'infra_app'

urlpatterns = [
    path('', include('infra_app.urls', namespace='infra_app')),
    path('admin/', admin.site.urls),
]
