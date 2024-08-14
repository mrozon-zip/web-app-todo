import streamlit as st
from PIL import Image
import random as rd

complements = [
    'Gorgeous',
    'Splendid',
    'Radiant',
    'Stunning',
    'Exquisite',
    'Elegant',
    'Charming',
    'Dazzling',
    'Brilliant',
    'Magnificent',
    'Lovely',
    'Graceful',
    'Marvelous',
    'Breathtaking',
    'Impressive',
    'Delightful',
    'Enchanting',
    'Striking',
    'Alluring',
    'Fabulous'
]

st.title('PhotoBooth')
st.subheader("Lets have some fun...smile!")

with st.expander("Start camera when you're ready and take a photo"):
    camera_image = st.camera_input('camera')

if camera_image:

    st.write(rd.choice(complements) + '! Here is your photo, I tuned it up a bit')
    # create pillow image instance
    img = Image.open(camera_image)

    # convert pillow image instance to grayscal
    gray_img = img.convert("L")

    # display grayscale image on a webpage
    st.image(gray_img)