from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .models import Report
from .serializers import UserSerializer, RegisterUserSerializer, ReportSerializer
from django.shortcuts import get_object_or_404

# Users views #

@api_view()
@permission_classes([IsAuthenticated])
def get_users(request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
@permission_classes([IsAuthenticated])
def get_single_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user)
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

# Report views #

@api_view()
@permission_classes([IsAuthenticated])
def get_reports(request):
    queryset = Report.objects.all()
    serializer = ReportSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def handle_single_report(request, pk):
    report = get_object_or_404(Report, pk=pk)

    if request.method == 'GET':
        serializer = ReportSerializer(report)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ReportSerializer(report, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Report changed"})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        operation = report.delete()

        if operation:
            return Response({"message": "Report Deleted"})
        else:
            return Response({"message": "Report not deleted"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_report(request):
    serializer = ReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)