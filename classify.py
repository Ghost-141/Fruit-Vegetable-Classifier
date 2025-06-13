import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import gradio as gr

# Load your model
model = tf.keras.models.load_model("custom_cnn_model.h5")

# Class Names
class_map = [
    'apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot', 'cauliflower',
    'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic', 'ginger', 'grapes', 'jalepeno', 'kiwi',
    'lemon', 'lettuce', 'mango', 'onion', 'orange', 'paprika', 'pear', 'peas', 'pineapple',
    'pomegranate', 'potato', 'raddish', 'soy beans', 'spinach', 'sweetcorn', 'sweetpotato', 'tomato',
    'turnip', 'watermelon']

def prediction(test_image):
    """Make a prediction using the loaded model and show the result."""
 
    # Load and preprocess the image
    test_img = image.load_img(test_image, target_size=(192, 192)) 
    test_img_array = image.img_to_array(test_img)
    test_img_batch = tf.expand_dims(test_img_array, 0)

    #Make Prediction
    prediction = model.predict(test_img_batch)
    score = tf.nn.softmax(prediction[0])
    predicted_class = class_map[np.argmax(score)]
    confidence = np.max(score)*100
    return f"Predicted Class: {predicted_class}, Confidence: {confidence:.2f}%"

sample_images= ['Apple.jpg','corn.jpg','potato1.jpeg','Tomato.jpg','Banana.jpg']

#Gradio interface
interface = gr.Interface(
    fn=prediction, 
    inputs=gr.Image(type="filepath"),
    outputs="text", 
    allow_flagging="never",
    title="Vegetable & Fruit Classifer",
    examples=sample_images,
    description="Upload image of any vegetable or furit to classify."
)
#interface.launch()
interface.launch(server_name="0.0.0.0")
