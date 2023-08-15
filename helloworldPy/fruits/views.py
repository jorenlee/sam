from rest_framework.views import APIView
from .models import Fruit
from rest_framework.response import Response
from .serializers import FruitSerializer
from rest_framework import status

# Create your views here.
class RetrieveFruitView(APIView):
  def get(self, request, format=None):
    try:
      if Fruit.objects.all().exists():
        fruit = Fruit.objects.all()
        fruit = FruitSerializer(fruit, many=True)

        return Response({'fruit': fruit.data}, status=status.HTTP_200_OK)
      else:
        return Response({'error': 'No images found'},
          status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response({'error': 'Something went wrong when retrieving images'},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)