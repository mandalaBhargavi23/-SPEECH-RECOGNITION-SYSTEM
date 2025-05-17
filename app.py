import streamlit as st  # Streamlit for building the web app interface
import speech_recognition as sr  

# Function to handle speech recognition from the microphone
def recognize_speech():
    recognizer = sr.Recognizer()  # Create a Recognizer instance

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        # Show a spinner while adjusting for ambient noise
        with st.spinner("Adjusting for ambient noise..."):
            recognizer.adjust_for_ambient_noise(source, duration=1)

        # Notify the user that listening has started
        st.success("Listening... Speak now.")
        audio = recognizer.listen(source)  # Capture the audio input

    try:
        # Show a spinner while recognizing speech
        with st.spinner("Recognizing speech..."):
            # Use Google's Web Speech API to transcribe the audio
            text = recognizer.recognize_google(audio)

        # Notify the user that recognition was successful
        st.success("Recognition successful!")
        return text  # Return the recognized text

    # Handle case where speech was unintelligible
    except sr.UnknownValueError:
        st.error("Could not understand the audio.")
    # Handle case where there was a problem with the API request
    except sr.RequestError:
        st.error("Could not request results; check your internet connection.")

# Streamlit user interface
st.title("🎙️ Speech Recognition App")  # App title
st.write("Click the button below and start speaking.")  # Instructions

# Add a button to start recording
if st.button("Start Recording"):
    result = recognize_speech()  # Call the speech recognition function
    if result:
        # Display the recognized text in a text area
        st.text_area("Recognized Text", result, height=150)
