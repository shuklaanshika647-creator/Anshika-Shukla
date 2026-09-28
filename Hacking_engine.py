from interface import Interface
from word_vault import WordVault
from analytics import Analytics

class HackingEngine:
    def __init__(self):
        self.vault = WordVault()

    def play_round(self):
        """Controls the interactive turn-based sequence logic loop for password guessing."""
        Interface.show_header("Initializing Breach")
        username = input("Enter Hacker Handle/Name: ").strip() or "Guest_Netrunner"
        
        print("\nSelect Security Level:")
        print(" [1] Low Security (4-letter keys)")
        print(" [2] Medium Security (5-letter keys)")
        print(" [3] High Security (6-letter keys)")
        diff = Interface.get_choice("Select Level (1-3): ", ["1", "2", "3"])

        word_options, secret_word = self.vault.get_word_list(diff)
        attempts_left = 4

        print(f"\n🔐 TARGET LOCKED. ENTER CORRECT PASSKEY CLUSTER LINK:")
        print(" | ".join(word_options))

        while attempts_left > 0:
            print(f"\n⏱️ Security Clearance Tries Left: {attempts_left}")
            guess = input("Enter Password Guess: ").strip().upper()

            if guess not in word_options:
                print("❌ Encryption sequence unrecognized by active memory cluster. Try again.")
                continue

            if guess == secret_word:
                print("\n🎉 SUCCESS! Access Granted. Mainframe matrix compromised.")
                Analytics.log_session(username, "SUCCESS", 5 - attempts_left)
                return

            # Main comparative algorithmic matching mechanism
            matches = sum(1 for a, b in zip(guess, secret_word) if a == b)
            print(f"⛔ ACCESS DENIED. Cryptographic Match: {matches}/{len(secret_word)} positions correct.")
            attempts_left -= 1

        print(f"\n💀 TERMINAL LOCKOUT INITIATED! Decrypted core was: {secret_word}")
        Analytics.log_session(username, "FAILED", 4)
