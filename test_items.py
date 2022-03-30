from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_exists(browser):
    browser.get(link)
    assert EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")), "'Add to basket' button doesn't exist"