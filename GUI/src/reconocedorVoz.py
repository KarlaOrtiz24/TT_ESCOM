import speech_recognition as sr
import time
import Routes.Routes as routes

def reconocerVoz():
    r = sr.Recognizer()
    with sr.AudioFile(routes.juntarRutas(routes.getRutaActual(__file__), 'audioTraducir.wav')) as source: 
        r.adjust_for_ambient_noise(source)
        print("Grabando...")
        # audio = r.listen(source, timeout= 5, phrase_time_limit=None)
        nuevo_audio = r.record(source)
    try:
        texto = r.recognize_google(nuevo_audio, language='es-MX')
    except sr.UnknownValueError:
        texto = "No fue posible entenderte"
    except sr.RequestError as e:
        texto = "No se pudieron solicitar los resultados del servicio de reconocimiento de voz {0}".format(e)
    return texto

# print(reconocerVoz())

# import soundfile as sf

# data, samplerate = sf.read(routes.juntarRutas(routes.getRutaActual(__file__), 'audioTraducir.mp3'))
# sf.write(routes.juntarRutas(routes.getRutaActual(__file__), 'nuevo_audioTraducir.wav'), data, samplerate)