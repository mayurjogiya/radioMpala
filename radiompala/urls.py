from django.contrib import admin
from django.urls import include, path
from django.conf import settings  
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stores.urls')),
    path('manage/', include('managers.urls')),
    path('surapura/', include('Surapuradada.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
