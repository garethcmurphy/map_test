import streamlit as st
import folium
from folium.features import CircleMarker

# Define your data (replace with your actual data)
data = {
    "Latitude": [51.505, 48.8566, 40.7128],
    "Longitude": [-0.09, 2.3522, -74.0059],
    "Names": ["London", "Paris", "New York City"]
}

# Create a base map centered on a certain location (adjust as needed)
m = folium.Map(location=[48.8566, 2.3522], zoom_start=3)  # Centered on Paris

# Iterate through data and add markers with popups
for i in range(len(data["Latitude"])):
  latitude = data["Latitude"][i]
  longitude = data["Longitude"][i]
  name = data["Names"][i]
  marker = CircleMarker(location=[latitude, longitude], radius=5, popup=name, color='red')  # Adjust marker size and color
  marker.add_to(m)

# Add map to Streamlit app
st.title("Map with Points")
st.folium_map(m)
