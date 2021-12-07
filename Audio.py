import speech_recognition as sr

r1 = sr.Recognizer()
with sr.Microphone () as source: 
    print("Di una palabra, yo la interpretare:")
    audio = r1.listen(source)
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition cree que dices " + r1.recognize_google(audio, language='es-MX'))
except sr.UnknownValueError:
    print("Google Speech Recognition no puede entenderte")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
