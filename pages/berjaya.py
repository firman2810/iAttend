import streamlit as st
from utils import load_image, gap

st.set_page_config(page_title="Berjaya", page_icon="🟢", layout="centered")

# Title
st.title("PENGESAHAN BERJAYA ✅")

# Load image correctly
img = load_image("good.jpg")
if img:
    st.image(img, width=300)

# Retrieve stored session data
staff_id = st.session_state.get("staff_id", None)
staff_name = st.session_state.get("staff_name", None)
timestamp = st.session_state.get("timestamp", None)

if staff_id and timestamp:
    st.success(
        f"Nama: {staff_name if staff_name else '-'}  \n"
        f"Staff ID: {staff_id}  \n"
        f"Masa Check-in: {timestamp}  \n\n"
        "Sila laporkan diri di kaunter pendaftaran bersama **screenshot** laman web ini. "
        "Terima kasih."
    )

gap(1)

# Centered button for homepage
col1, col2, col3 = st.columns([3, 2, 3])
with col2:
    if st.button("Homepage"):
        st.switch_page("pages/homepage.py")
