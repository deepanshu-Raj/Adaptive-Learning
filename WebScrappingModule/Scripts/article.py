from selenium import webdriver
import GoogleSearch as gs

driver = webdriver.Chrome(executable_path = r"D:\webDrivers\chromedriver.exe")
driver.implicitly_wait(20)
driver.maximize_window()
file = open("Articles/articles.txt", 'w', encoding='utf-8')

google = gs.GoogleSearchQuestion(driver,file)

questions = []
questions.append("Python Tutorial")

for q in questions:
    var = google.run(q,0)

driver.close()
driver.quit()