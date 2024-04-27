import numpy as np
import tensorflow as tf

class VectorAi:
    def __init__(self):
        self.model = tf.keras.applications.EfficientNetB0(include_top=False, pooling="avg")

    def image_to_vec(self, image):
        tf_image = tf.image.decode_jpeg(image, channels=3)
        resize_image = tf.image.resize(tf_image, [224, 224])
        vec = self.model.predict(np.array([resize_image.numpy()]))[0]
        return vec
    
    def vec_from_list(self, vec_list):
        return np.array(vec_list)
    
    def cos_sim(self, v1, v2):
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))