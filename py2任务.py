# #企查查滑动
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# driver = webdriver.Chrome()
# ac = ActionChains(driver)
# driver.get("https://www.qcc.com/")
# driver.maximize_window()
# driver.find_element_by_link_text("登录 | 注册").click()
# time.sleep(5)
# ele = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")
# ac.click_and_hold(ele).move_by_offset(308,0).perform()
# time.sleep(10)
# driver.quit()

#苏宁买个东西
# driver.get("https://www.suning.com/")
# driver.maximize_window()
# driver.find_element_by_link_text("家用电器").click()
# data = driver.window_handles
# driver.switch_to.window(data[1])
# driver.find_element_by_link_text("电风扇").click()
# data = driver.window_handles
# driver.switch_to.window(data[2])
# driver.find_element_by_xpath("//*[@id='ssdsn_search_pro_baoguang-1-0-1_1_04:0000000000_12230773604']/img").click()
# data = driver.window_handles
# driver.switch_to.window(data[3])
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='addCart']").click()
# time.sleep(5)
# driver.quit()

# #京东买个东西
# driver.get("https://www.jd.com/")
# driver.maximize_window()
# driver.find_element_by_link_text("你好，请登录").click()
# driver.find_element_by_link_text("账户登录").click()
# driver.find_element_by_xpath("//*[@id='loginname']").send_keys("17603379853")
# driver.find_element_by_xpath("//*[@name='nloginpwd']").send_keys("admin123")
# driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
# time.sleep(10)
# driver.find_element_by_link_text("电脑").click()
# data = driver.window_handles
# driver.switch_to.window(data[1])
# driver.find_element_by_link_text("一体机").click()
# data = driver.window_handles
# driver.switch_to.window(data[2])
# driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[2]/div/div[1]/a/img").click()
# time.sleep(3)
# data = driver.window_handles
# driver.switch_to.window(data[3])
# driver.find_element_by_link_text("加入购物车").click()
# time.sleep(10)
# driver.quit()





# #前程贷！
# driver.get("http://8.129.91.152:8765/")
# driver.maximize_window()
# driver.find_element_by_link_text("免费注册").click()
# driver.find_element_by_xpath("//*[@name='phone']").send_keys("15335845369")
# time.sleep(15)
# driver.find_element_by_xpath("//*[@name='password']").send_keys("admin123")
# driver.find_element_by_xpath("//*[@name='agree']").click()
# driver.find_element_by_xpath("//*[@type='button']").click()
# time.sleep(5)
# driver.quit()