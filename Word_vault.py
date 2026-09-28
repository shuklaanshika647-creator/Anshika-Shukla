import random

class WordVault:
    def __init__(self):
        # Database dictionary containing password target clusters matching exact string lengths
        self.vault = {
            "1": ["CODE", "DATA", "HASH", "BYTE", "PORT", "PING"],
            "2": ["CYBER", "LOGIC", "PROXY", "TOKEN", "ARRAY", "SHIFT"],
            "3": ["ROUTER", "MATRIX", "BINARY", "KERNEL", "SCRIPT", "SECURE"]
        }

    def get_word_list(self, difficulty):
        """Randomly selects a password and fetches the operational word cluster choice list."""
        words = self.vault.get(difficulty, self.vault["1"])
        secret_word = random.choice(words)
        return words, secret_word
