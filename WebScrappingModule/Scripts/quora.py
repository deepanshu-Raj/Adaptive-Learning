from selenium import webdriver
import QuoraSearch as qu


driver = webdriver.Chrome(executable_path=r"D:\webDrivers\chromedriver.exe")
driver.implicitly_wait(20)
driver.maximize_window()
file = open("Answers/Answers.txt", 'w', encoding='utf-8')

quora = qu.QuoraSearchQuestion(driver,file)

questions = []
questions.append("What is Water Cycle?")

for i in questions:
    var = quora.run(i,0)

driver.close()
driver.quit()