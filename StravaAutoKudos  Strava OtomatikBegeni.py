
import time
import os
from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument("--private")
# 'myprofile = webdriver.FirefoxProfile(r'C:\\Users\\Ogo\\PycharmProjects\\untitled\\ffuser')
driver = webdriver.Firefox(options=options, executable_path="geckodriver.exe")


# 10TANE KULÜBE KATILIN. KATILDIĞINIZ KULUPLERİN LİNKLERİNİ BURAYA YAPIŞTIRIN

url1 = "https://www.strava.com/clubs/286173/recent_activity"
url2 = "https://www.strava.com/clubs/285396/recent_activity"
url3 = "https://www.strava.com/clubs/160544/recent_activity"
url4 = "https://www.strava.com/clubs/39996/recent_activity"
url5 = "https://www.strava.com/clubs/114478/recent_activity"
url6 = "https://www.strava.com/clubs/570485/recent_activity"
url7 = "https://www.strava.com/clubs/730529/recent_activity"
url8 = "https://www.strava.com/clubs/596044/recent_activity"
url9 = "https://www.strava.com/clubs/527136/recent_activity"
url10 = "https://www.strava.com/clubs/52733/recent_activity"



driver.get('https://www.strava.com/login?cta=log-in&element=global-header&source=athletes_show')

#############İD SİFRENİZİ GİRİN.
driver.find_element_by_name("email").send_keys("GİRİS MAİL ADRESİNİ GİRİN ")
driver.find_element_by_name("password").send_keys("SİFRENİZİ BURRAYA YAZIN")

driver.find_element_by_id("login-button").click()



i = 0
while True:
    try:

        driver.get(url1)
        like = driver.find_elements_by_xpath(r'//button[@title="Give Kudos"]')
        for x in range(0, len(like)):
            if like[x].is_displayed():
                like[x].click()
                i += 1
                print(i)
        time.sleep(333)

        driver.get(url2)
        like = driver.find_elements_by_xpath(r'//button[@title="Give Kudos"]')
        for x in range(0, len(like)):
            if like[x].is_displayed():
                like[x].click()
                i += 1
                print(i)
        time.sleep(333)

        driver.get(url3)
        like = driver.find_elements_by_xpath(r'//button[@title="Give Kudos"]')
        for x in range(0, len(like)):
            if like[x].is_displayed():
                like[x].click()
                i += 1
                print(i)
        time.sleep(333)

        driver.get(url4)
        like = driver.find_elements_by_xpath(r'//button[@title="Give Kudos"]')
        for x in range(0, len(like)):
            if like[x].is_displayed():
                like[x].click()
                i += 1
                print(i)
        time.sleep(333)

        driver.get(url5)
        like = driver.find_elements_by_xpath(r'//button[@title="Give Kudos"]')
        for x in range(0, len(like)):
            if like[x].is_displayed():
                like[x].click()
                i += 1
                print(i)
        time.sleep(333)

        driver.get(url6)
        like = driver.find_elements_by_xpath(r'//button[@title="Give Kudos"]')
        for x in range(0, len(like)):
            if like[x].is_displayed():
                like[x].click()
                i += 1
                print(i)
        time.sleep(333)

        driver.get(url7)
        like = driver.find_elements_by_xpath(r'//button[@title="Give Kudos"]')
        for x in range(0, len(like)):
            if like[x].is_displayed():
                like[x].click()
                i += 1
                print(i)
        time.sleep(333)

        driver.get(url8)
        like = driver.find_elements_by_xpath(r'//button[@title="Give Kudos"]')
        for x in range(0, len(like)):
            if like[x].is_displayed():
                like[x].click()
                i += 1
                print(i)
        time.sleep(333)

        driver.get(url9)
        like = driver.find_elements_by_xpath(r'//button[@title="Give Kudos"]')
        for x in range(0, len(like)):
            if like[x].is_displayed():
                like[x].click()
                i += 1
                print(i)
        time.sleep(333)

        driver.get(url10)
        like = driver.find_elements_by_xpath(r'//button[@title="Give Kudos"]')
        for x in range(0, len(like)):
            if like[x].is_displayed():
                like[x].click()
                i += 1
                print(i)
        time.sleep(333)


    except:
        print("uwu")