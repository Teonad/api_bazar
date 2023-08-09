from django.urls import path
from users.views import RegistrUserView

app_name = 'urls'


urlpatterns = [
    path('registr/', RegistrUserView.as_view(), name='registr')
]
