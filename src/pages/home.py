import pathlib
import utils.display as udisp
from PIL import Image
import streamlit as st


def write():
    udisp.title_awesome("Early African American Movies")
    image = Image.open('./img/1.jpg')

    st.image(image, use_column_width=True)
    
    st.write(
            """
The Early African American Movies project is data analytics and visualization project that seeks to bring more insights into Silent Race Films.

This project uses data from the "EARLY AFRICAN AMERICAN FILM - Reconstructing the History of Silent Race Films, 1909-1930" project from student and faculty as UCLA.

This project provides analytics and visualization of the data on:
- **The Films**   
- **The Companies**. 
- **The People**.s
    """
        )
    st.write(
        f'<iframe width="560" height="315" src="https://www.youtube.com/embed/uCVrFj7fclg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        unsafe_allow_html=True,
    )
