from selenium import webdriver

class GoogleSearchQuestion():
    def __init__(self,driver,file):
        self.driver = driver
        self.file = file
        self.var1=0
    def run(self,s,variable):
        self.var=0
        self.var1 = variable
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys(s)
        self.driver.find_element_by_name("q").send_keys(u'\ue007')
        try:
            text_box = self.driver.find_element_by_class_name("e24Kjd")
            text = text_box.text
            print(text,file= self.file)
        except:
            pass

        results = self.driver.find_elements_by_css_selector('div.g')
        print(len(results))
        for i in range(len(results)):
            link = results[i].find_element_by_tag_name("a")
            href = link.get_attribute("href")
            print(href,file=self.file)
            print(href)
        
        return self.var1+1
    def close(self):
        self.driver.close()
        self.driver.quit()