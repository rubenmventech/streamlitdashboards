import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.write("Hello Diana")

lottie_love = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_jvxwtdtp.json")

st_lottie(lottie_love, height=300, key="coding")