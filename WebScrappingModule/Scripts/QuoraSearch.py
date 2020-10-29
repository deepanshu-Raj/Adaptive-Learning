from selenium import webdriver
import time
import cv2 as cv

class QuoraSearchQuestion():
    def __init__(self,driver,file):
        self.driver = driver
        self.file = file
        self.var1=0
    def run(self,s,variable):
        self.var=0
        self.var1 = variable
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys(s+" quora")
        self.driver.find_element_by_name("q").send_keys(u'\ue007')
        try:
            text_box = self.driver.find_element_by_class_name("e24Kjd")
            text = text_box.text
            print(text,file= self.file)
        except:
            pass
        self.driver.find_element_by_partial_link_text('Quora').click()

        buttons = self.driver.find_elements_by_class_name('ui_button_label')
        for i in buttons:
            i.click()
        time.sleep(10)
        paragraphs = self.driver.find_elements_by_tag_name('p')
        print(len(paragraphs))
        for i in paragraphs:
            text = i.get_attribute("textContent")
            print(text,file=self.file)
            # print(text)
            self.driver.implicitly_wait(2000)
        images = self.driver.find_elements_by_tag_name('img')
        for i in images :
            try:
                i.screenshot('Answers/img'+str(self.var1)+'-'+str(self.var)+'.png')
                img = cv.imread('Answers/img'+str(self.var1)+'-'+str(self.var)+'.png',1)
                w = img.shape[0]
                h = img.shape[1]
                if w<50 or h<50 :
                    os.remove('Answers/img'+str(self.var1)+'-'+str(self.var)+'.png')
                else:
                    self.var = self.var+1
            except:
                pass
        return self.var1+1
    def close(self):
        self.driver.close()
        self.driver.quit()