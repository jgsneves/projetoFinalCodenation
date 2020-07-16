from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterUserSerializer

# Create your views here.

@api_view()
@permission_classes([IsAuthenticated])
def get_users(request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def sign_up_user(request):
    serializer = RegisterUserSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['username'] = account.username
        data['email'] = account.email
    else:
        data = serializer.errors
    return Response(data)