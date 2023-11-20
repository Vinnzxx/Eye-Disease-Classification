# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 19:55:54 2023

@author: USER
"""

import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import cv2
from tensorflow.keras.applications.efficientnet import preprocess_input

def app():
    st.title("Eye Disease Classification Process")
    # Use columns to organize the layout
    col1, col2, col3, col4 = st.columns(4)

    # Load and display images in separate columns
    with col1:
        img1 = Image.open('Cataract.jpg')
        st.image(img1, caption='Cataract', use_column_width=True)

    with col2:
        img2 = Image.open('Diabbetic_Retinopathy.jpeg')
        st.image(img2, caption='Diabetic Retinopathy', use_column_width=True)

    with col3:
        img3 = Image.open('Glaucoma.jpg')
        st.image(img3, caption='Glaucoma', use_column_width=True)
        
    with col4:
        img4 = Image.open('Normal.jpg')
        st.image(img4, caption='Normal', use_column_width=True)
        
    model = load_model("EfficientNet_EyeDisease.h5")
    
    # File uploader for user input
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
    
        # Preprocess the image for prediction
        img_size = 224  # Adjust the image size based on DenseNet's input requirements
        img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img = cv2.resize(img, (img_size, img_size))
        img = img.astype(np.float32) / 255.0
        img = np.expand_dims(img, axis=0)  # Add batch dimension
    
        # Make predictions
        prediction = model.predict(img)
        predicted_class = np.argmax(prediction)
        
        # Display the predicted class
        class_labels = ["Cataract", "Diabetic Retinopathy", "Glaucoma", "Normal"]
        st.success(f"Predicted Class: {class_labels[predicted_class]}")
        