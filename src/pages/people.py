import pathlib
import utils.display as udisp
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from wordcloud import WordCloud
from collections import Counter
from PIL import Image


def write():
    udisp.title_awesome("Films")
    
    
    ky = {
    './data/people.csv'
            }
    st.header("Dataset")
    image = Image.open('./img/7.jpg')
    st.image(image, use_column_width=True)
    pick = st.selectbox("Select Dataset: ", list(ky))
    
        
    df = pd.read_csv(pick, encoding='utf8')
    st.dataframe(df)
 
    