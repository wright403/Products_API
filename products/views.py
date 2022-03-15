from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

@api_view(['GET', 'POST'])
def products_list(request):

    if request.method == 'GET':
      products = Product.objects.all()
      serializer = ProductSerializer(products, many=True)
      return Response(serializer.data)
    elif request.method == 'POST':
          serializer = ProductSerializer(data=rf)