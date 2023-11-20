# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 19:55:13 2023

@author: USER
"""

import streamlit as st
from PIL import Image
import numpy as np

def app():
    st.title("Eye Disease Classification")

    st.markdown(
        """
        <p style="text-align:justify;">
        Eye disease is one type of disease that is dangerous and becomes one of the frightening diseases because it threatens the human visual sense. Types of eye diseases that can occur in humans include cataracts, diabetic rethinopaty and glaucoma. Cataract is a type of eye disease that can trigger blindness and can affect parents with a prevalence of 40 years and over approximately 11.8% to 18.8%. Diabetic rethinopathy is a type of eye disease caused by high blood sugar content that can damage blood vessels in the retina of the eye. Meanwhile, Glaucoma is a condition where there is a loss of retinal ganglion cells and thinning of the retinal nerve fiber layer, which can also cause loss of vision. Therefore, we must be able to always maintain the health of our eyes with a good lifestyle, so that they can stay healthy and can move well.
        """,
        unsafe_allow_html=True
    )
    
    
    img =Image.open('img.png')
    st.image(img)
    
    st.markdown(
        """
        <p style="text-align:justify;">
        The dataset used for building model is an eye disease image dataset which has a total of 4217 image data and has 4 classes, namely cataract, diabetic rethinopaty, glaucoma and normal. With data distribution in each class, namely 1038 cataract images, 1098 diabetic rethinopathy images, 1007 glaucoma images and 1074 normal images
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <p style="text-align:justify;">
        The classification process will use the Transfer Learning CNN method, namely the Efficient Net architecture. The purpose of using Efficient Net is because this architecture conducts training with relatively few parameters compared to other architectures, but still has good classification performance 
        """,
        unsafe_allow_html=True
    )
    
    st.title("Model Classificaation Layer")
    img4 = Image.open('EfficientNet.png')
    st.image(img4)
    
    