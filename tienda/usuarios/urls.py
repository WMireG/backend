from django.urls import path
from usuarios.views import CustomLoginView, RegistrationView, LogoutConfirmationView, Home


urlpatterns = [
    path('', Home.as_view(), name="usuarios"), 
    path("login/", CustomLoginView.as_view(), name="login"),
    path("registro/", RegistrationView.as_view(), name="registro"),
    path("confirm_logout/", LogoutConfirmationView.as_view(), name="confirm_logout"),
]
