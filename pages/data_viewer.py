import streamlit as st
import psycopg2
import pandas as pd
from db import get_connection

st.set_page_config(page_title="Data Viewer", page_icon="📊", layout="wide")

st.header("Data Viewer")

# --- Connect to DB ---
conn = get_connection()
cur = conn.cursor()

# --- Fetch data ---
cur.execute("SELECT * FROM union_member;")
data = cur.fetchall()
columns = [desc[0] for desc in cur.description]

# --- Convert to DataFrame ---
df = pd.DataFrame(data, columns=columns)

# --- Show all data ---
st.write("### Union Members Data")
st.dataframe(df)

# --- Staff Selector ---
staff_id_selector = st.selectbox("Select Staff", options=df['staff_id'].to_list())

# Get the selected row
staff_row = df[df['staff_id'] == staff_id_selector].iloc[0]

# --- Display selected staff  ---
st.markdown(
    f"""
    <div style="
        padding:20px; 
        border-radius:15px; 
        background-color:#4a4a4a;  /* Grey background */
        box-shadow: 0 4px 8px rgba(0,0,0,0.2); 
        margin-bottom:20px;
        font-family: Arial, sans-serif;
        color: white;  /* White text */
    ">
        <h3 style="margin-bottom:10px; color:white;">
            {staff_row['employee_name']}
        </h3>
        <p><strong>Staff ID:</strong> {staff_row['staff_id']}</p>
        <p><strong>Company:</strong> {staff_row['company_name']}</p>
        <p><strong>Unit:</strong> {staff_row['organizational_unit']}</p>
    </div>
    """,
    unsafe_allow_html=True
)