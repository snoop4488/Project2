import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image
from gtts import gTTS
import base64

st.title("Asistente de Lectura")

# Agregar la opción para cargar una imagen desde el sistema
uploaded_image = st.file_uploader("Cargar una imagen", type=["jpg", "png", "jpeg"])

# Agregar la opción para tomar una foto con la cámara
img_file_buffer = st.camera_input("Tomar una foto")

if uploaded_image is not None:
    # Si se cargó una imagen desde el sistema, la leemos y la procesamos
    pil_image = Image.open(uploaded_image)
    cv2_img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
elif img_file_buffer is not None:
    # Si se tomó una foto con la cámara, la procesamos
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
else:
    cv2_img = None

# Variable para almacenar el texto reconocido por OCR
ocr_text = ""

if cv2_img is not None:
    # Si hay una imagen, realizar OCR y almacenar el texto
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    ocr_text = pytesseract.image_to_string(img_rgb)

# Widget para ingresar el texto a convertir en voz
text = st.text_input("Texto", ocr_text)

# Botón para convertir el texto en voz y reproducirlo
if st.button("Decirlo"):
    if text:
        # Utilizar gTTS para convertir el texto en voz
        tts = gTTS(text, lang='es')
        audio_data = tts.get_audio_data()

        # Reproducir el audio
        st.audio(audio_data, format='audio/wav')
        except Exception as e:
    st.error(f"Error al generar el audio: {str(e)}")

# Mostrar el botón de Texto a Voz
