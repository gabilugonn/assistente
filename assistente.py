import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia

engine = pyttsx3.init()
wikipedia.set_lang("pt")

def speak(audio):
    print(f"Assistente: {audio}")
    engine.say(audio)
    engine.runAndWait()
    
def getCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {query}\n")
    except Exception as e:
        print("Não entendi. Pode repetir?")
        return "Nenhum comando"
    return query.lower()

if __name__ == "__main__":
    speak("Assistente Digital foi ativada")
    speak("Como eu posso te ajudar?")

    while True:
        command = getCommand()
        
        if 'wikipédia' in command or 'wikipedia' in command:
            speak("Pesquisando na Wikipédia...")
            command = command.replace("wikipédia", "")
            command = command.replace("wikipedia", "")
            command = command.replace("procure na", "")
            command = command.replace("pesquise na", "")

            try:
                results = wikipedia.summary(command, sentences=2)
                speak("De acordo com a Wikipédia:")
                speak(results)
            except Exception as e:
                speak("Não consegui encontrar nada sobre isso na Wikipédia.")
                
        elif 'youtube' in command:
            speak("Abrindo o Youtube")
            webbrowser.open("https://www.youtube.com")
            break
            
        elif 'google' in command:
            speak("Abrindo o Google")
            webbrowser.open("https://www.google.com")
            break
            
        elif 'calculadora' in command:
            speak("Abrindo a Calculadora")
            os.system("open -a Calculator")
            
        elif 'tchau' in command or 'sair' in command:
            speak("Tchau Tchau")
            break
