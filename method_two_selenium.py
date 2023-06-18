from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import requests

# Replace the following folder name with one that
# exists on your computer or create a new folder with the same name "muppet_scrape"
folder_name = "muppet_scrape"

# URL of the webpage with the slideshow
url = 'https://muppet.fandom.com/wiki/Behind_the_scenes_Henson_photos?file=Sam-friends-stills.jpg'

# webdriver path and activation
webdriver_path = '/Users/your/path/here'
service = Service(webdriver_path)
driver = webdriver.Chrome(webdriver_path)
driver.get(url)

# This section automates clicking next on the slideshow in our link,
# you can find the class_name by inspecting html in the browser
lightbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'WikiaLightbox')))
right_arrow = lightbox.find_element(By.CLASS_NAME, 'arrow.next')

# Set the desired number of images to scrape
num_images_to_scrape = 149
num_scraped_images = 0

while num_scraped_images < num_images_to_scrape:
    try:
        current_image = lightbox.find_element(By.TAG_NAME, 'img')
        image_url = current_image.get_attribute('src')

        # Download the image
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        filename = image_url.split("/")[-1]

        # Save files as .jpg
        if not filename.lower().endswith('.jpg'):
            filename += '.jpg'

        # Write to selected folder
        filepath = os.path.join(folder_name, filename)
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded image: {filename}")
        num_scraped_images += 1

        # Move to the next image
        ActionChains(driver).move_to_element(right_arrow).click().perform()
    except Exception as e:
        print(f"Error downloading image: {e}")
driver.quit()

