# Importing the necessary libraries
from dotenv import load_dotenv  # Load environment variables from a .env file
import streamlit as st  # Streamlit for building the web application
import os  # OS module for interacting with the operating system
import google.generativeai as genai  # Google Generative AI library for content generation

# Load environment variables from the .env file
load_dotenv()

# Configure the Google Generative AI with the API key from the environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the GenerativeModel using the "gemini-pro" model
model = genai.GenerativeModel("gemini-pro")

# Function to get responses from the Gemini model based on user input
def get_gemini_response(question):
    # Generate content based on the input question using the Gemini model
    response = model.generate_content(question)
    # Return the text part of the generated response
    return response.text

# Set the configuration for the Streamlit app, including the page title
st.set_page_config(page_title="Q&A Demo")

# Display the application header with specified font size
st.markdown("<h1 style='font-size:40px;'>Gemini LLM Application</h1>", unsafe_allow_html=True)

# Create an input text box for the user to type their question with specified font size
st.markdown("<p style='font-size:40px;'>Input:</p>", unsafe_allow_html=True)
input = st.text_input("Input:", key='input', label_visibility='hidden')  # Provide a valid label

# Create a button for the user to submit their question
submit = st.button("Submit your question")

# Check if the submit button is clicked
if submit:
    # Retrieve the response from the Gemini model based on the user's input
    response = get_gemini_response(input)
    # Display the response text below the input field with increased font size
    st.markdown("<p style='font-size:40px;'>The Response is:</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:40px;'>{response}</p>", unsafe_allow_html=True)
