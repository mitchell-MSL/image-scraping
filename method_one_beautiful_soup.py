import requests
from bs4 import BeautifulSoup
import urllib
import os

# Replace the following url with any url of your choice, 
# or run the code to see what happens.
url = "https://toughpigs.com/photos-inhospitable/"

# Replace the following folder name with one that
# exists on your computer or create a 
# new folder with the same name "muppet_scrape"
folder_name = "muppet_scrape"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
img_tags = soup.find_all("img")

# Extract the image URLs
image_urls = [img["src"] for img in img_tags]

# Download the images
for url in image_urls:
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        filename = url.split("/")[-1]

        # Save the image to the folder
        filepath = os.path.join(folder_name, filename)
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded image: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image from {url}: {e}")