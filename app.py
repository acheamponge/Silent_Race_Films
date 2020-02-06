import streamlit as st

import utils.display as udisp

import src.pages.home
import src.pages.about
import src.pages.films
import src.pages.companies
import src.pages.resources
import src.pages.people
import src.pages.sources    


MENU = {
    "Home" : src.pages.home,
    "Films" : src.pages.films,
    "Companies" : src.pages.companies,
    "People" : src.pages.people,
    "Sources" : src.pages.sources,
    "Resources": src.pages.resources,
    "About" : src.pages.about
}

def main():
    st.sidebar.title("Navigation")
    menu_selection = st.sidebar.radio("Pick an option...", list(MENU.keys()))

    menu = MENU[menu_selection]

    with st.spinner(f"Loading {menu_selection} ..."):
        udisp.render_page(menu)

    st.sidebar.title("Contribute")
    st.sidebar.info(
        "This an open source project and please feel free to contribute"
        +"\n"+
        "[Github](https://github.com/acheamponge/Silent_Race_Films)"
        +"\n"+
        "\n"+
        "[Google Docs](https://docs.google.com/document/d/1kbcVVAPeMC7yXmZHdzHuTVLiXklKUrcpf7z4I8LMueE/edit) "
    )
    
      
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This purpose of this app is analyze the dataset curated by faculty and students at UCLA on Early African American Films."""
    )
    


if __name__ == "__main__":
    main()