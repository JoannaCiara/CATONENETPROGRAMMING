import socket

def start_client():
    # Use the Public IP of your VPS
    server_ip = "127.0.0.1" 
    server_port = 9999

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((server_ip, server_port))
        print(f"[*] Connected to {server_ip}:{server_port}")
        
        message = "Hello from Joan's Client!"
        client.send(message.encode())
        
        response = client.recv(1024)
        print(f"[*] Server says: {response.decode()}")
        
    except Exception as e:
        print(f"[!] Connection failed: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
