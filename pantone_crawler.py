from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle

# Setting up the browser (with adblock!)
chrome_path = r'C:\xampp\htdocs\collections\chromedriver.exe'

# Get adblock extension working
ad_block_path = r'C:\xampp\htdocs\collections\1.11.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + ad_block_path)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()

url_base = "http://rgb.to/pantone/coated/page/"
rgb_to_pantone = {}

for j in range(0, 18):
    # get the paginated URL
    url = url_base + str(j + 1)
    driver.get(url)
    # get all swatches
    swatches = driver.find_elements_by_css_selector(".swatch.pantone")

    for i, swatch in enumerate(swatches):
        # Extract the swatches background color (as rgb)
        bgstr = swatch.get_attribute("style")
        rgb = bgstr[16:-2]
        # Extract the swatches name text
        text = swatch.find_element_by_css_selector("a").text
        name = text[15:]
        rgb_to_pantone[rgb] = name

driver.quit()
# Save out the finished dictionary of rgb : name pairs   
fn = "rgb_to_pantone.p"
pickle.dump(rgb_to_pantone, open(fn, "wb"))
