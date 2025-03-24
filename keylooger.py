import psutil
import pygetwindow as gw
import winreg

# List of suspicious process names (expand as needed)
SUSPICIOUS_PROCESSES = ["keylogger.exe", "logger.exe", "hooker.exe"]

# Function to check running processes
def detect_suspicious_processes():
    for process in psutil.process_iter(['pid', 'name']):
        try:
            if any(proc in process.info['name'].lower() for proc in SUSPICIOUS_PROCESSES):
                print(f"[ALERT] Suspicious process detected: {process.info['name']} (PID: {process.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

# Function to check registry for suspicious entries (Windows only)
def detect_registry_keyloggers():
    suspicious_keys = [
        r"Software\Microsoft\Windows\CurrentVersion\Run",  # Common autostart location
        r"Software\Microsoft\Windows\CurrentVersion\RunOnce"
    ]
    
    for key in suspicious_keys:
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key) as reg_key:
                i = 0
                while True:
                    try:
                        value = winreg.EnumValue(reg_key, i)
                        if any(proc in value[1].lower() for proc in SUSPICIOUS_PROCESSES):
                            print(f"[ALERT] Suspicious registry entry found: {value[0]} -> {value[1]}")
                    except OSError:
                        break
                    i += 1
        except FileNotFoundError:
            pass

# Run detection
detect_suspicious_processes()
detect_registry_keyloggers()
