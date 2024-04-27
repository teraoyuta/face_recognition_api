from api.models import Face
from libraries.image_vector import VectorAi
import logging

logger = logging.getLogger(__name__)

class FaceService:
    def __init__(self):
        self.vector_ai_model = VectorAi()

    def register_face(self, user_name, block_width, block_height, image):
        vec_tensor = self.vector_ai_model.image_to_vec(image)
        vec_string = ''
        vec_last_index = len(vec_tensor) - 1
        for i in range(len(vec_tensor)):
            vec_string += str(vec_tensor[i])
            if i != vec_last_index:
                vec_string += ','
        Face.objects.create(user_name=user_name, block_width=block_width, block_height=block_height, vector=vec_string)
        return 0
    
    def get_blok_size(self, user_id):
        user_face = Face.objects.values('block_width', 'block_height').get(id=user_id)
        return user_face
    
    def get_cos_similarity(self, user_id, image):
        input_image_vec = self.vector_ai_model.image_to_vec(image)
        user_face = Face.objects.get(id=user_id)
        user_face_vector_list = [float(value) for value in user_face.vector.split(',')]
        user_face_vector = self.vector_ai_model.vec_from_list(user_face_vector_list)

        similarity = self.vector_ai_model.cos_sim(input_image_vec, user_face_vector)
        return similarity
