# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 19:56:57 2023

@author: USER
"""

import streamlit as st

from Tabs import home, predict

Tabs = {
        "Home" : home,
        "Prediction" : predict
        }

#sidebar
st.sidebar.title("Navigation")

#option
page = st.sidebar.radio("Pages", list(Tabs.keys()))

#call function
# if page in ["Prediction", "Visualisation"]:
#     Tabs[page].app(data,x,y)
# else:
#     Tabs[page].app()

Tabs[page].app()