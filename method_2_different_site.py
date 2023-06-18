from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import os
import requests

# Replace the following folder name with one that
# exists on your computer or create a new folder with the same name "movie_scrape"
folder_name = "movie_scrape"

# URL of the webpage with the slideshow
url = 'https://fancaps.net/movies/Image.php?imageid=5719709'

# webdriver path, activation and ad-blocker
webdriver_path = '/Users/your/path/here'
service = Service(webdriver_path)
adblock_extension_path = '/Users/your/path/here'
chrome_options = Options()
chrome_options.add_extension(adblock_extension_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(url)

# Wait for the image holder to load
image_holder = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'img-holder')))
num_images_to_scrape = 2500
num_scraped_images = 0

while num_scraped_images < num_images_to_scrape:
    try:
        image = image_holder.find_element(By.TAG_NAME, 'img')
        image_url = image.get_attribute('src')

        # Save image as .jpg
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        filename = f"oz_pt2_image_{num_scraped_images + 1}.jpg"

        # Write to selected folder
        filepath = os.path.join(folder_name, filename)
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded image: {filename}")
        num_scraped_images += 1

        # Clicks next. You can find your class names
        # by inspecting html in your browser
        next_button = driver.find_element(By.CLASS_NAME, 'btn.btn-info.pull-right')
        ActionChains(driver).move_to_element(next_button).click().perform()

        # Wait for the image holder to refresh
        WebDriverWait(driver, 10).until(EC.staleness_of(image_holder))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'img-holder')))
        image_holder = driver.find_element(By.CLASS_NAME, 'img-holder')
    except StaleElementReferenceException:
        # Handle StaleElementReferenceException by waiting for the elements to reload properly
        image_holder = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'img-holder')))
        next_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn.btn-info.pull-right')))
    except Exception as e:
        print(f"Error downloading image: {e}")

# Close the browser
driver.quit()


