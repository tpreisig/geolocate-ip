import json
from public_ip import get_public_ip
from geolocate import geolocate_ip
from create_map import get_map

    
if __name__ == '__main__':
    ip = get_public_ip()
    print(f"Public IP address is {ip}")
    print("Geolocation data:")
    geo_data = geolocate_ip(ip)
    print(json.dumps(geo_data, indent=2))
    get_map(geo_data)
    print("➡️ Open it in a browser to check it out.")
    
