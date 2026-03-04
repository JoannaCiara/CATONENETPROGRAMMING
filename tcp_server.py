import socket
import threading

def handle_client(client_socket, address):
    print(f"[+] New connection from {address}")
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"[*] Received from {address}: {data.decode()}")
            client_socket.send("Message received!".encode())
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        client_socket.close()
        print(f"[-] Connection closed from {address}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999)) # Binds to all interfaces on port 9999
    server.listen(5)
    print("[*] Multithreaded TCP Server listening on port 9999...")

    while True:
        client_sock, addr = server.accept()
        # Create a new thread for every client connection
        client_handler = threading.Thread(target=handle_client, args=(client_sock, addr))
        client_handler.start()

if __name__ == "__main__":
    start_server()
