import tensorflow as tf

# Load the saved model
saved_model_dir = 'my_cnn_model'

# Convert the model
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()

# Save the TensorFlow Lite model to a file
with open('my_cnn_model.tflite', 'wb') as f:
    f.write(tflite_model)
