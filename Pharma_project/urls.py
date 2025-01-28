
from django.urls import path
from django.urls import path,include

urlpatterns = [
    
     path('admin/', admin.site.urls),
    path('',include('Pharma_app.urls'))
]
