from .models import User ,TaskModel
from .serializers import UserSerializer ,TaskSerializers
from django.contrib.auth import authenticate, login
from rest_framework import status ,filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated  


class UserRegistrationView(APIView):
    permission_classes = []
    def post(self, request):
        data = request.data
        data["username"] = data.get("email")
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserLoginView(APIView):
    permission_classes = []
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)

            response = Response({
                'message': 'Login successful',
                'username': user.username,
                'role': user.role,
            })

            response.set_cookie(
                key='Authorization',
                value=f'Token {token.key}',
                httponly=True,
                samesite='Lax',  # or 'None' if using HTTPS and cross-site
                secure=False,    # set to True in production with HTTPS
            )
            return response
        return Response({'message': 'Invalid credentials'}, status=401)



class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.headers) 
        token_key = request.auth.key
        token = Token.objects.get(key=token_key)
        token.delete()

        return Response({'detail': 'Successfully logged out.'})


class TaskManagementView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        serializer = TaskSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data , status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors , status=status.HTTP_400_BAD_REQUEST )
    
    def get(self,request):
        queryset = TaskModel.objects.all()

        # Get query parameters
        status = request.query_params.get('status')
        created_at = request.query_params.get('created_at')
        updated_at = request.query_params.get('updated_at')
        # user = request.query_params.get('user')  
        name = request.query_params.get('name')

        # Apply filters
        if status:
            queryset = queryset.filter(status=status)

        if created_at:
            queryset = queryset.filter(created_at__date=created_at)

        if updated_at:
            queryset = queryset.filter(updated_at__date=updated_at)

        # if user:
        #     queryset = queryset.filter(user_id=user)  

        if name:
            queryset = queryset.filter(name__icontains=name)

        serializer = TaskSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def patch(self, request, task_id):
        task = TaskModel.objects.filter(id=task_id).first()
        if not task:
            return Response(data={"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        task_status = request.data.get("status")
        if task_status is None:
            return Response(data={"error": "Task status required to update"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TaskSerializers(instance=task, data={"status": task_status}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

