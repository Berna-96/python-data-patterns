from datetime import datetime

def write_log(level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] [{level}] {message}\n")

