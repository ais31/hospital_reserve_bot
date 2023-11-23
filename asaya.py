from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def HihukaYoyaku():
    try:
        driver = webdriver.Chrome()
        # driver.get('https://www.google.co.jp/')


        driver.get('https://sv01.e-junban.com/asaya/asaya1/')

        # 順番取りをクリック
        elem = driver.find_element(By.XPATH,'//*[@id="Tori_J"]/li/a')

        elem.click()

        time.sleep(5)

        #診察券番号入力
        
        form_sinsatu = driver.find_element(By.XPATH,'//*[@id="middle"]/form/input[1]')
        form_sinsatu.send_keys('XXXXXXX')

    #電話番号入力
        form_tel = driver.find_element(By.XPATH,'//*[@id="middle"]/form/input[5]')
        form_tel.send_keys('XXX-XXXX-XXXX')

    # 予約ボタンクリック
        yoyaku = driver.find_element(By.XPATH,'//*[@id="bt_area"]/input')
        yoyaku.click()

    #予約番号返却
        bangou = driver.find_element(By.XPATH, '//*[@id="middle"]/p/font[1]/strong')
        print(bangou.text)

        yoyakuNo = bangou.text
        time.sleep(10)

        driver.quit()

        return yoyakuNo
    
    except:
        print("error")
        res='予約に失敗しました'
        return res



def zyunban():
    try:
        driver = webdriver.Chrome()

        driver.get('https://sv01.e-junban.com/asaya/asaya1/')

        # 順番待ちを見るをクリック
        elem = driver.find_element(By.XPATH,'//*[@id="Machi_J"]/li/a')

        elem.click()
        time.sleep(5)
        num = []
        first_num = driver.find_element(By.XPATH,'//*[@id="middle"]/table/tbody/tr[2]/td[1]')
        fifth_num = driver.find_element(By.XPATH,'//*[@id="middle"]/table/tbody/tr[6]/td[1]')

        num.append(first_num.text)
        num.append(fifth_num.text)


        driver.quit()

        return num

    except:
        res = '順番取得に失敗しました'
        return res
    








