from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view()),
    # path('activate/<str:activation_code>/', admin.site.urls),
    # path('login/', admin.site.urls),
    # path('logout/', admin.site.urls),
    # path('change_password/', admin.site.urls),
]