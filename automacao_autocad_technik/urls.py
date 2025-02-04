from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('extracao-de-tags/', include('extracao_de_tags.urls'))
]
