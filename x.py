"""make battle plot maps"""
import folium
from folium import Marker
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import requests
from bs4 import BeautifulSoup  # For HTML parsing


def get_battle_data(url):
    """
    Extracts battle data (name and location) from a Wikipedia article URL.

    Args:
        url: The URL of the Wikipedia article.

    Returns:
        A list of dictionaries containing battle data.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Identify table containing battles (adjust selectors as needed)
    battle_table = soup.find("table", class_="wikitable sortable")
    if not battle_table:
        print(f"Warning: Battle table not found in {url}")
        return []

    battles = []
    for row in battle_table.find_all("tr")[1:]:  # Skip header row
        cells = row.find_all("td")
        if len(cells) >= 2:  # Ensure name and location cells exist
            battles.append(
                {"Name": cells[0].text.strip(), "Location": cells[1].text.strip()}
            )
    return battles


# Wikipedia article URLs for each war period (replace with actual URLs)
war_urls = {
    "War of Independence": "https://en.wikipedia.org/wiki/List_of_battles_in_the_Irish_War_of_Independence",
    "Civil War": "https://en.wikipedia.org/wiki/List_of_battles_in_the_Irish_Civil_War",
}

# Collect battle data for each war period
battles = {}
for war, url in war_urls.items():
    battles[war] = get_battle_data(url)

# Set map center coordinates (replace with Ireland coordinates)
latitude = 53.4129
longitude = -8.1436

# Create base map
m = folium.Map(location=[latitude, longitude], zoom_start=5)


# Function to animate markers
def animate(frame):
    m.clear_layers()  # Clear previous markers
    war = list(battles.keys())[frame]  # Get current war based on frame
    for battle in battles[war]:
        try:
            # Extract latitude and longitude from location string (adjust based on format)
            location_parts = battle["Location"].split(",")
            latitude = float(location_parts[0].strip())
            longitude = float(location_parts[1].strip())
        except ValueError:
            print(f"Warning: Invalid location format for {battle['Name']}")
            continue
        marker = Marker([latitude, longitude])
        marker.add_to(m)
    return m


# Create animation object
anim = FuncAnimation(
    plt.figure(figsize=(8, 6)), animate, frames=len(battles), interval=1000
)

# Save animation as MP4 (replace filename)
anim.save("irish_battles.mp4", fps=1)

# Display animation (optional)
plt.show()
