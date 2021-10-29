from django.urls import path
from .views import *

urlpatterns = [
  path('signup/', SignupManagerView.as_view(), name='signup'),
  path('register_employee', RegisterEmployeeView.as_view(), name='register_employee'),
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('users_list/', UsersList.as_view(template_name='users_list.html'), name='users_list'),
  path('delete/<int:pk>/', DeleteUser.as_view(template_name='delete_user.html'), name='delete_user')
]