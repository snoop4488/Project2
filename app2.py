import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image


st.title("Reconocimiento óptico de Caracteres")

uploaded_image = st.file_uploader("Cargar una imagen", type=["jpg", "png", "jpeg"])

# Agregar la opción para tomar una foto con la cámara
img_file_buffer = st.camera_input("Tomar una foto")

with st.sidebar:
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))

if uploaded_image is not None:
    # Si se cargó una imagen desde el sistema, la leemos y la procesamos
    pil_image = Image.open(uploaded_image)
    cv2_img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
elif img_file_buffer is not None:
    # Si se tomó una foto con la cámara, la procesamos
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
else:
    st.write("Cargue una imagen o tome una foto para continuar")

if uploaded_image is not None or img_file_buffer is not None:
    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)
    else:
        cv2_img = cv2_img

    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img_rgb)
    st.write(text)


    

