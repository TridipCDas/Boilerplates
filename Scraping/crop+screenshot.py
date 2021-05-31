"""
Useful for 2 jobs
1. Get complete screenshot of a site
2. Crop a section from a site given the two elements

"""
import re
import random
import PIL
from PIL import Image
from datetime import datetime
from selenium import webdriver

def configure_settings():
    """
    Configuring the settings for selenium.
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome('./chromedriver', chrome_options=options)
    return driver

def extract_moves_image(url,coordinates):
    """
    coordinates = A tuple containing the first element and second element
    """

    #NOTE: Below code might not be required or might change
    url = re.sub("ix\?doc=/","",url)
    driver = configure_settings()
    driver.implicitly_wait(random.randint(25, 30))
    driver.maximize_window()
    driver.get(url)

    #========================================================================
    all_texts= driver.find_element_by_xpath("/html/body").text
    counter =1

    while len(all_texts) <200 or len(all_texts) == 2920:
        driver.quit()
        driver = configure_settings()
        driver.implicitly_wait(random.randint(25, 30))
        driver.maximize_window()
        driver.get(url)
        all_texts= driver.find_element_by_xpath("/html/body").text
        counter = counter +1
        if counter == 9:
            break
    # len(all_texts) might change depending on url. Done so that all dynamic contents also get loaded up.
    #===================================================================================
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment  
    driver.find_element_by_tag_name('body').screenshot('fullpageShot.png') #NOTE: THis takes full screenshot the page
    
    
    body_element = driver.find_element_by_xpath("/html/body")

    #-----------------------------------------------------
    x1 = coordinates[0].location['x']-10
    y1 = coordinates[0].location['y']-10
    x2 = body_element.size['width']+3   #NOTE: This might change
    y2 = coordinates[1].location['y']-10
    # NOTE: Adjust this manually
    #-------------------------------------------------------

    image = Image.open('./fullpageShot.png')
    image = image.crop((x1,y1,x2,y2))
    
    #NOTE: Check te width manually
    fixed_width = 800
    width_percent = (fixed_width / float(image.size[0]))
    height_size = int((float(image.size[1]) * float(width_percent)))
    image = image.resize((fixed_width, height_size), PIL.Image.NEAREST)
    filename = f"{random.randint(10,99)}_{int(datetime.now().timestamp())}.png"
    savepath = f"/home/DiVmTestAdmin/TechVariable/assets/moves/{filename}"
    image.save(savepath)
    filename = 'https://directorintel.com/diassets/moves/' + filename
    
    driver.close()
    return filename