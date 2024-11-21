from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Assistant')
trainer = ChatterBotCorpusTrainer(chatbot)

# Entraînement avec le corpus français
trainer.train('chatterbot.corpus.french')

while True:
    question = input("Vous : ")
    if question.lower() == "quit":
        break
    reponse = chatbot.get_response(question)
    print("Assistant :", reponse)