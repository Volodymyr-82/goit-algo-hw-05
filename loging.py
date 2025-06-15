import sys
import os
from collections import defaultdict

def parse_log_line(line):
    parts = line.strip().split()
    if len(parts) < 4:
        return None  
    date, time, level = parts[0], parts[1], parts[2]
    message = " ".join(parts[3:])
    return {"date": date, "time": time, "level": level.upper(), "message": message}

def load_logs(file_path):
    
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"[Помилка] Файл не знайдено: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"[Помилка] Під час читання файлу сталася помилка: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs, level):
    level = level.upper()
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs):
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return dict(counts)

def display_log_counts(counts):
  
    print("\n Статистика логів за рівнями:")
    print("+------------+--------+")
    print("| Рівень     | Кількість |")
    print("+------------+--------+")
    for level in sorted(counts.keys()):
        print(f"| {level:<10} | {counts[level]:>8} |")
    print("+------------+--------+")


def display_logs(logs: list):
    if not logs:
        print("Жодного запису не знайдено.")
        return
    print(f"\n Записи рівня {logs[0]['level']}:")
    for log in logs:
        print(f"{log['date']} {log['time']} {log['level']} {log['message']}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python log_analyzer.py <шлях_до_файлу> [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)

    if level:
        filtered = filter_logs_by_level(logs, level)
        display_logs(filtered)
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)


if __name__ == "__main__":
    main()