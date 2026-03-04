import subprocess

def monitor():
    # Checks if nginx is active using systemctl
    check = subprocess.run(['systemctl', 'is-active', 'nginx'], capture_output=True, text=True)
    status = check.stdout.strip()
    
    if status == "active":
        print(f"[*] SUCCESS: Nginx background process is {status}.")
    else:
        print(f"[!] ALERT: Nginx process is {status}!")

if __name__ == "__main__":
    monitor()
