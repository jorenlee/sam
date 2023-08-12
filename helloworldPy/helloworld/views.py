from rest_framework.views import APIView
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework import status

# Create your views here.
class RetrieveProductView(APIView):
  def get(self, request, format=None):
    try:
      if Product.objects.all().exists():
        product = Product.objects.all()
        product = ProductSerializer(product, many=True)

        return Response({'product': product.data}, status=status.HTTP_200_OK)
      else:
        return Response({'error': 'No images found'},
          status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response({'error': 'Something went wrong when retrieving images'},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)