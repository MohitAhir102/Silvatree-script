# from selenium import webdriver

# driver = webdriver.Chrome(executable_path="chromedriver.exe")

# driver.get ("googlr.com")






from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Specify the path to your ChromeDriver executable
chrome_driver_path = "/Users/ztlab142/Documents/script/chromedriver.exe"

# Create a ChromeOptions object
chrome_options = webdriver.ChromeOptions()

# Initialize the Chrome driver with the specified executable path and options
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# Navigate to a website

driver.get("https://www.google.com")