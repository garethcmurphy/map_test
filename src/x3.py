
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Define battle data (replace with your desired battle)
battle = {
  "Name": "Battle of Kilmichael",
  "Latitude": 51.8333,
  "Longitude": -8.3333
}

# Set map center coordinates (Ireland)
latitude = 53.4129
longitude = -8.1436

# Create figure and GeoAxes projection for world map
fig, ax = plt.subplots(figsize=(8, 6))
m = Basemap(projection='mill', llcrnrlat=40, urcrnrlat=70, llcrnrlon=-20, urcrnrlon=20, resolution='l')  # Adjust projection and extent as needed

# Fill continents and draw coastlines
m.fillcontinents(color='lightgray')
m.drawcoastlines()

# Convert battle coordinates to map projection coordinates
x, y = m(battle["Longitude"], battle["Latitude"])  

# Plot marker for the battle
ax.plot(x, y, 'ro', markersize=10)  # Red marker with size 10

# Optional: Add label for the battle
ax.text(x + 5000, y, battle["Name"], ha='center', va='center', fontsize=12)  # Adjust offset for label placement

# Remove axes (optional for cleaner map image)
plt.axis('off')
plt.title('')

# Save the figure as a PNG image
plt.savefig("irish_battle_map.png")

print("Map saved as irish_battle_map.png")
