# Import the required libraries
from dotenv import load_dotenv  # For loading environment variables from a .env file
import streamlit as st  # Streamlit for building the web application
import os  # For interacting with the operating system
import google.generativeai as genai  # Google Generative AI library for content generation

# Load environment variables from the .env file
load_dotenv()

# Configure the Google Generative AI with the API key retrieved from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the GenerativeModel using the "gemini-pro" model
model = genai.GenerativeModel('gemini-pro')

# Start a chat session with an empty history using the Gemini model
chat = model.start_chat(history=[])

# Function to get a response from the Gemini model based on the user's question
def get_gemini_response(question):
    # Send a message to the chat model and get a streaming response
    response = chat.send_message(question, stream=True)
    # Return the streaming response for further processing
    return response

# Set the configuration for the Streamlit app, including the page title
st.set_page_config(page_title="Q&A Demo")

# Display the header of the application
st.header("Gemini LLM Application")

# Initialize session state to store chat history if it doesn't already exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []  # Store user-bot interactions as a list of tuples

# Create a text input box for the user to enter their question
input = st.text_input('Input: ', key="input")

# Create a button for the user to submit their question
submit = st.button('Ask the question')

# If the submit button is clicked and the input is not empty
if submit and input:
    # Get the response from the Gemini model using the user's input
    response = get_gemini_response(input)
    
    # Add the user's query to the session state chat history
    st.session_state['chat_history'].append(("You", input))
    
    # Display the response section with a subheader
    st.subheader("The Response is ")
    
    # Display a horizontal line separator to differentiate between current chat and chat history
    st.markdown("---")

    # Iterate through the response chunks (for streaming responses)
    for chunk in response:
        # Write each chunk of the response
        st.write(chunk.text)
        # Add the bot's response to the session state chat history
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display a horizontal line separator to differentiate between current chat and chat history
st.markdown("---")
    
# Display the entire chat history with a subheader
st.subheader("The chat history is:")
# Loop through the chat history and display each role (user or bot) and the respective text
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
