from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework import status, permissions, generics, filters
from rest_framework.views import APIView , View
from rest_framework.response import Response
from .permissions import  IsOwnerOrReadOnly, IsAdminOnly
from .serializers import CustomUserSerializer, CustomUserDetailSerializer, CategorySerializer, CustomUserCategorySerializer
from .serializers import QuestionSerializer, AnswerSerializer
from .models import CustomUser, Category, Question, Answer

from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

# Create your views here.
class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']

    # def perform_create(self, serializer):
    #     serializer.save()

class CategoryList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class CustomUserCategoryList(generics.ListCreateAPIView):
    queryset = CustomUser.categories.through.objects.all()
    serializer_class = CustomUserCategorySerializer

class CustomUserCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.categories.through.objects.all()
    serializer_class = CustomUserCategorySerializer

class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class CustomUserDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            instance = CustomUser.objects.get(pk=pk)
            self.check_object_permissions(self.request,instance)
            return instance
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserDetailSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = CustomUserDetailSerializer(
            instance=user, data=data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = CustomUserDetailSerializer(instance=user, data=data)

        if serializer.is_valid:
            user.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def send_email(request):  
    if request.method == 'POST':
        # message = request.POST['message']
        # email = request.POST['email']
        # name = request.POST['name']
        send_mail(
        'Welcome Mail From Tech-Diversity.com',
        'Welcome to our website. You are part of our community and you can create profiles of women and non-Binary Folk. You could share this website to show young people that anyone can work in tech.',
        'settings.EMAIL_HOST_USER',
        ['yotevo9234@dogemn.com','balakvign@gmail.com'],#Receivers email address
        fail_silently=False)
    return render(request, 'send_email.html')