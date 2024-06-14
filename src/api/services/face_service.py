import pickle
from api.models import Face
from libraries.image_vector import VectorAi
import logging

logger = logging.getLogger(__name__)

class FaceService:
    def __init__(self):
        self.vector_ai_model = VectorAi()

    def register_face(self, user_name, block_width, block_height, image):
        vec_tensor = self.vector_ai_model.image_to_vec(image.read())
        dec_binary = pickle.dumps(vec_tensor)
        Face.objects.create(user_name=user_name, block_width=block_width, block_height=block_height, vector=dec_binary)
        return 0
    
    def get_blok_size(self, user_id):
        user_face = Face.objects.values('block_width', 'block_height').get(id=user_id)
        return user_face
    
    def get_user_name(self, image):
        input_image_vec = self.vector_ai_model.image_to_vec(image.read())
        user_face = Face.objects.all()
        slogan_vecs_dict = self.vector_ai_model.get_vec_dict(user_face)
        similarities = self.vector_ai_model.cos_sim(input_image_vec, slogan_vecs_dict[self.vector_ai_model.VECS_KEY])
        
        json_data = []
        for slogan, distance in zip(slogan_vecs_dict[self.vector_ai_model.SENTENCES_KEY], similarities):
            logging.info(distance)
            
            entry = {
                "user_name": slogan,
                "distance": round(distance, 2),
            }
            json_data.append(entry)
        max_entry = max(json_data, key=lambda x: x['distance'])
        return max_entry["user_name"]
