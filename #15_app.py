#%% 
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My first Streamlit Website", page_icon=":peach:", layout="wide")

def load_lottie(url): 
    r = requests.get(url)
    if r.status_code != 200: 
        return None
    return r.json()

url = "https://static.coingecko.com/s/rocket-emoji-bd92cd2d54bcd1d4b3056ea59d1c9fcac16ff2414c6c7deb5a3bf3dfc28743a9.json"
img = Image.open("coingecko.png")

with st.container():
    st.header("Hello")
    st.title("I'm just trying to make my first Streamlit website")
    st.write("Idk man")
    st.write("[Learn more > ](https://www.coingecko.com)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("idk again")
    with right_column: 
        st_lottie(url, height=300, key="idk")

with st.container(): 
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column: 
        st.image(img)
    with text_column: 
        st.header("LALALA")
        st.write("HMMMMMMMM")
# %%
with st.container(): 
    st.write("---")
    st.header("Don't reach out to me")
    st.write("##")

contact_form = """
<form action="https://formsubmit.co/user@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column: 
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()