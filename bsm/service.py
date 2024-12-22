import json
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the log directory and file
LOG_DIR = "/home/majed/bsm/logs"
LOG_FILE = os.path.join(LOG_DIR, "changes.json")

# Ensure the log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

class ChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        log_entry = {
            "event_type": event.event_type,
            "src_path": event.src_path,
            "is_directory": event.is_directory
        }
        with open(LOG_FILE, "a") as log_file:
            log_file.write(json.dumps(log_entry) + "\n")
        print(f"Logged: {log_entry}")

if __name__ == "__main__":
    path_to_monitor = "/home/majed/bsm/test"
    os.makedirs(path_to_monitor, exist_ok=True)  # Ensure the directory exists

    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_monitor, recursive=True)
    observer.start()

    try:
        print(f"Monitoring changes in: {path_to_monitor}")
        while True:
            pass  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

