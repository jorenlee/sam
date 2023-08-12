from django.urls import path
from .views import RetrieveProductView

urlpatterns = [
 path('retrieve-products', RetrieveProductView.as_view()),
]