import tkinter as tk
from tkinter import messagebox
import random
import time

# Questions par catégorie et difficulté
questions = {
    "facile": {
    },
    "moyen": {
        "Un train electrique qui va vers le nord a grande vitesse de 90km/h, dans quel sens va se dirige la fumeé ? Vers le sud/ouest/est?????": "garrr tu ndemmm un train electrique n a pas de fumeé🤣🤣🤣🤣",

    },
    "difficile": {
    },
}

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Interactif")
        
        self.score = 0
        self.bonnes_reponses_consecutives = 0
        self.current_question = ""
        self.current_answer = ""
        self.start_time = 0
        
        # Interface de sélection de difficulté
        self.label = tk.Label(master, text="Choisissez la difficulté :", font=("Arial", 16))
        self.label.pack(pady=20)

        self.var_difficulte = tk.StringVar(value="facile")
        self.rb_facile = tk.Radiobutton(master, text="Facile", variable=self.var_difficulte, value="facile")
        self.rb_moyen = tk.Radiobutton(master, text="Moyen", variable=self.var_difficulte, value="moyen")
        self.rb_difficile = tk.Radiobutton(master, text="Difficile", variable=self.var_difficulte, value="difficile")
        
        self.rb_facile.pack()
        self.rb_moyen.pack()
        self.rb_difficile.pack()
        
        self.start_button = tk.Button(master, text="Démarrer le Quiz", command=self.start_quiz)
        self.start_button.pack(pady=20)

        self.question_label = tk.Label(master, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(master, font=("Arial", 14))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Soumettre", command=self.check_answer)
        self.submit_button.pack(pady=20)

    def start_quiz(self):
        self.score = 0
        self.bonnes_reponses_consecutives = 0
        self.ask_question()

    def ask_question(self):
        difficulty = self.var_difficulte.get()
        self.current_question, self.current_answer = random.choice(list(questions[difficulty].items()))
        self.question_label.config(text=self.current_question)
        self.answer_entry.delete(0, tk.END)
        self.start_time = time.time()
        
        # Chronomètre de 15 secondes
        self.master.after(2000000, self.time_up)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        elapsed_time = time.time() - self.start_time
        
        if user_answer.lower() == self.current_answer.lower():
            self.score += 1
            self.bonnes_reponses_consecutives += 1
            messagebox.showinfo("Correct !", "Bonne réponse !")
        else:
            self.bonnes_reponses_consecutives = 0
            messagebox.showerror("garrr tu ndemmm un train electrique n'a pas de fumeé🤣🤣🤣🤣", f"Mauvaise réponse. La bonne réponse est : {self.current_answer}")
        
        # Vérification des récompenses
        if self.bonnes_reponses_consecutives in (3, 5, 7):
            messagebox.showinfo("Récompense !", "Vous avez obtenu une récompense pour vos bonnes réponses consécutives !")

        self.ask_question()

    def time_up(self):
        messagebox.showwarning("Temps écoulé", "Le temps est écoulé pour cette question.")
        self.bonnes_reponses_consecutives = 0
        self.ask_question()

# Lancer l'application
root = tk.Tk()
quiz_app = QuizApp(root)
root.mainloop()