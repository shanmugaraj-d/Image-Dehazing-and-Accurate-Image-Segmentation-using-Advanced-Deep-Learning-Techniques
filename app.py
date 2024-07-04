import image_dehazer
import cv2
import os
import streamlit as st
from PIL import Image




def dehaze_image(input_path,input_format):
    HazeImg = cv2.imread(input_path)					
    HazeCorrectedImg, haze_map = image_dehazer.remove_haze(HazeImg, showHazeTransmissionMap=False)
    cv2.imwrite('output_img.'+input_format.lower(), HazeCorrectedImg)
    img = Image.open('output_img.'+input_format.lower())
    return img,'output_img.'+input_format.lower()


def load_image(image_file):
    img = Image.open(image_file)
    format = img.format
    img.save(f"input_img.{format.lower()}")
    return img,f"input_img.{format.lower()}",format

st.title('Image Dehazion')
st.text('Remove Haze from Image')
img = st.file_uploader("Upload the Image here")
if st.button(label="Show"):
    col1, col2, col3 = st.columns(3)
    input_img,img_path,format = load_image(img)
    
    output_img,output_img_path = dehaze_image(img_path,format)
    
    
    
    with col1:
        st.image(input_img,caption='Input Image')
    with col2:
        st.image(output_img,caption='Output Image')