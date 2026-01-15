import streamlit as st
import pandas as pd
from urllib.parse import quote_plus
from sqlalchemy import create_engine

# ⚠️ PHẢI đặt ở đầu file
st.set_page_config(layout="wide")

username = "minhnn"
password = quote_plus("gs^FR@&x3ubDoYZUU9`9V%po")
host = "42.1.65.59"
port = 9030
database = "bss"

@st.cache_resource
def get_engine():
    return create_engine(
        f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}",
        pool_pre_ping=True
    )

@st.cache_data(ttl=600)
def load_data():
    engine = get_engine()
    query = """
        SELECT *
        FROM cdr.galaxy_in_icc_export
        LIMIT 10
    """
    return pd.read_sql(query, engine)

st.title("CDR Data Table")

with st.spinner("Loading data..."):
    df = load_data()

st.dataframe(df, use_container_width=True)
