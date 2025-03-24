# logger.py
import time

log = []

def write_log(event):
    timestamp = time.strftime("%H:%M:%S")
    entry = f"[{timestamp}] {event}"
    log.append(entry)
    print(entry)

def save_log_file():
    with open("simulation_log.txt", "w") as f:
        for entry in log:
            f.write(entry + "\n")

def predict_failures(bridge_members):
    return [i for i, m in enumerate(bridge_members) if m.is_broken()]