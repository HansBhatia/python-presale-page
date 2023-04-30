from snowflake.snowpark import Session
import streamlit as st

# Establish Snowflake session
@st.cache_resource
def create_session():
    return Session.builder.configs(st.secrets.snowflake).create()