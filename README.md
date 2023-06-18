# Image-scraping
Two methods of image scraping are used to download photos of muppets from the web. Method one uses Beutiful Soup, and method two uses selenium. If you are new to web-scraping and would like to use this notebook, you will need to install the following libraries.

**Method One Beautiful Soup:** 
- pip install requests 
- pip install beautifulsoup4

**Method Two Selenium:**
- pip install requests
- pip install selenium
- You will also have to install a Chrome driver for this method. The path I used for this driver can be seen in the method two file, but yours will be different. 
  - https://chromedriver.chromium.org/downloads
- For one of my scrapes an ad blocker was useful. You can find one on the chrome webstore.
  - https://chrome.google.com/webstore/category/extensions
 
**Method One Beautiful Soup:** 
- Pros
  - Quick way to download images from any link.
  - You should only have to change the link, and name of the target file.
- Cons
  - You are only able to scrape the page indicated.
  - You may get low resolution images like thumbnails since you can't click through.

**Method Two Selenium:**
I included two versions of Method two to show how much the code can change for different websites. This method of scraping involves interactions with the webpages, and every web page is different. It may take a bit longer to set this up to work for your usecase, but you got this!
- Pros
  - You can automate tasks that require interactions like scrolling, or clicking with the page.
  - This will help you scrape multiple pages of images.
- Cons
  - Not as simple to implement.
  - Every situation is different, and the code will need to be adapted.  

# Sources:
**Method One Beautiful Soup:**
1. How to Scrape and Download ALL images from a webpage -John Wattson Rooney with Python
    https://www.youtube.com/watch?v=stIxEKR7o-c
    https://github.com/jhnwr/image-downloader/blob/main/imagedownloader.py
3. Chat GPT was used to help address errors with downloading the images and tie it all together.
    https://chat.openai.com/
   

**Method Two Selenium:**
1. How To Web Scrape & Download Images With Python - Tech with Tim
   https://www.youtube.com/watch?v=NBuED2PivbY&t=1s
   https://github.com/techwithtim/Image-Scraper-And-Downloader/blob/main/tutorial.py
2. 3. Chat GPT was very useful for addressing errors with StaleElementReferenceException, in method_2_different_site.py
