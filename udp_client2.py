import socket

def start_udp_client():
    server_ip = "127.0.0.1"
    server_port = 9998
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        message = "Hello UDP Server from Joan 2!"
        client.sendto(message.encode(), (server_ip, server_port))
        
        # Buffer size is 1024 bytes
        data, addr = client.recvfrom(1024)
        print(f"[*] Server response: {data.decode()}")
    finally:
        client.close()

if __name__ == "__main__":
    start_udp_client()
