import psutil
import os
import sys

def kill_keylogger(script_name):
    """Kill the keylogger script by name."""
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            if script_name in proc.info['exe']:
                print(f"Terminating process: {proc.info['exe']}")
                proc.terminate()  # Terminate the process
                proc.wait()  # Wait for the process to terminate
                print("Keylogger terminated.")
                return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    print("Keylogger not found.")

if __name__ == "__main__":
    script_name = "keylogger_script.py"  # Replace this with your keylogger script name
    kill_keylogger(script_name)
