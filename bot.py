import os
import telebot
import random

# Utiliser la variable d'environnement pour le token
TOKEN =os.eviron.get('6786499988:AAEeq0a0VJYWUepDnWwQu1wS8zwngiNzSO0')

bot = telebot.TeleBot(6786499988:AAEeq0a0VJYWUepDnWwQu1wS8zwngiNzSO0)

manga_recommendations = [
    "One Piece", "Naruto", "Attack on Titan", "Death Note", "My Hero Academia",
    "Fullmetal Alchemist", "Dragon Ball", "Tokyo Ghoul", "Demon Slayer", "Hunter x Hunter"
]

manga_facts = [
    "Le manga le plus vendu de tous les temps est One Piece.",
    "Osamu Tezuka, créateur d'Astro Boy, est souvent appelé le 'Dieu du manga'.",
    "Le terme 'manga' a été inventé par le célèbre artiste Hokusai au 19ème siècle.",
    "Les mangas se lisent généralement de droite à gauche.",
    "Le plus long manga jamais publié est JoJo's Bizarre Adventure, avec plus de 130 volumes."
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bienvenue sur le bot de divertissement manga ! Utilisez /recommend pour obtenir une recommandation de manga ou /fact pour un fait amusant sur les mangas.")

@bot.message_handler(commands=['recommend'])
def send_recommendation(message):
    recommendation = random.choice(manga_recommendations)
    bot.reply_to(message, f"Je vous recommande de lire : {recommendation}")

@bot.message_handler(commands=['fact'])
def send_fact(message):
    fact = random.choice(manga_facts)
    bot.reply_to(message, f"Saviez-vous que : {fact}")

if __name__ == "__main__":
    print("Le bot démarre...")
    bot.polling()
    print("Le bot s'est arrêté.")
