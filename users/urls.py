from django.urls import path
from .views import RegisterView, UserListView, InterestListView, MessageListView,LoginView, LogoutView

################

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('interests/', InterestListView.as_view(), name='interest-list'),
    path('messages/', MessageListView.as_view(), name='message-list'),

]