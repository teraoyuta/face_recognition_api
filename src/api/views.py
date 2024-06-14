from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.services.face_service import FaceService
from rest_framework import status
import logging

    
logger = logging.getLogger(__name__)

@api_view(['POST'])
def register_user_face(request):
    face_service = FaceService()
    block_width = 0# request.POST.get('block_width')
    block_height = 0# request.POST.get('block_height')
    face_image = request.FILES['face_image']
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    user_name = last_name + " " + first_name
    
    face_service.register_face(user_name, block_width, block_height, face_image)
    return Response({'message': 'register success'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_shuffle_key(request):
    face_service = FaceService()

    user_id = request.GET.get('user_id')
    blok_size = face_service.get_blok_size(user_id)
    logger.info(blok_size)
    return Response({'block_width': blok_size['block_width'], 'block_height': blok_size['block_height']})

@api_view(['POST'])
def check_user_face(request):
    face_service = FaceService()
    face_image = request.FILES['face_image']
    user_name = face_service.get_user_name(face_image)
    return Response({'user_name': user_name})
