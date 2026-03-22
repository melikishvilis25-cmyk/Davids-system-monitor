import os
import time
import psutil


try:
    import gpustat
    GPU_AVAILABLE = True
except ImportError:
    GPU_AVAILABLE = False



RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_disk_path():
    return "C:\\" if os.name == "nt" else "/"


def usage_bar(percent, length=25):
    filled = int(length * percent // 100)
    empty = length - filled

    if percent <= 50:
        color = GREEN
    elif percent <= 80:
        color = YELLOW
    else:
        color = RED

    bar = f"{color}{'█' * filled}{RESET}{'-' * empty}"
    return f"{bar} {percent:5.1f}%"



def get_system_stats():
    stats = {
        "cpu": psutil.cpu_percent(interval=0.5),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage(get_disk_path()).percent,
        "gpus": []
    }

    if GPU_AVAILABLE:
        try:
            gpus = gpustat.new_query()
            for gpu in gpus:
                stats["gpus"].append({
                    "index": gpu.index,
                    "temp": gpu.temperature,
                    "usage": gpu.utilization or 0
                })
        except Exception:
            stats["gpus"] = []

    return stats



def render(stats):
    print("=== DAVID'S SYSTEM MONITOR ===")
    print("-" * 40)

    print(f"CPU   | {usage_bar(stats['cpu'])}")
    print(f"RAM   | {usage_bar(stats['ram'])}")
    print(f"Disk  | {usage_bar(stats['disk'])}")

    print("\n--- GPU ---")
    if stats["gpus"]:
        for gpu in stats["gpus"]:
            print(
                f"GPU {gpu['index']} | "
                f"Temp: {gpu['temp']}°C | "
                f"Usage: {usage_bar(gpu['usage'])}"
            )
    else:
        print("No GPU data available")

    print("\nPress CTRL+C to stop")



def main():
    try:
        while True:
            stats = get_system_stats()
            clear_screen()
            render(stats)
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


if __name__ == "__main__":
    main()
