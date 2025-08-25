import streamlit as st 
from PIL import Image 
from utils import load_image, gap

st.set_page_config(page_title="iAttend", page_icon="🌐", layout="centered")

# Load image correctly
img = load_image("kppit.png")
if img:
    st.image(img, use_container_width=True)

gap(2)

# Main title
st.header("Majlis Mesyuarat Agung KPPIT 2025")

gap(2)

# Staff ID input
x = st.text_input("Sila masukkan staff ID anda untuk membuat pengesahan: ")
st.caption("Nota penting: \n - Majlis ini hanya terbuka kepada ahli berdaftar sahaja \n "
"- Pastikan staff ID yang dimasukkan adalah betul dan lengkap\n "
"- Staff ID hanya mengandungi nombor sahaja \n - Contoh: 12345678")

gap(1)

# Database mimic
valid_staff = {
    "12345678": "Muhammad Firman Syah",
    "87654321": "Nurzainina Husna",
    "01234567": "Sharul Ariffin"
}

# Center the Check-in button
col1, col2, col3 = st.columns([3, 2, 3])  
with col2:
    if st.button("CEK", use_container_width=True):

        # If empty input
        if x.strip() == "":
            st.session_state["error_msg"] = "Sila masukkan staff ID anda."
            st.switch_page("pages/gagal.py")

        # If contains non-digit characters
        elif not x.isdigit():  
            st.session_state["error_msg"] = "Staff ID hanya boleh mengandungi nombor."
            st.switch_page("pages/gagal.py")

        # If ID is not in the list
        elif x not in valid_staff:
            st.session_state["error_msg"] = "Maaf, nama anda tidak tersenarai sebagai ahli berdaftar."
            st.switch_page("pages/gagal.py")
            
        else:
            # Save staff ID and name into session_state
            st.session_state["staff_id"] = x
            st.session_state["staff_name"] = valid_staff[x]

            # Go to pengesahan page
            st.switch_page("pages/pengesahan.py")
