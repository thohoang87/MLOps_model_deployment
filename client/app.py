import streamlit as st
import json
import requests


st.title("Iris Dataset Prediction")

sepal_length = st.slider("sepal_length",min_value = 0.0,max_value=8.0)
st.write(sepal_length)

sepal_width = st.slider("sepal_width",min_value = 0.0,max_value=8.0)
st.write(sepal_width)

petal_length = st.slider("petal_length",min_value = 0.0,max_value=8.0)
st.write(petal_length)

petal_width = st.slider("petal_width",min_value = 0.0,max_value=8.0)
st.write(petal_width)

inputs = {
            "sepal_length":sepal_length,
            "sepal_width":sepal_width,
            "petal_length":petal_length,
            "petal_width":petal_width
        }
    

if st.button("Result") : 
    res= requests.post(url = "http://host.docker.internal:8000/iris_prediction", data = json.dumps(inputs))
    if res:
        st.write("Result : ", res.json())
    else:
        st.write("Try again")
        