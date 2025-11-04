from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenida a Liher Fashion 🛍️ — desplegado con éxito en Render")

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('appLiher.urls')),  # Rutas de la app
    path('accounts/', include('allauth.urls')),  # Google login y demás
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)