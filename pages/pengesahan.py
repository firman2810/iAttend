import streamlit as st
from datetime import datetime
from utils import gap

st.set_page_config(page_title="Pengesahan", page_icon="📄", layout="centered")

# Retrieve data from session_state
staff_id = st.session_state.get("staff_id", None)
staff_name = st.session_state.get("staff_name", None)
timestamp = st.session_state.get("timestamp", None)

st.header("Pengesahan Kehadiran")

gap(2)

# Display staff info (disabled so cannot edit)
st.text_input("Staff ID", staff_id, disabled=True)
st.text_input("Nama", staff_name, disabled=True)

gap(1)

# Centered button
col1, col2, col3 = st.columns([3, 2, 3])
with col2:
    if st.button("CHECK-IN", use_container_width=True):
        # Save current timestamp
        st.session_state["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Navigate to success page
        st.switch_page("pages/berjaya.py")
