import os
from datetime import datetime, timedelta


class Memory:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        self.log_file = os.path.join(BASE_DIR, "data", "logs.txt")

        self.cache = {}
        self.messages = {}

        # auto cleanup on startup
        self.delete_old_logs(7)

    # -----------------------------
    # CACHE
    # -----------------------------
    def get_cache(self, key):
        return self.cache.get(key)

    def set_cache(self, key, value):
        self.cache[key] = value

    # -----------------------------
    # DATE KEY (DAILY GROUPING)
    # -----------------------------
    def get_week(self):
        return datetime.now().strftime("%Y-%m-%d")

    # -----------------------------
    # CHAT MEMORY (RAM)
    # -----------------------------
    def get_messages(self, week):
        return self.messages.setdefault(week, [])

    def add_message(self, week, role, content):
        self.messages.setdefault(week, []).append({
            "role": role,
            "content": content
        })

        self._save_to_file(week, role, content)

    # -----------------------------
    # FILE LOGGING
    # -----------------------------
    def _save_to_file(self, week, role, content):
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] ({week}) {role}: {content}\n")

    # -----------------------------
    # DELETE OLD LOGS (7 DAYS)
    # -----------------------------
    def delete_old_logs(self, days=7):
        if not os.path.exists(self.log_file):
            return

        cutoff_time = datetime.now() - timedelta(days=days)
        updated_lines = []

        with open(self.log_file, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    # extract timestamp safely
                    timestamp_str = line.split("]")[0][1:]
                    log_time = datetime.strptime(
                        timestamp_str, "%Y-%m-%d %H:%M:%S"
                    )

                    if log_time >= cutoff_time:
                        updated_lines.append(line)

                except:
                    continue

        with open(self.log_file, "w", encoding="utf-8") as f:
            f.writelines(updated_lines)


# -----------------------------
# LOAD LOGS FROM FILE
# -----------------------------
def load_logs():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(BASE_DIR, "data", "logs.txt")

    logs_by_date = {}

    if not os.path.exists(file_path):
        return logs_by_date

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                date = line.split("(")[1].split(")")[0]
                role = line.split(") ")[1].split(":")[0]
                content = line.split(": ", 1)[1].strip()

                logs_by_date.setdefault(date, []).append({
                    "role": role,
                    "content": content
                })

            except:
                continue

    return logs_by_date