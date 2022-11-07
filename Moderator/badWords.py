words = [
    "kanker"
]

def check_words(message, words):
    for word in words:
        if word in message.content.lower():
            return True
    return False