import openai
import pyttsx3
import speech_recognition as sr

# pip install openai
# pip install pyttsx3
# pip install SpeechRecognition


openai.api_key = "YOUR API KEY"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Hello sir , tell me how may I help you")

def getCommand():

    reco = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        reco.pause_threshold = 1
        audio = reco.listen(source)

    try:
        print("Recognizing...")    
        query = reco.recognize_google(audio, language='en-in')

    except:
        return "None"
    return query

def respondGPT(text):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= text,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    return response.choices[0].text

if __name__ == "__main__":
    wishMe()
    while True:
        query = getCommand().lower()
        if "stop" in query :
            speak("Stopped sir")
            break
        if "jarvis" in query or query == "None":
            speak("Sure sir")
            speak(respondGPT(query))
        else :
            continue
