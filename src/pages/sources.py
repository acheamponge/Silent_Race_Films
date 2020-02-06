import pathlib
import utils.display as udisp
from PIL import Image
import streamlit as st
import pandas as pd

def write():
    udisp.title_awesome("Films")
    
    
    keys = {
    './data/sources.csv'
            }
    st.header("Dataset")
    pick = st.selectbox("Select Dataset: ", list(keys))
    
        
    df = pd.read_csv(pick, encoding='utf8')
    st.dataframe(df)
    