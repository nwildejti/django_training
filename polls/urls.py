from django.urls import path

from .import views 

urlpatterns = [
    path('Question', views.QuestionView.as_view(), name="index")
]