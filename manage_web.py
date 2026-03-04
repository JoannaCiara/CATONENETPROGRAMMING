import os

def restart_process():
    print("[*] Initiating restart of the Nginx web server...")
    # Using os.system to send a management command to the OS
    exit_code = os.system('sudo systemctl restart nginx')
    
    if exit_code == 0:
        print("[+] Nginx restarted successfully.")
    else:
        print("[-] Failed to restart Nginx.")

if __name__ == "__main__":
    restart_process()
