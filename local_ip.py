
import socket

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print(f"Your local IP address: {get_local_ip()}")
    
    
    
    
    