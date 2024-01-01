import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/styles.css")

# load assets
lottie_coding = load_lottieurl("https://lottie.host/6e09e5e3-14ff-4a30-8117-7c6b6ba827ab/otowj3wrtK.json")
image_avm = Image.open("images/AVM.jpg")
image_srm = Image.open("images/SRM.JPG")
# Header
with st.container():
    st.subheader("Hi, I am Huma :wave:")
    st.title("An Electrical Engineer from Pakistan")
    st.write(
        "Welcome to my corner of the web! Explore my journey, passions, and experiences as I share my world with you.")
    st.write("[Learn More >](https://sites.google.com/view/humahashmi/home)")
# about myself
# Add divider
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Short Biography")
        # insert some space to next element
        st.write("##")
        st.write(
            "I am Huma Hashmi from Islamabad, Pakistan. I have completed my bachelors in Electrical Electronic Engineering from COMSATS University Islamabad, Abbottabad Campus. I have secured CGPA of 3.42 out of 4.00. My main research interests include Machine Learning, Robotics, Power Electronics, Microsystems Technologies and Neural Engineering. I am also a Youtuber, working on arts and sharing fact contents.")
        st.write("[Youtube Channel >](https://www.youtube.com/channel/UCJFUU2iwSGRQW1emh7m8nug)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
# PROJECTS
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image_avm)

    with text_column:
        st.subheader("Automatic Electronic Voting System")
        st.write(
            "The project's goal was to create an Electronic Voting System (EVS) that would employ facial recognition to identify a voter before casting a vote. This concept also aims to combat rigging by providing each person with a unique ID based on their facial print. For the purpose of face detection and recognition, we collected a diverse dataset of faces in a variety of contexts, including occlusions, posture alterations, and position shifts. We conducted a tonne of trials to ensure that the system was as accurate as possible. The technique was time-effective, as it turned out. Based on the facts indicated above, this project also tries to present an efficient solution to transparency, a free and fair manner of holding elections, and an accurate, reliable, robust, and automated electronic voting system that can work in real-time. ")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image_srm)

    with text_column:
        st.subheader("Design and Analysis of Switched Reluctance Motor")
        st.write(
            "In this project, MATLAB Simulink is used to do a simulation analysis of a three-phase 6/4 Poles Switched Reluctance Motor to examine the effect of changing terminal voltage on speed. An Equivalent Circuit is also calculated without taking into account mutual inductance between the phases.")
# Contact Form
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")
    contact_form = """ 
    <form action="https://formsubmit.co/hmahashmi735@gmail.com" method="POST">
       <input type="hidden" name="_captcha" value="false">
       <input type="text" name="name" placeholder="Your name" required>
       <input type="email" name="email" placeholder="Your email" required>
       <textarea name="message" placeholder="Your message here" required></textarea>
       <button type="submit">Send</button>
    </form>"""
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
