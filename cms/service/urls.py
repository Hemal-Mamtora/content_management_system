from django.urls import path
from .views import (RegisterUserAPIView, loginView, CreateCategory, ContentCreateView, 
                    listContent, AdminListContent, AdminRetrieveContentUpdate, updateContent, 
                    AdminDeleteContent, AuthorDeleteContent, SearchAPIView)
urlpatterns = [
  path('register/',RegisterUserAPIView.as_view()),
  path('login/', loginView),
  path('category/', CreateCategory.as_view()),
  path('content/', ContentCreateView.as_view()),
  path('list-content/',listContent),
  path('admin-list-content/',AdminListContent.as_view()),
  path('admin-update-content/<int:pk>/',AdminRetrieveContentUpdate.as_view()),
  path('update-content/<int:pk>/',updateContent.as_view()),
  path('admin-delete-content/<int:pk>/',AdminDeleteContent.as_view()),
  path('delete-content/<int:pk>/',AuthorDeleteContent.as_view()),
  path('search/',SearchAPIView.as_view()),
]
