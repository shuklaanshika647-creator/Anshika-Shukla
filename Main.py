from interface import Interface
from hacking_engine import HackingEngine
from analytics import Analytics

def main():
    """Initializes and runs the continuous program workflow interface loop."""
    engine = HackingEngine()
    
    while True:
        Interface.show_header("Network Shield Terminal")
        print(" [1] Launch Cyber Hack Simulation")
        print(" [2] Read Mainframe Breach Logs")
        print(" [3] Terminate Program Connection")
        
        choice = Interface.get_choice("\nSelect Directive (1-3): ", ["1", "2", "3"])
        
        if choice == "1":
            engine.play_round()
            input("\nPress Enter to return to main command menu...")
        elif choice == "2":
            Analytics.display_logs()
            input("\nPress Enter to return to main command menu...")
        elif choice == "3":
            print("\nConnection safely terminated. Systems operational. Goodbye.")
            break

if __name__ == "__main__":
    main()

       
