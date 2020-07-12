from django.urls import path
from .views import InquiryCreateView,InquiryCreateViewAuth, InquiryDetailView, GetInquiriesView
from .views import UserCreate, LoginView


urlpatterns = [
    path('inquiry/create-auth/', InquiryCreateViewAuth.as_view()),
    path('inquiry/create/', InquiryCreateView.as_view()),
    path('inquiry/detail/<int:pk>/', InquiryDetailView.as_view()),
    path('inquiry/all/', GetInquiriesView.as_view()),


    path('user/create/', UserCreate.as_view(), name="user_create"),
    path('login/', LoginView.as_view(), name="login"),

]