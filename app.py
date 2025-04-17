import streamlit as st
from deepface import DeepFace
from PIL import Image

# Page config
st.set_page_config(page_title="Psixologik Holat Tahlili", layout="centered")
st.title("🧠 Yuz orqali Psixologik Holatni Aniqlash")

# File uploader
uploaded_file = st.file_uploader("Surat yuklang:", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Yuklangan surat", use_column_width=True)
    image_path = "temp.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("⏳ Tahlil qilinmoqda...")

    try:
        result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']

        # Map to psychological state
        emotion_map = {
            'happy': "😊 Xotirjam / Quvnoq",
            'sad': "😔 G‘amgin / Ichki tushkunlik",
            'angry': "😠 G‘azablangan / Stress holati",
            'fear': "😨 Xavotirlangan / Tashvishli",
            'disgust': "😣 Norozilik / Salbiy hissiyot",
            'neutral': "😐 Tinch / Barqaror",
            'surprise': "😲 Hayrat / Noaniqlik"
        }

        psychological_state = emotion_map.get(emotion, "Noma'lum")

        st.success(f"🧠 Psixologik holat: **{psychological_state}**  \n(Asosiy emotsiya: `{emotion}`)")

    except Exception as e:
        st.error(f"Xatolik yuz berdi: {str(e)}")
