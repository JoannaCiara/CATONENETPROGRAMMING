import socket
import threading

def handle_request(data, addr, server_socket):
    print(f"[+] Received message from {addr}: {data.decode()}")
    response = f"UDP Server received your message: {data.decode()}"
    server_socket.sendto(response.encode(), addr)

def start_udp_server():
    # SOCK_DGRAM specifies that this is a UDP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('0.0.0.0', 9998))
    print("[*] UDP Server listening on port 9998...")

    while True:
        # recvfrom returns the data AND the address of the sender
        data, addr = server.recvfrom(1024)
        # Even though UDP is connectionless, we use threads to process 
        # multiple incoming packets concurrently for Part A requirements.
        thread = threading.Thread(target=handle_request, args=(data, addr, server))
        thread.start()

if __name__ == "__main__":
    start_udp_server()
