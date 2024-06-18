from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home') ),
    path('examples/', include('examples.urls', namespace='examples')),
    path('resume/', include('resume.urls', namespace='resume')),
    path('skills/', include('skills.urls', namespace='skills')),
    path('design/', include('design.urls', namespace='design')),
    path('articles/', include('articles.urls', namespace='articles')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
