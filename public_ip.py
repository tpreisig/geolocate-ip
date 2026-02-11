import requests
import socket


def get_public_ip() -> str:
    apis = [
        "https://api.ipify.org?format=json",
        "https://ipinfo.io/json",
        "https://ifconfig.me/ip"
    ]
    for url in apis:
        try:
            host = url.split('/')[2].split('?')[0]
            socket.gethostbyname(host)
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            if "json" in url:
                return response.json().get("ip")
            else:
                return response.text.strip()
        except (requests.RequestException, socket.gaierror) as e:
            print(f"Failed to fetch from {url}: {e}")
    raise ValueError("All APIs failed. Check your network/DNS.")
