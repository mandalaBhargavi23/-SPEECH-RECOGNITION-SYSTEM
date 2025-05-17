import speech_recognition as sr # it will access its features and tools for converting spoken audio into text

def recognize_speech_from_mic():
    # Create an instance of the Recognizer class
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        # Adjust the recognizer sensitivity to ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Listening... Speak into the microphone.")
        # Listen for the first phrase and extract audio data
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text  # Return the recognized text
    except sr.UnknownValueError:
        # Error: Speech was unintelligible
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        # Error: Could not request results from the service (e.g., network issue)
        print("Request failed. Check your internet connection.")

# Run the function only if this script is executed directly
if __name__ == "__main__":
    recognize_speech_from_mic()

