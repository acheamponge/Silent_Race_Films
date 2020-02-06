import pathlib
import utils.display as udisp
import pandas as pd
import calendar
import streamlit as st
from PIL import Image


def write():
    udisp.title_awesome("Films")
    
    
    keys = {
    './data/films.csv'
            }
    image = Image.open('./img/11.jfif')
    st.image(image, use_column_width=True)
    st.header("Dataset")
    pick = st.selectbox("Select Dataset: ", list(keys))
    
        
    df = pd.read_csv(pick, encoding='utf8')
    st.dataframe(df)
    image = Image.open('./img/12.jpg')
    st.image(image, use_column_width=True)
    
    image = Image.open('./img/9.jpeg')
    st.image(image, use_column_width=True)