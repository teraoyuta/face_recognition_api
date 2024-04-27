from django.urls import path
from api import views

urlpatterns = [
    # path('hello/', SloganAPIView.as_view(), name='helloworld'),
    path('get_shuffle_key/', views.get_shuffle_key, name='get_shuffle_key'),
    path('register_user_face/', views.register_user_face, name='register_user_face'),
    path('check_user_face/', views.check_user_face, name='check_user_face')
]
