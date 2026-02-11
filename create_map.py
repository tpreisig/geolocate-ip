import folium


def get_map(location: dict):
    if not location["lat_long"][0] or not location["lat_long"][1]:
        print("No lat/long available for mapping.")
        return
    
    lat, lon = float(location["lat_long"][0]), float(location["lat_long"][1])  # Convert to floats here
    
    # Create a folium map centered on the location
    m = folium.Map(location=[lat, lon], zoom_start=10)  # Zoom level 10 shows city-level detail
    
    # Add a marker with popup info
    popup_text = f"IP: {location['ip']}<br>City: {location['city']}<br>Region: {location['region']}<br>Country: {location['country']}"
    folium.Marker(
        [lat, lon],
        popup=popup_text,
        tooltip="Click for details"
    ).add_to(m)
    
    # Save to HTML file (open in browser for interactivity)
    m.save("ip_map.html")
    print(f"A map was created for position {lat:.4f}°N {lon:.4f}°E and saved as ip_map.html") 