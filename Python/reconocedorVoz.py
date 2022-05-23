import speech_recognition as sr
import time

def reconocerVoz():
    r = sr.Recognizer()
    with sr.Microphone () as source: 
        r.adjust_for_ambient_noise(source)
        print("Grabando...")
        audio = r.listen(source, timeout= 5, phrase_time_limit=None)
    try:
        texto = r.recognize_google(audio, language='es-MX')
    except sr.UnknownValueError:
        texto = "No fue posible entenderte"
    except sr.RequestError as e:
        texto = "No se pudieron solicitar los resultados del servicio de reconocimiento de voz {0}".format(e)
    return texto