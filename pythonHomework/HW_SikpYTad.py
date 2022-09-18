# 操作 browser 的 API
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# 處理逾時例外的工具
from selenium.common.exceptions import TimeoutException
# 面對動態網頁，等待某個元素出現的工具，通常與 exptected_conditions 搭配
from selenium.webdriver.support.ui import WebDriverWait
# 搭配 WebDriverWait 使用，對元素狀態的一種期待條件，若條件發生，則等待結束，往下一行執行
from selenium.webdriver.support import expected_conditions as EC
# 期待元素出現要透過什麼方式指定，通常與 EC、WebDriverWait 一起使用
from selenium.webdriver.common.by import By
# 操控鍵盤滑鼠
import pyautogui
# 強制等待 (執行期間休息一下)
from time import sleep

# 啟動瀏覽器工具的選項
my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")                #不開啟實體瀏覽器背景執行
my_options.add_argument("--start-maximized")         #最大化視窗
my_options.add_argument("--incognito")               #開啟無痕模式
my_options.add_argument("--disable-popup-blocking") #禁用彈出攔截
my_options.add_argument("--disable-notifications")  #取消通知
my_options.add_argument("--lang=zh-TW")  #設定為正體中文

# 使用 Chrome 的 WebDriver
def openChrome():
    driver = webdriver.Chrome(
        options = my_options,
        service = Service(ChromeDriverManager().install())
    )

# 前往頁面
def visit():
    driver.get('https://www.youtube.com/')
# 輸入關鍵字
def search():
    # 輸入
    txtInput = driver.find_element(By.CSS_SELECTOR, 'input#search')
    # 百變怪之歌
    search = 'metamon song'
    txtInput.send_keys(search)
    sleep(1) # 等待假裝輸入時間
    # 送出表單
    txtInput.submit()
    sleep(2)

# 點第一支影片
def pick1st():
    try:
        # 等待影片出現
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a#thumbnail')))
        # 移動到第一支影片點一下
        pyautogui.click(700,300,1)
        sleep(1)
    except TimeoutException:
        print('等候逾時')

# 找到一樣的封面圖點下去
def clickPic():
    tn = pyautogui.locateOnScreen('clickPic.jpg',confidence = 0.8)
    tnMid = pyautogui.center(tn)
    pyautogui.click(pyautogui.center(tn))

# 圖片相似度信心指數
tn = pyautogui.locateOnScreen('clickPic.png',confidence = 0.9)
tnMid = pyautogui.center(tn)

# 略過廣告
def skipAd():
    try:
        # 等待影片出現
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.ytp-ad-skip-button.ytp-button')))
        driver.find_element(By.CSS_SELECTOR,"button.ytp-ad-skip-button.ytp-button").click()
        sleep(1)
    except TimeoutException:
        # print('沒廣告，賺爛了')
        sleep(0)

'''主程式'''
# 只執行自己的 main 方法 (不執行函式的 print 之類的)
if __name__ == "__main__": 
    openChrome()
    visit()
    search()
    pick1st()
    clickPic()
    skipAd()

# 等確定擷取流程結束後，再關閉瀏覽器，以便 debug
driver.quit()


    