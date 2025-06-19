from .serializers import CategorySerializer
from .models import Category
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def category_list(request):
    category = Category.objects.all()
    data = CategorySerializer(category, many=True)
    return Response({
        'data': data.data
    })

@api_view(['POST'])
def category_add(request):
    serialize_data = CategorySerializer(data = request.data)
    if serialize_data.is_valid():
        serialize_data.save()
        return Response(
            data = 'category created',
            status = status.HTTP_201_CREATED,
        )
    return Response(status= status.HTTP_400_BAD_REQUEST)
        
