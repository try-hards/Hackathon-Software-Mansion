from django.urls import path
from .views import SignupView, LoginView, LogoutView, CheckAuthenticatedView, DeleteAccountView, SetPhotoAccountView, GetCSRFToken

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('authenticated', CheckAuthenticatedView.as_view()),
    path('register', SignupView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('delete', DeleteAccountView.as_view()),
    path('set-photo', SetPhotoAccountView.as_view()),
    path('csrf_cookie', GetCSRFToken.as_view()),

]