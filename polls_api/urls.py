from django.urls import path, include
from rest_framework.routers import DefaultRouter
from polls_api import views

router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'choices', views.ChoiceViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]