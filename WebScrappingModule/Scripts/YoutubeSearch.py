from selenium import webdriver
import time

class YoutubeSearchPlaylist:
    def __init__(self, driver, file):
        self.driver = driver
        self.file = file
        self.var1=0

    def run(self, s, variable):
        self.var = 0
        self.var1 = variable
        self.driver.get("https://www.youtube.com/")
        self.driver.find_element_by_name("search_query").click()
        self.driver.find_element_by_name("search_query").send_keys(s+" playlist")
        self.driver.find_element_by_id("search-icon-legacy").click()
        time.sleep(10)
        playlists = self.driver.find_elements_by_id("content")
        print(type(playlists))
        print(len(playlists))
        for i in range(len(playlists)):
            link = playlists[i].find_element_by_tag_name("a")
            href = link.get_attribute("href")
            print(href,file=self.file)
            print(href)
            
        return self.var1+1

    def close(self):
        self.driver.close()
        self.driver.quit()