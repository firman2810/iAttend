import streamlit as st
from utils import load_image, gap

st.set_page_config(page_title="Gagal", page_icon="🔴", layout="centered")

st.title("PENGESAHAN GAGAL ❌")

# Load image correctly
img = load_image("fakyu.jpg")
if img:
    st.image(img, width=300)

# Display the correct error message
if "error_msg" in st.session_state:
    st.error(st.session_state["error_msg"])

gap(1)

col1, col2, col3 = st.columns([3, 2, 3])  
with col2:
    if st.button("Homepage"):
        st.switch_page("pages/homepage.py")