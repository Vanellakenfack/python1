import tkinter as tk
import requests

class AppMeteo:
    def __init__(self, master):
        self.master = master
        self.master.title("Application Météo")
        
        self.label_ville = tk.Label(master, text="Entrez le nom de la ville :", font=("Arial", 14))
        self.label_ville.pack(pady=10)

        self.entry_ville = tk.Entry(master, font=("Arial", 14))
        self.entry_ville.pack(pady=10)

        self.bouton_rechercher = tk.Button(master, text="Rechercher", command=self.obtenir_meteo, font=("Arial", 14))
        self.bouton_rechercher.pack(pady=20)

        self.label_resultat = tk.Label(master, text="", font=("Arial", 14))
        self.label_resultat.pack(pady=20)

    def obtenir_meteo(self):
        ville = self.entry_ville.get()
        api_key = 'votre_api_key'  # Remplacez par votre clé API
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric&lang=fr"
        
        try:
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                temperature = data['main']['temp']
                description = data['weather'][0]['description']
                self.label_resultat.config(text=f"Météo à {ville}: {temperature}°C, {description}")
            else:
                self.label_resultat.config(text="Ville non trouvée.")
        except Exception as e:
            self.label_resultat.config(text="Erreur lors de la récupération des données.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppMeteo(root)
    root.mainloop()