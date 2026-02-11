import requests
from public_ip import get_public_ip

ip = get_public_ip()

def geolocate_ip(ip: str) -> dict:
    try:
        url = f"https://ipinfo.io/{ip}/json" 
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Extract key info (handle missing fields gracefully)
        location = {
            "ip": data.get("ip", ip),
            "city": data.get("city", "Unknown"),
            "region": data.get("region", "Unknown"),
            "country": data.get("country", "Unknown"),
            "lat_long": data.get("loc", "Unknown").split(",") if "loc" in data else [None, None]
        }
        return location
    except requests.RequestException as e:
        raise ValueError(f"Geolocation failed: {e}")
    
