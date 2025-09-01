import streamlit as st
from utils import load_image, gap

st.set_page_config(page_title="Berjaya", page_icon="🟢", layout="centered")

# Title
st.title("PENGESAHAN BERJAYA ✅")

# Load image
img = load_image("good.jpg")
if img:
    st.image(img, width=300)

# Retrieve session data
staff_id = st.session_state.get("staff_id")
staff_name = st.session_state.get("staff_name")
company_name = st.session_state.get("company_name")
organizational_unit = st.session_state.get("organizational_unit")
timestamp = st.session_state.get("timestamp")

# Display inside st.success
if staff_id and timestamp:
    st.success(
        f"Nama: {staff_name if staff_name else '-'}  \n"
        f"Staff ID: {staff_id}  \n"
        f"Company: {company_name if company_name else '-'}  \n"
        f"Unit: {organizational_unit if organizational_unit else '-'}  \n"
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
