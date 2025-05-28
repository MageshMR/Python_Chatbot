from django.urls import path
from . import views
    
urlpatterns = [
    path('', views.chat_page),       # for chatbot UI
    path('chat/', views.chat_view, name='chatbot'),
]