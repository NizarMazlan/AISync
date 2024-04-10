# import libraries
import streamlit as st
import sqlite3
import webbrowser
import base64
from annotated_text import annotated_text
from streamlit_extras.app_logo import add_logo 
import io
from PIL import Image

'''
file = open("logoo.png", "rb")
contents = file.read()
img_str = base64.b64encode(contents).decode("utf-8")
buffer = io.BytesIO()
file.close()
img_data = base64.b64decode(img_str)
img = Image.open(io.BytesIO(img_data))
resized_img = img.resize((150, 60))  # x, y
resized_img.save(buffer, format="PNG")
img_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
st.code("st.image('./logoo.png')")
st.image('./logoo.png')


st.markdown(
        f"""
        <style>
            [data-testid="stSidebar"] {{
                background-image: url('data:image/png;base64,{img_b64}');
                background-repeat: no-repeat;
                padding-top: 50px;
                background-position: 100px 50px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] {
                background-image: url(http://placekitten.com/200/200);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebar"]::before {
                content: "My Company Name";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
'''

st.markdown("<h1 style='text-align: left; color: black;'>AiSync 🌊</h1>", unsafe_allow_html=True)
#st.title("AiSync 🌊")
annotated_text(
    ("Revolutionizing Water Meter Inventory Management","","#8ef"), )
st.markdown("<h2 style='text-align: left; color: black;'>Welcome to our home page! </h2>",unsafe_allow_html=True)

st.markdown("<h3 style='text-align: left; color: #00008B;'>About Us </h3>",unsafe_allow_html=True)
st.text("AiSync is an advanced proposed solution brought to you by Swiftly with the purpose  of digitally revolutionizing the water meter inventory management of Air Selangor Sdn Bhd.")

# BACKGROUND IMAGE (and sidebar color)

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://i.postimg.cc/XvQjmgbG/Untitled-design-1.png");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
    }

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

[data-testid="stSidebar"] {
    background: LightBlue;
    }

</style>
"""

st.markdown(background_image, unsafe_allow_html=True) 