import numpy as np
import streamlit as st
import pickle
from PIL import Image,ImageOps
import cv2
import tensorflow

st.markdown("<h1 style='text-align: center;'>PHOTO TO PENCIL SKETCH IMAGE CONVERTER</h1>", unsafe_allow_html=True)

file=st.file_uploader("Please Upload u r Image",type=['jpg','png','jpeg'])



if file is None:
    st.text('Please upload an image file')
else:
    image=Image.open(file)
    size=(400,400)
    img=ImageOps.fit(image,size,Image.ANTIALIAS)
    img_arr=np.array(img)
    gray_img=cv2.cvtColor(img_arr,cv2.COLOR_BGR2GRAY)
    inverted_gray_img=255-gray_img
    blurred_img=cv2.GaussianBlur(inverted_gray_img,(21,21),0)
    inverted_blurred_img=255-blurred_img
    pencil_sketch_img=cv2.divide(gray_img,inverted_blurred_img,scale=256.0)
    original_img,pencil_img=st.columns(2)
    with original_img:
        st.image(img)
    with pencil_img:
        st.image(pencil_sketch_img)
    