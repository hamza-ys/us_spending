import streamlit as st

from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine

# Connect to Neon


DATABASE_URL = st.secrets["key"] 
engine = create_engine(DATABASE_URL)

@st.cache_data
def load_data():
    return pd.read_sql("SELECT * FROM your_table", engine)

df = load_data()
st.dataframe(df)



