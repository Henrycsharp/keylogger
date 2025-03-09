import psutil
import sys

def kill_keylogger(script_name):
    """Kill the keylogger script based on the process name or path."""
    for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
        try:
            # Check if the process is a Python process and if it matches the script name
            if proc.info['name'] == 'python' and script_name in ' '.join(proc.info['cmdline']):
                print(f"Terminating process: {proc.info['pid']} - {proc.info['cmdline']}")
                proc.terminate()  # Terminate the process
                proc.wait()  # Wait for the process to terminate
                print("Keylogger terminated.")
                return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    print("Keylogger not found.")

if __name__ == "__main__":
    script_name = "keylogger_script.py"  # Replace with the exact script name or part of it
    kill_keylogger(main.py)
