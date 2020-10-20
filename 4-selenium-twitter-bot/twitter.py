from twitterUserInfo import username, password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept.languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")
        passwordInput = self.browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def theMostPopular(self):
        theMostPopular = self.browser.find_element_by_xpath("//div[@data-testid='trend']")
        theMostPopular.click()
        time.sleep(2)

        results = []

        list = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]")
        time.sleep(2)
        print('Count: '+ str(len(list)))

        for i in list:
            results.append(i.text)

        loopCounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")

        while True:
            if loopCounter > 10:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter += 1

            list = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]")
            time.sleep(2)
            print('Count: '+ str(len(list)))

            for i in list:
                results.append(i.text)

        count = 1
        with open("theMostPopular.txt","w",encoding="utf-8") as file:
            for item in results:
                file.write(f"{count}. {item}\n{'*'*50}\n")
                count+=1

    def search(self, hashtag):
        searchInput = self.browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

        results = []

        list = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]")
        time.sleep(3)
        print('Yüklenen tweet sayısı: '+ str(len(list)))

        for i in list:
            results.append(i.text)

        loopCounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")

        while True:
            
            if loopCounter >= 10:
                print('Loop tamamlandı.')
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(4)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                print('Sayfanın sonuna ulaştınız. Daha fazla içerik yok.')
                break
            last_height = new_height
            loopCounter += 1

            list = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]")
            time.sleep(3)

            for i in list:
                try:
                    results.append(i.text)
                except:
                    pass
                    print('Yüklenemedi.')
            print('Count: '+ str(len(list)))
    
        print('Toplam yüklenen tweet sayısı:',len(results))
        self.browser.close()

        count = 1
        with open("tweets.txt","w",encoding="utf-8") as file:
            for item in results:
                file.write(f"{count}. {item}\n{'*'*50}\n")
                count+=1

        # count = 1
        # for item in results:
        #     print(f"{count}. {item}")
        #     count += 1
        #     print("*"*50)

twitter = Twitter(username, password)
twitter.signIn()
twitter.search("python")
# twitter.theMostPopular()