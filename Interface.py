class Interface:
    @staticmethod
    def show_header(title):
        """Prints a clean, standardized command-line dashboard border."""
        print("\n" + "=" * 45)
        print(f" 🖥️  {title.upper()}  🖥️ ")
        print("=" * 45)

    @staticmethod
    def get_choice(prompt, valid_options):
        """Validates menu selections to ensure robust, error-free navigation."""
        while True:
            choice = input(prompt).strip().lower()
            if choice in valid_options:
                return choice
            print(f"❌ Invalid entry. Choose from: {valid_options}")
