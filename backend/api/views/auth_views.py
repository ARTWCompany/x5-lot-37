from rest_framework_simplejwt.views import TokenObtainPairView

from api.serializers import LogInSerializer


class LogInView(TokenObtainPairView):
    serializer_class = LogInSerializer
