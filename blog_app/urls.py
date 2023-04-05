from django.urls import path
from .views import BlogList, CommentList, CommentDetail, UserRegistrationView, BlogDetail

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='registration'),
    path('blogs/', BlogList.as_view(), name='blogs'),
    path('blogs/<int:pk>/', BlogDetail.as_view(), name='blogs_id'),
    path('comments/', CommentList.as_view(), name='comments'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comments_id')

    ]
