from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
driver.get("https://jqueryui.com/datepicker/")

framewar=driver.find_element_by_xpath("//iframe[@class='demo-frame']")
driver.switch_to_frame(framewar)

driver.find_element_by_id("datepicker").click()

month=driver.find_element_by_class_name("ui-datepicker-month")
S1=Select(month)
S1.select_by_visible_text("Mar")

Year=driver.find_element_by_class_name("ui-datepicker-year")
S1=Select(Year)
S1.select_by_visible_text("2010")

driver.find_element_by_xpath("//a[text()='17']").click()













