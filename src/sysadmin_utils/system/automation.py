import os

try:
    import pyautogui
except (ImportError, Exception):
    # Fallback for headless environments (CI, servers) where GUI libs are missing.
    # This allows the module to load and tests to patch the attribute.
    pyautogui = type(
        "PyAutoGUIPlaceholder",
        (),
        {"position": lambda: (0, 0), "moveTo": lambda *a, **k: None},
    )


def get_mouse_position():
    """
    Returns the current mouse (x, y) coordinates.
    Used for automation tasks and coordinate tracking.
    """
    if hasattr(pyautogui, "__name__") or pyautogui is not None:
        return pyautogui.position()
    raise RuntimeError("pyautogui is not available in this environment.")


def move_mouse_to(x: int, y: int, duration: float = 0.25):
    """
    Moves the mouse to the specified (x, y) coordinates.
    :param x: Target X coordinate
    :param y: Target Y coordinate
    :param duration: Time in seconds to perform the move
    """
    if hasattr(pyautogui, "__name__") or pyautogui is not None:
        pyautogui.moveTo(x, y, duration=duration)
    else:
        raise RuntimeError("pyautogui is not available in this environment.")


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
