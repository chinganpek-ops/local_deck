from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('journal.urls', namespace='journal')),
    path('pages/', include('pages.urls', namespace='pages')),
]
