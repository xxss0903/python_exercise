from selenium import webdriver

bro = webdriver.Chrome()
bro.get("http://www.baidu.com/")
txt = bro.find_element_by_id("kw")
txt.clear()
txt.send_keys(u"fan")
btn = bro.find_element_by_id("su")
btn.click()