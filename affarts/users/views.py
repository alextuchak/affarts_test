from rest_framework.views import APIView
from .serializers import UserSerializer
from django.http import JsonResponse


class Register(APIView):
    serializers_class = UserSerializer

    def post(self, request):
        user_serializers = self.serializers_class(data=request.data)
        if user_serializers.is_valid():
            user = user_serializers.save()
            user.set_password(request.data['password'])
            user.save()
            return JsonResponse({'Status': True}, status=201)
        else:
            return JsonResponse({'Status': False}, status=403)

