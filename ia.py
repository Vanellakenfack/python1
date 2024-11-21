import  pyttsx3
import  requests
#lecture=pyPDF2()

droid=pyttsx3.init()
droid.say('bonjour  kenfack vanella je suis un droid de la 3e  generation et je suis alexia j ai des questions a te poser qu est ce que tu a mange aujourdhui')
droid.runAndWait()
# Capturer la réponse de l'utilisateur
rep = input("Qu'est-ce que tu as mangé aujourd'hui ? ")
droid.say("Tu as mangé " + rep + ". C'est délicieux !")
droid.runAndWait()


def get_weather():
    api_key = "votre_api_key"
    city = "Paris"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=fr&units=metric"
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        return f"La température à {city} est de {data['main']['temp']}°C avec {data['weather'][0]['description']}."
    else:
        return "Je n'ai pas pu obtenir la météo."

# Utilisation dans le dialogue
droid.say("Voulez-vous connaître la météo aujourd'hui ?")
droid.runAndWait()
droid.say(get_weather())
droid.runAndWait()