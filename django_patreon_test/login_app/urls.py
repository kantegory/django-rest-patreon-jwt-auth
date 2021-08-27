from login_app.views import ObtainJWTTokenView
from django.urls import path

urlpatterns = [
    path('auth/obtain-jwt/', ObtainJWTTokenView.as_view())
]
