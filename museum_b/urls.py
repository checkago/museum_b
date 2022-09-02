from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('muzy', views.muzy, name='muzy'),
    path('golosa', views.voices, name='golosa'),
    path('osipov', views.osipov, name='osipov'),
    path('tropa', views.tropa, name='tropa'),
    path('foto', views.foto, name='foto'),
    path('simphony/', views.simphony, name='simphony'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('books/', views.books, name='books'),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        urlpatterns += staticfiles_urlpatterns()
