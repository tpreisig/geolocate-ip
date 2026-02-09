
def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org/?format=json")
        response.raise_for_status()
        return response.json()["ip"]
    except Exception as e:
        return f"Error: {e}"
