

from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('crud/', include('polls.urls2')),
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('refresh-token/', refresh_jwt_token),
]
