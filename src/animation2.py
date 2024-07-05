import folium
from folium import Marker
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

# Sample list of battles (replace with your actual data)
battles = [
    {"Name": "Battle of Kilmichael", "Latitude": 51.8333, "Longitude": -8.3333},
    {"Name": "Ambush at Kilmeena", "Latitude": 54.0833, "Longitude": -9.1667},
    {"Name": "Four Courts Battle", "Latitude": 53.3478, "Longitude": -6.2797},
]

# Set map center coordinates (Ireland)
latitude = 53.4129
longitude = -8.1436

# Create base map
m = folium.Map(location=[latitude, longitude], zoom_start=6)


# Function to animate markers
def animate(frame):
    m.clear_layers()  # Clear previous markers
    marker = Marker([battles[frame]["Latitude"], battles[frame]["Longitude"]])
    marker.add_to(m)
    return m


# Create animation object
anim = FuncAnimation(
    plt.figure(figsize=(8, 6)), animate, frames=len(battles), interval=1000
)

# Save animation as MP4 (replace filename)
anim.save("irish_battles_animation.mp4", fps=1)

# Display animation (optional)
plt.show()
