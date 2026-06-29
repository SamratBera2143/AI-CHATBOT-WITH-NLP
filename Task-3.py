# AI Chatbot using NLTK

import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (Run once)
nltk.download('punkt')

# Define chatbot patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi there! Ask me anything."]
    ],
    [
        r"what is your name ?",
        ["I am an AI Chatbot created using Python and NLTK."]
    ],
    [
        r"how are you ?",
        ["I'm doing great! Thank you for asking."]
    ],
    [
        r"who created you ?",
        ["I was created by a Python programmer."]
    ],
    [
        r"what is python ?",
        ["Python is a high-level, interpreted programming language."]
    ],
    [
        r"what is ai ?",
        ["AI (Artificial Intelligence) is the simulation of human intelligence by machines."]
    ],
    [
        r"what is nlp ?",
        ["NLP stands for Natural Language Processing. It helps computers understand human language."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a nice day."]
    ],
    [
        r"(.*)",
        ["Sorry, I don't understand that. Please ask another question."]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

print("=" * 50)
print("      AI CHATBOT WITH NLP")
print("Type 'bye' or 'exit' to quit.")
print("=" * 50)

# Start conversation
chatbot.converse()
