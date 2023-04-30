import streamlit as st
from lib.snowflakeDB.add_to_mail_list import insert_email

def render_mail_list():
    with st.form("Join Mailing List"):
        st.write("Join our mailing list!")
        email = st.text_input("Email")
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            # add to db
            insert_email(email)
            st.success('You email has been added! Thanks for the support.')
            