from .serializers import CategorySerializer, TodoSerializer
from .models import Category, Todo
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status as http_status
 
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
        status=http_status.HTTP_201_CREATED)
    except Exception as e:
        return Response({
            'message': str(e)
        }, status=http_status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST', 'GET',])
def todo(request):
    
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
        status = request.query_params.get('status')
        category_id = request.query_params.get('category')
        if (status != None and category_id != None):
            status = str(status).capitalize()
            id = int(category_id)
            results =  Todo.objects.filter(status=status, category__id=id)
            serialize_result =  TodoSerializer(results, many = True)
            return Response(
                {
                    'result' : serialize_result.data,
                    'status' : 'success' 
                },
                status= http_status.HTTP_200_OK
            )
        elif status != None:
            status = str(status).capitalize()
            results =  Todo.objects.filter(status=status)
            serialize_result =  TodoSerializer(results, many = True)
            return Response(
                    {
                        'result' : serialize_result.data,
                        'status' : 'success' 
                    },
                    status= http_status.HTTP_200_OK
                )
        elif category_id != None:
            category_id = int(category_id)
            results =  Todo.objects.filter(category__id=category_id)
            serialize_result =  TodoSerializer(results, many = True)
            return Response(
                    {
                        'result' : serialize_result.data,
                        'status' : 'success' 
                    },
                    status= http_status.HTTP_200_OK
                )
             
    data = Todo.objects.all()
    serialize_data = TodoSerializer(data, many=True)
    return Response({'data': serialize_data.data})  


@api_view(['PUT'])
def todo_update(request, pk):
    try:
        task = Todo.objects.get(id=pk)
        task.status = Todo.StatusTypes.COMPLETED
        task.save()
        return Response({'message': 'success'}, status=http_status.HTTP_200_OK)
    except task.DoesNotExist:
        return Response(
                {'message': 'Todo not found'},
            status=http_status.HTTP_404_NOT_FOUND,
        )
    except Exception as e:
        return Response({'message': str(e)}, status=http_status.HTTP_500_INTERNAL_SERVER_ERROR)
            
