import streamlit as st

# Define pages
homepage_page = st.Page("pages/homepage.py", title="Homepage", icon="🏠")
pengesahan_page = st.Page("pages/pengesahan.py", title="Pengesahan", icon="📄")
berjaya_page = st.Page("pages/berjaya.py", title="Berjaya", icon="🟢")
gagal_page = st.Page("pages/gagal.py", title="Gagal", icon="🔴")
data_viewer_page = st.Page("pages/data_viewer.py", title="Data Viewer", icon="📊")

# Navigation controller
pg = st.navigation([homepage_page, pengesahan_page, berjaya_page, gagal_page, data_viewer_page])
pg.run()
