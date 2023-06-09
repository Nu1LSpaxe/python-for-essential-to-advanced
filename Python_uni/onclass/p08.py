from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()

driver.get('https://www.wikipedia.org/')

search_box = driver.find_element(By.NAME, 'search')
# search_box = driver.find_element(By.ID, 'searchInput')
search_box.send_keys('Python (programming language)')

search_box.send_keys(Keys.RETURN)

result = driver.find_element(By.CSS_SELECTOR, '#firstHeading > span')
print(result.text)

driver.quit()


# # 先導入我們需要的函式庫
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # 開一個新的 Edge 瀏覽器
# driver = webdriver.Edge()

# # 讓瀏覽器打開 Google 的網頁
# driver.get("http://www.google.com")

# # 利用名稱（NAME）找到搜索框，然後輸入 "Python"
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("Python")

# # 模擬按下 Enter 鍵
# search_box.send_keys(Keys.RETURN)

# # 等兩秒，讓瀏覽器有足夠的時間載入搜尋結果
# time.sleep(2)

# # 找到所有的搜尋結果標題，並印出
# results = driver.find_elements(By.CSS_SELECTOR, 'h3')
# #results = driver.find_elements(By.XPATH, '//div[@class="yuRUbf"]/a/h3')
# for result in results:
#     print(result.text)

# # 用完記得要關閉瀏覽器喔
# driver.quit()