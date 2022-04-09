from django.contrib import admin
from django.urls import path, include
from main.views import actiovation_post

urlpatterns = [
    path('api-docs/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/users/activation/<str:uid>/<str:token>', actiovation_post)
    # path('auth/', include('djoser.urls.jwt')),
]
