import streamlit as st
import stripe

stripe.api_key = st.secrets["stripe"]["api_key"]

def create_checkout(quantity: int):
    try: 
        return stripe.checkout.Session.create(
                    line_items=[
                        {
                            # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                            'price': 'price_1N2NIAAsQNyIwCoLnfdIQsD5',
                            'quantity': quantity,
                        },
                    ],
                    mode='payment',
                    success_url='http://localhost:8501/',
                    cancel_url='http://localhost:8501/',
        )
    except Exception as e:
        return None
        