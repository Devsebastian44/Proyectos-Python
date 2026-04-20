import os
import shutil


def shutdown_system(delay: int = 60):
    """
    Schedules a system shutdown.
    """
    print(f"System will shutdown in {delay} seconds.")
    import subprocess

    cmd = shutil.which("shutdown") or "shutdown"
    if os.name == "nt":
        subprocess.run([cmd, "/s", "/t", str(delay)], shell=False)  # noqa: S603, S607
    else:
        sudo_cmd = shutil.which("sudo") or "sudo"
        subprocess.run(
            [sudo_cmd, cmd, "-h", f"+{delay // 60}"],
            shell=False,  # noqa: S603, S607
        )


def cancel_shutdown():
    """
    Cancels a scheduled shutdown.
    """
    print("Canceling scheduled shutdown...")
    import subprocess

    cmd = shutil.which("shutdown") or "shutdown"
    if os.name == "nt":
        subprocess.run([cmd, "/a"], shell=False)  # noqa: S603, S607
    else:
        sudo_cmd = shutil.which("sudo") or "sudo"
        subprocess.run([sudo_cmd, cmd, "-c"], shell=False)  # noqa: S603, S607


if __name__ == "__main__":
    # WARNING: Be careful when running this script
    print("Shutdown controller (Test mode)")
    # cancel_shutdown() # Just to be safe
