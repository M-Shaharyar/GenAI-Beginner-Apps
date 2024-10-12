# Import the required libraries
from dotenv import load_dotenv  # Load environment variables from a .env file
import streamlit as st  # Streamlit for building the web application
import os  # Interacting with the operating system for environment variables
import google.generativeai as genai  # Google Generative AI library for content generation
from PIL import Image  # PIL library to handle image files

# Load all environment variables from the .env file
load_dotenv()

# Configure the Google Generative AI library with the API key retrieved from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the GenerativeModel using the "gemini-1.5-flash" model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get responses from the Gemini model based on input text and image
def get_gemini_response(input, image):
    # Check if the input text is not empty
    if input != '':
        # Generate content using both the input text and the image
        response = model.generate_content([input, image])
    else:
        # Generate content using only the image when no text input is provided
        response = model.generate_content(image)
    # Return the text part of the response
    return response.text

# Set the configuration for the Streamlit app, including the page title
st.set_page_config(page_title="Gemini Image Demo")

# Display the title of the application
st.title("Gemini Image Demo")

# Create a text input box for the user to enter a prompt or description
input = st.text_input("Input Prompt: ", key='input')

# Allow the user to upload an image file (jpg, jpeg, or png)
uploaded_file = st.file_uploader("Choose an image: ", type=['jpg', 'jpeg', 'png'])

# Initialize an empty variable for the image
image = ""

# Check if the user has uploaded an image file
if uploaded_file is not None:
    # Open the uploaded image file using PIL
    image = Image.open(uploaded_file)
    # Display the uploaded image with a caption, using the column width for better scaling
    st.image(image, caption='Uploaded Image', use_column_width=True)

# Create a button for the user to submit the prompt and image for analysis
submit = st.button("Tell me about the image")

# Check if the submit button is clicked
if submit:
    # Get the response from the Gemini model using the user's input and uploaded image
    response = get_gemini_response(input, image)
    # Display a subheader for the response section
    st.subheader("The Response is")
    # Display the response text from the Gemini model
    st.markdown(f"<p style='font-size:20px;'>{response}</p>", unsafe_allow_html=True)
