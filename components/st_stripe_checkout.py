import streamlit as st
from lib.stripeCheckout.create_intent import create_checkout

def render_stripe_checkout(quantity: int):
    checkout_session = create_checkout(quantity);
    if not checkout_session:
        e = RuntimeError('Issue creating payment')
        st.exception(e)
    else:
        st.markdown(f'''[Click here to buy now]({checkout_session.url})''')