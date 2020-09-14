from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .settings import SIMPLE_JWT


class CustomizeTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data['access'] = str(refresh.access_token)
        data['refresh'] = str(refresh)
        data['access_expires'] = int(SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds())
        data['refresh_expires'] = int(SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds())

        return data


class CustomizeTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomizeTokenObtainPairSerializer
