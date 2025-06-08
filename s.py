import streamlit as st
import speech_recognition as sr
import requests
import pyjokes
import pywhatkit
import wikipedia
import datetime
import webbrowser
import streamlit.components.v1 as components

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Verse AI Assistant", layout="centered")

# --- Session State Initialization ---
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'speak_enabled' not in st.session_state:
    st.session_state.speak_enabled = True
if 'mic_listening' not in st.session_state:
    st.session_state.mic_listening = False

# --- Text-to-Speech Function ---
def speak(text):
    if st.session_state.speak_enabled and text:
        escaped_text = text.replace('"', '\\"').replace("'", "\\'")
        components.html(f"""
        <script>
        const msg = new SpeechSynthesisUtterance("{escaped_text}");
        window.speechSynthesis.speak(msg);
        </script>
        """, height=0)

# --- Greeting Function ---
def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        greet = "Good Morning! I am your friend Verse to help you."
    elif hour < 18:
        greet = "Good Afternoon! I am your friend Verse to help you."
    else:
        greet = "Good Evening! I am your friend Verse to help you."
    return f"Hello, {greet}"

# --- Voice Recognition ---
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        with st.spinner("🎙 Listening..."):
            audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language='en-in')
            return command.lower()
        except Exception:
            return "Sorry, I couldn't understand that. Please try again."

# --- Assistant Command Logic ---
def run_gone(command):
    if 'wikipedia' in command:
        query = command.replace("wikipedia", "").strip()
        try:
            result = wikipedia.summary(query, sentences=2)
        except Exception:
            result = "Sorry, I couldn't find anything on Wikipedia about that."
        speak(result)
        return f"📚 According to Wikipedia: {result}"

    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
        return "📺 Opening YouTube..."

    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
        return "🌐 Opening Google..."
    
    elif "weather" in command:
        api_key = "8ef61edcf1c576d65d836254e11ea420"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        speak("What's the city name?")
        city_name = take_command()

        if city_name != "None" and city_name.strip() != "":
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                temp = y["temp"]
                humidity = y["humidity"]
                desc = x["weather"][0]["description"]

                weather_info = (
                    f"🌡 Temperature: {temp} K\n"
                    f"💧 Humidity: {humidity}%\n"
                    f"🌤 Description: {desc.capitalize()}"
            )

                speak(f"Temperature is {temp} Kelvin, humidity is {humidity} percent, and the weather is {desc}")
                return weather_info
            else:
                speak("City not found.")
                return "⚠ City not found."
        else: 
            speak("I couldn't hear the city name.")
            return "⚠ City name not detected."

    elif 'tell me a joke' in command or "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)
        return f"😂 Here's a joke: {joke}"
    

    elif "play" in command and "on youtube" in command:
        song = command.replace("play", "").replace("on youtube", "").strip()
        if song:
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)
            return f"🎶 Playing *{song}* on YouTube..."
        else:
            speak("Please say the name of the song.")
            return "⚠ No song name detected."


    elif 'time' in command:
        time_str = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time_str}")
        return f"⏰ The time is {time_str}"

    elif 'stop' in command or 'goodbye' in command:
        speak("Verse is shutting down. Goodbye!")
        return "👋 Verse is shutting down..."

    elif any(phrase in command for phrase in ["about yourself", "who are you", "what can you do", "about you", "introduce yourself", "your capabilities"]):
        about_text = (
            "I am Verse, your personal AI voice assistant built with Python and Streamlit. "
            "I can perform voice-based tasks like searching Wikipedia, opening websites, telling the time, "
            "and giving spoken feedback using text-to-speech. I'm here to make your life easier and more interactive!"
        )
        speak(about_text)
        return f"ℹ {about_text}"

    elif any(phrase in command for phrase in ["about owner", "who built you", "who made you", "about shruti"]):
        about_text = (
            "Hi, I'm Verse! My owner is Radhika — a fun-loving and ambivert person who also enjoys living her moments of solitude. "
            "Her best friend is Shruti , who’s a mix of similar and opposite traits. Despite their differences, "
            "they’re incredibly compatible and make a great pair!"
        )
        speak(about_text)
        return f"ℹ {about_text}"

    else:
        speak("Sorry, I can't help with that yet.")
        return "⚠ Command not recognized. Try again!"

# --- Custom CSS ---
st.markdown("""
    <style>
    .stChatMessage {
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .chat-bubble-assistant {
        background-color: #0a9396;
        color: white;
    }
    .chat-bubble-user {
        background-color: #005f73;
        color: white;
        text-align: right;
    }
    .reportview-container {
        background: linear-gradient(to right, #001219, #005f73);
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title and Description ---
st.markdown("<h1 style='text-align: center; color: cyan;'>🤖 Verse AI Voice Assistant</h1>", unsafe_allow_html=True)
st.markdown("---")

with st.expander("ℹ About Verse AI Assistant"):
    st.markdown("""
    *Verse AI Assistant* is your intelligent voice-controlled assistant built with Python and Streamlit.  
    It can perform the following tasks:

    - Respond to voice commands  
    - Search information on Wikipedia  
    - Open popular websites like YouTube and Google  
    - Tell you the current time  
    - Provide voice feedback using TTS (Text-to-Speech)

    Created to make your life easier and more interactive. Just speak, and Verse will assist you!
    """)

# --- Control Panel ---
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    if st.button("🔁 Clear Chat"):
        st.session_state.chat_history = []
with col2:
    st.session_state.speak_enabled = st.toggle("🔊 Voice Output", value=st.session_state.speak_enabled)
with col3:
    if st.button("🎤 Start Listening") and not st.session_state.mic_listening:
        st.session_state.mic_listening = True
with col4:
    with st.expander("💡 Command Suggestions"):
        st.markdown("""
        - "Open YouTube"  
        - "Open Google"  
        - "Tell me the time"  
        - "Search on Wikipedia"  
        - "Stop" or "Goodbye" 
        - "weather"
        - "jokes"  
        - "play song of your choice"                                       
        """)

# --- Display Chat History ---
for entry in st.session_state.chat_history:
    with st.chat_message(entry["role"]):
        st.markdown(entry["content"])

# --- Handle Microphone Listening ---
if st.session_state.mic_listening:
    command = take_command()
    st.session_state.mic_listening = False  # reset listening state

    if command.strip() != "":
        st.session_state.chat_history.append({"role": "user", "content": f"🗣 {command}"})
        response = run_gone(command)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
    else:
        st.session_state.chat_history.append({"role": "assistant", "content": "⚠ Sorry, no command detected."})

    # No need to st.rerun() — Streamlit will update naturally on next interaction

# --- Initial Greeting ---
if len(st.session_state.chat_history) == 0:
    greet_text = wish_me()
    speak(greet_text)
    st.session_state.chat_history.append({"role": "assistant", "content": greet_text})