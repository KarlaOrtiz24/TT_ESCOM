import speech_recognition as sr

def reconocerVoz():
    r = sr.Recognizer()
    with sr.Microphone () as source: 
        r.adjust_for_ambient_noise(source, duration = 1)
        print("Di una palabra, yo la interpretare:")
        audio = r.listen(source, phrase_time_limit=None)
    try:
        texto = r.recognize_google(audio, language='es-MX')
    except sr.UnknownValueError:
        texto = "Google Speech Recognition no puede entenderte"
    except sr.RequestError as e:
        texto = "No se pudieron solicitar los resultados del servicio de reconocimiento de voz de Google {0}".format(e)
    return texto