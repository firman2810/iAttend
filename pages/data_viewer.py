import streamlit as st
import psycopg2
import pandas as pd
from db import get_connection

st.set_page_config(page_title="Data Viewer", page_icon="📊", layout="wide")

st.header("Data Viewer")

conn = get_connection()
cur = conn.cursor()

# Fetch data from the database
cur.execute("SELECT * FROM union_member;")
data = cur.fetchall()
columns = [desc[0] for desc in cur.description]
st.write("### Union Members Data")

df = pd.DataFrame(data, columns=columns)
st.dataframe(df)

staff_id_selector = st.selectbox("Select Action", options=df['staff_id'].to_list())