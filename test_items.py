from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"


def test_checking_the_add_to_cart_button(browser):
    browser.get(link)
    element1 = browser.find_element(By.CSS_SELECTOR, 'a[tabindex="-1"]')
    element1.click()
    card = browser.find_element(By.CSS_SELECTOR, "a[title]")
    card.click()
    button = browser.find_elements(By.CSS_SELECTOR, "button.btn.btn-add-to-basket")
    assert button != [], 'Кнопка не найдена!'

    