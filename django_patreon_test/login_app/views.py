from rest_framework import views
from djoser.conf import settings
from rest_framework.response import Response
from rest_framework import status


class ObtainJWTTokenView(views.APIView):
    
    def get(self, request):
        tokens = settings.SOCIAL_AUTH_TOKEN_STRATEGY.obtain(request.user)

        data = {
            "access": tokens.get("access"),
            "refresh": tokens.get("refresh")
        }

        return Response(
            status=status.HTTP_200_OK,
            data=data
        )
