from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .kv_engine import KVEngine

engine = KVEngine()

@api_view(['POST'])
def set_value(request):
    key = request.data.get('key')
    value = request.data.get('value')
    if key is None or value is None:
        return Response({'error': 'key and value required'}, status=status.HTTP_400_BAD_REQUEST)
    engine.set(key, value)
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_value(request):
    key = request.data.get('key')
    if key is None:
        return Response({'error': 'key required'}, status=status.HTTP_400_BAD_REQUEST)
    value = engine.get(key)
    if value is None:
        return Response({'message': 'Key not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'value': value}, status=status.HTTP_200_OK)

@api_view(['POST'])
def delete_value(request):
    key = request.data.get('key')
    if key is None:
        return Response({'error': 'key required'}, status=status.HTTP_400_BAD_REQUEST)
    success = engine.delete(key)
    if success:
        return Response({'message': 'Deleted'}, status=status.HTTP_200_OK)
    return Response({'message': 'Key not found'}, status=status.HTTP_404_NOT_FOUND)