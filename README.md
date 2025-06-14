# 🤖 Verse AI Voice Assistant

Verse is your friendly AI voice assistant built with *Python* and *Streamlit*. It listens to your voice commands, responds with speech, and performs various helpful tasks like searching Wikipedia, telling jokes, playing songs on YouTube, providing weather updates, and more — all through a clean, interactive interface.

---

## 🧠 Features

- 🎙 Voice Command Recognition  
- 📢 Text-to-Speech Voice Output  
- 🔎 Wikipedia Search  
- 📺 Open Websites like YouTube and Google  
- ⏰ Get Current Time  
- 🎵 Play Songs on YouTube  
- 🌦 Get Real-Time Weather Information  
- 😂 Tell Jokes  
- 🧠 Responds to questions about itself and its creator

---

## 🛠 Tech Stack

- Python 3.8+
- [Streamlit](https://streamlit.io/) — for web UI
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) — for voice input
- [PyWhatKit](https://pypi.org/project/pywhatkit/) — for playing YouTube videos
- [Wikipedia](https://pypi.org/project/wikipedia/) — for summary searches
- [PyJokes](https://pypi.org/project/pyjokes/) — for random jokes
- [Requests](https://pypi.org/project/requests/) — for API calls (e.g., weather)
- Web APIs: [OpenWeatherMap](https://openweathermap.org/api)

---

## 🚀 How to Run Locally

### 1. Clone the Repository

bash
git clone :https://github.com/radhika-025/AI-Voice.git
cd Verse-ai-assistant


### 2. Install Required Libraries

You can use pip to install dependencies:

bash
pip install -r requirements.txt


> Create a requirements.txt with:
txt
streamlit
speechrecognition
pyjokes
pywhatkit
wikipedia
requests


### 3. Set Your OpenWeatherMap API Key

Replace this line in your code with your actual API key:

python
api_key = "YOUR_OPENWEATHERMAP_API_KEY"


You can get your free key here: [https://openweathermap.org/](https://openweathermap.org/)

### 4. Run the App

bash
streamlit run app.py


---

## 🎮 Voice Command Examples

Try saying:

- Open YouTube
- What's the weather like?
- Play Faded on YouTube
- Search India on Wikipedia
- Tell me a joke
- What time is it?
- Who made you?

---

## 📦 Folder Structure (Suggestion)


APP
├── final.py
├── README.md
└── requirements.txt


---

## 👤 About the Creator

*Radhika* — A fun-loving and ambivert person who also enjoys living her moments of solitude who built Verse with a passion for interactive AI experiences.

---

## 📃 License

This project is open source and free to use under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🙌 Acknowledgements

- Streamlit Team
- OpenWeatherMap API
- Python Speech Recognition Library
