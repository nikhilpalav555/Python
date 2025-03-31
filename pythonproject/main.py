import speech_recognition as sr
import webbrowser as wb
import pyttsx3  
import musiclibrary

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = False  # Disable auto-thresholding for better response
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process commands
def processcommand(c):
    c = c.lower()
    
    if "open google" in c:
        wb.open("https://google.com")
    elif "open facebook" in c:
        wb.open("https://facebook.com")
    elif "open instagram" in c:
        wb.open("https://instagram.com")
    elif "open youtube" in c:
        wb.open("https://youtube.com")
    elif "open linkedin" in c:
        wb.open("https://linkedin.com")
    elif c.startswith("play"):
        song = " ".join(c.split(" ")[1:])  # Capture multi-word song names
        
        # Convert dictionary keys to lowercase dynamically
        music_dict = {k.lower(): v for k, v in musiclibrary.music.items()}
        
        if song in music_dict:
            link = music_dict[song]
            speak(f"Playing {song}")
            wb.open(link)
        else:
            speak("Song not found in the library.")

    else:
        #let open  ai  handle the request
        pass


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    # Setup microphone once
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

    # Listen for wake word 'Jarvis'
    while True:
        print("Listening for 'Jarvis'...")
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)

            # Recognize the wake word
            word = recognizer.recognize_google(audio).lower()

            if word == "jarvis":
                speak("Yes?")

                # Listen for command
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
                
                command = recognizer.recognize_google(audio)
                print(f"Command received: {command}")

                processcommand(command)

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results, error: {e}")
        except Exception as e:
            print(f"Error: {e}")
