
# import os
# import numpy
# import tensorflow as tf
# from tensorflow import keras

# saved_model_path = "AI\Model\Translator"

# class Translator:
    
#     def __init__(self):
#         load_options = tf.saved_model.LoadOptions(experimental_io_device='/job:localhost')
#         self.model = tf.saved_model.load(saved_model_path,options=load_options)
       
#     def translate(self,source):
#         result = self.model.translate([source])
#         target = result[0].numpy().decode()
#         print(f"source: {source}, target: {target}")
        
#         return target
        
