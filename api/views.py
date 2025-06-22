from .serializers import CategorySerializer, TodoSerializer
from .models import Category, Todo
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
    
    try:
        serialize_data.is_valid()
        serialize_data.save()
        return Response ({
            'message': 'Category created',
        },
        status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({
            'message': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST', 'GET'])
def todo_add(request):
    
    if (request.method == 'POST'):
        serialize_data = TodoSerializer(data = request.data)
        try:
            serialize_data.is_valid()
            serialize_data.save()
            return Response ({
                'message': 'Todo created',
                'data': serialize_data.data
            },
        status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
    elif (request.method == 'GET'):
        data = Todo.objects.all()
        serialize_data = TodoSerializer(data, many=True)
        return Response({
            'data': serialize_data.data
        })
        
    

            
