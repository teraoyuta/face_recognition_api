from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.services.face_service import FaceService
import logging
    
logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_shuffle_key(request):
    face_service = FaceService()

    user_id = request.GET.get('user_id')
    blok_size = face_service.get_blok_size(user_id)
    logger.info(blok_size)
    return Response({'block_width': blok_size['block_width'], 'block_height': blok_size['block_height']})

@api_view(['POST'])
def register_user_face(request):
    face_service = FaceService()

    user_name = request.POST.get('user_name')
    block_width = request.POST.get('block_width')
    block_height = request.POST.get('block_height')
    face_image = request.FILES['face_image'].read()

    face_service.register_face(user_name, block_width, block_height, face_image)
    return Response({'message': 'register success'})

@api_view(['GET'])
def check_user_face(request):
    face_service = FaceService()

    user_id = request.GET.get('user_id')
    face_image = request.FILES['face_image'].read()

    similarity = face_service.get_cos_similarity(user_id, face_image)
    return Response({'similarity': round(similarity, 2)})
