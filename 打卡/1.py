from selenium import webdriver

url = 'https://www.wjx.cn/vj/exuVsAI.aspx'

# 对智能测试 进行反爬
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
# 设置无界面  可选
# option = webdriver.ChromeOptions()
# option.add_argument('--headless')

browser = webdriver.Chrome(options=option)
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
})


browser.get(url)
user_name = "胡澳治"
user_num = "201900800510"
user_house = "江西省九江市修水县万象新城B区1301"
user_tmp = '36.5'
user_name_input = browser.find_element_by_id("q1")
user_name_input.send_keys(user_name)

user_num_input = browser.find_element_by_id("q2")
user_num_input.send_keys(user_num)

user_speciality_radio = browser.find_element_by_xpath('//*[@id="divquestion3"]/ul/li[6]/a')
browser.execute_script("arguments[0].click();", user_speciality_radio)
# user_speciality_radio.click()

user_condition_check = browser.find_element_by_xpath('//*[@id="divquestion4"]/ul/li[5]/a')
user_condition_check.click()

user_house_input = browser.find_element_by_id("q5")
user_house_input.send_keys(user_house)

user_green_radio = browser.find_element_by_xpath('//*[@id="divquestion6"]/ul/li[2]/a')
user_green_radio.click()

user_temperature_input = browser.find_element_by_id('q7')
user_temperature_input.send_keys(user_tmp)

user_outgoing_input = browser.find_element_by_xpath('//*[@id="divquestion8"]/ul/li[1]/a')
user_outgoing_input.click()


submit = browser.find_element_by_xpath('//*[@id="submit_button"]')
submit.click()

# 模拟点击智能验证按钮
# 先点确认
browser.find_element_by_xpath("//button[text()='确认']").click()
# 再点智能验证提示框，进行智能验证
browser.find_element_by_xpath("//div[@id='captcha']").click()
