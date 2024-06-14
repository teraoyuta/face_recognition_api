import pickle
import numpy as np
import tensorflow as tf

class VectorAi:
    def __init__(self):
        self.model = tf.keras.applications.EfficientNetB0(include_top=False, pooling="avg")
        self.VECS_KEY = "vecs"
        self.SENTENCES_KEY = "users"

    def image_to_vec(self, image):
        tf_image = tf.image.decode_jpeg(image, channels=3)
        resize_image = tf.image.resize(tf_image, [224, 224])
        vec = self.model.predict(np.array([resize_image.numpy()]))[0]
        return vec
    
    def vec_from_list(self, vec_list):
        return np.array(vec_list)
    
    def get_vec_dict(self, user_faces):
        tensor_list = []
        user_list = []
        for face in user_faces:
            serialized_tensor = face.vector
            tensor = pickle.loads(serialized_tensor).squeeze()
            tensor_list.append(tensor)
            user_list.append(face.user_name)
        tensors = tf.stack(tensor_list)
        return {self.VECS_KEY: tensors, self.SENTENCES_KEY: user_list}
    
    def cos_sim(self, v1, v2):
        dot_products = np.dot(v2, v1)
        norms_v1 = np.linalg.norm(v1)
        norms_v2 = np.linalg.norm(v2, axis=1)
        cos_similarities = dot_products / (norms_v1 * norms_v2)
        return cos_similarities
