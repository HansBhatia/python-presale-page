import streamlit as st
from PIL import Image

from components.st_mailing_list import render_mail_list
from components.st_stripe_checkout import render_stripe_checkout

st.title('Presale: The Enforcer')
echo_image = Image.open('./assets/amazon_echo_image.webp')
st.image(echo_image, caption='Alexa enforcer')

quantity = st.number_input(label='Item Quantity: ', min_value=1, value=1, step=1)

render_stripe_checkout(quantity)

st.markdown('''
## About
- The alexa enforcer allows you to complete your life goals and everyday tasks. As humans, we struggle to stay motivated
without any external interference. But now, with the alexa enforcer, things have changed. 
## Specs
- PREMIUM SOUND: Rich, detailed sound that automatically adapts to any room. Supports lossless HD audio available on select streaming services such as Amazon Music HD.
- VOICE CONTROL YOUR MUSIC: Stream songs from Amazon Music, Apple Music, Spotify, SiriusXM, and more. HD requires a compatible music streaming service.
            ''')

render_mail_list()