import os


def clear_screen():
    """Clears the terminal screen."""
    import subprocess

    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], shell=False)  # noqa: S603, S607
    else:
        subprocess.run(["clear"], shell=False)  # noqa: S603, S607


def interactive_menu():
    """Runs a simple interactive menu."""
    clear_screen()
    print("--- System Automation Menu ---")

    while True:
        try:
            prompt = "\nEnter option (1: Print XD, q: Quit): "
            user_input = input(prompt).strip()

            if not user_input:
                print("Please enter a valid option.")
                continue

            if user_input == "1":
                print("XD")
            elif user_input.lower() == "q":
                print("Exiting...")
                break
            else:
                print(f"Unknown option: {user_input}")

        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    interactive_menu()
