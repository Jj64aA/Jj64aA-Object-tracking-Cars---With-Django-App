from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
   path('',views.main , name="home"),
   path('Show/' ,views.show),
   path('Test/' , views.test , name="test"),
   path('NoDataFound/', views.data_found) , 
   path('Contact/', views.contact , name="contact")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


