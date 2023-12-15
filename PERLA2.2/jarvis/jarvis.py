import sounddevice as sd
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import numpy as np
import sys

# Configuración del reconocimiento de voz
r = sr.Recognizer()

# Configuración de la voz
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Voz en español

# Activar asistente
def escuchar_palabra_activacion():
    with sd.InputStream(callback=callback, channels=1, samplerate=22050):

        print("Di 'jarvis' para activarme...")
        sd.sleep(1000000)  # Escuchar indefinidamente

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    if np.any(indata):
        texto = reconocer_voz(indata)
        if 'jarvis' in texto:
            hablar("Sí, ¿en qué puedo ayudarte?")

# Función para escuchar
def reconocer_voz(audio):
    audio_data = sr.AudioData(np.asarray(audio), 44100, 2)
    texto = ""
    try:
        texto = r.recognize_google(audio_data, language='es')
    except sr.UnknownValueError:
        pass
    return texto

# Función para darle voz
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

# aquí gestionamos los comandos del asistente
while True:
    activado = escuchar_palabra_activacion()
    if not activado:
        continue

    comando = escuchar_comando()

    if not comando:
        hablar("No detecto ningún comando.")
    elif 'apagar' in comando:
        hablar("Hasta pronto, Apagado.....")
        break
    elif 'reproduce' in comando:
        cancion = comando.replace('reproduce', '')
        hablar("Reproduciendo " + cancion)
        pywhatkit.playonyt(cancion)
    elif 'hora' in comando:
        hora_actual = datetime.datetime.now().strftime('%H:%M:%S')
        hablar("La hora actual es: " + hora_actual)
    else:
        hablar("No entendí tu comando.")
