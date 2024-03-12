import threading
import subprocess
import time
from app import welcome, start_play


# Function to start the Flask app:
def start_flask_app():
    try:
        flask_process = subprocess.Popen(["python", "main_score.py"])
        flask_process.wait()
    except Exception as e:
        print(f"Error starting Flask app: {str(e)}")


# Function to start play + Flask app:
def start_play_with_flask():
    # Start the Flask app in a separate thread:
    flask_thread = threading.Thread(target=start_flask_app)
    flask_thread.start()

    # Wait for a short time to allow the Flask app to start:
    time.sleep(1)

    # Play wog:
    welcome()
    start_play()

    # Stop the Flask app:
    flask_thread.join()


# Call the combined function: start play + start Flask app
start_play_with_flask()
