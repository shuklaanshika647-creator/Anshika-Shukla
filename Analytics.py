class Analytics:
    @staticmethod
    def log_session(username, status, attempts_used):
        """Appends the results of runtime breach attempts safely to a local text file database."""
        try:
            with open("hack_logs.txt", "a") as file:
                file.write(f"User: {username} | Status: {status} | Tries: {attempts_used}\n")
        except IOError:
            print("⚠️ Storage Warning: Unable to update historical logging system.")

    @staticmethod
    def display_logs():
        """Reads and presents historical entry tracking lists for system metrics reporting."""
        print("\n--- 📊 HISTORICAL ACCESS LOGS ---")
        try:
            with open("hack_logs.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No previous breach logs found on disk storage records.")
