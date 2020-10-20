from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:

    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        usernameInput = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)
    
    def saveInfo(self):
        saveInfo = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/section/div/button").click()  
        time.sleep(2)
    
    def getFollowers(self, max):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"First Count: {followerCount}")

        action = webdriver.ActionChains(self.browser)

        while followerCount < max:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(0.4)

            newCount = len(dialog.find_elements_by_css_selector("li"))
            
            if followerCount != newCount:
                followerCount = newCount
                print(f"Second Count: {newCount}")
                time.sleep(1)
            else:
                break

        followers = dialog.find_elements_by_css_selector("li")

        followerList =  []
        i = 0
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followerList.append(link)
            i += 1
            if i == max:
                break

        with open("followers.txt", "w", encoding="utf-8") as file:
            for item in followerList:
                file.write(item + "\n")

    def followUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text != "Message":
            followButton.click()
            time.sleep(2)
        else:
            print(f"Kullanıcı zaten takip ediyorsunuz. {username}")

    def unFollowUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text == "Message":
            unFollowButton = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button")
            unFollowButton.click()
            time.sleep(2)
            self.browser.find_element_by_xpath('//button[text()="Unfollow"]').click()
        else:
            print('Zaten takip etmiyorsunuz.')

instagram = Instagram(username,password)
instagram.signIn()
instagram.saveInfo()
instagram.getFollowers(50)

# list = {"kod_evreni","kodevreni2","kodluyoruz"}

# for user in list:
#     instagram.followUser(user)
#     time.sleep(3)

# instagram.unFollowUser('kod_evreni')