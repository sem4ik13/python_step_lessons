import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button(browser):
	browser.get(link)
	button = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
	assert (button.is_enabled()), f"Button is not clickable"
	time.sleep(3)