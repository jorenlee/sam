from django.urls import path
from .views import RetrieveFruitView

urlpatterns = [
 path('retrieve-fruit', RetrieveFruitView.as_view()),
]