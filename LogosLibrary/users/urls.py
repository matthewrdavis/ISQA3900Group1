from django.urls import path
from .import views
from .views import SignUpView

app_name = 'users'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('account/<int:pk>', views.customUser_view, name='account'),
    path('account/<int:pk>/edit/', views.account_edit, name='account_edit'),
]
