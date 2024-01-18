from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.amazon.com/KOORUI-Inch-Computer-Monitor-Ultra-Thin/dp/B0C4DNVG5H?pf_rd_r=SY8QBX51ANWMPE7J87YY&pf_rd_t=Events&pf_rd_i=deals&pf_rd_p=2364d0f5-5054-4700-a4e8-74a53fead388&pf_rd_s=slot-14&ref=dlx_deals_gd_dcl_img_6_46db9c7a_dt_sl14_88"
)

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"${price_dollar.text}.{price_cents.text}")


# driver.close()
driver.quit()
