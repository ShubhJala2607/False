# streamlit_app.py

import streamlit as st
import subprocess

# Function to start the Flask app
def start_flask():
    subprocess.Popen(["python", "flask_app.py"])

# Display a message to start the Flask app
st.title("Flask App on Streamlit Cloud")
st.write("Click the button below to start the Flask app.")

if st.button("Start Flask App"):
    start_flask()
    st.write("Flask app started!")

st.write("The Flask app is running. You can now make requests to it.")
