import streamlit as st

# Define pages
homepage_page = st.Page("pages/homepage.py", title="Home", icon=":material/home:")
pengesahan_page = st.Page("pages/pengesahan.py", title="Pengesahan", icon=":material/person_check:")
data_viewer_page = st.Page("pages/data_viewer.py", title="Data Viewer", icon=":material/data_table:")

# Navigation controller
pg = st.navigation([homepage_page, pengesahan_page, data_viewer_page])
pg.run()
