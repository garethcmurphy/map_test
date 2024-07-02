import streamlit as st
import folium

# Define your data (replace with your actual data)
data = {
    "Latitude": [51.505, 48.8566, 40.7128],
    "Longitude": [-0.09, 2.3522, -74.0059],
    "Names": ["London", "Paris", "New York City"]
}

# Create a base map centered on a certain location (adjust as needed)
m = folium.Map(location=[48.8566, 2.3522], zoom_start=3)  # Centered on Paris

# Add markers using a loop
for i in range(len(data["Latitude"])):
  latitude = data["Latitude"][i]
  longitude = data["Longitude"][i]
  name = data["Names"][i]
  folium.Marker([latitude, longitude], popup=name, icon=folium.Icon(color='red')).add_to(m)  # CircleMarker or other icons

# Display the map in Streamlit
st.title("Map with Points")
map_html = m._repr_html_()
st.markdown(map_html, unsafe_allow_html=True)
