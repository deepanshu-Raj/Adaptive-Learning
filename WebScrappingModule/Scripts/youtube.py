from selenium import webdriver
import YoutubeSearch as YS

driver = webdriver.Chrome(executable_path=r"D:\webDrivers\chromedriver.exe")
driver.implicitly_wait(20)
driver.maximize_window()

file = open("Videos/playlist.txt", 'w', encoding='utf-8')

youtube = YS.YoutubeSearchPlaylist(driver, file)

questions = []
questions.append("Web Development tutorials")

for i in questions:
    var = youtube.run(i,0)

driver.close()
driver.quit()