import pprint

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from settings import WEBSITE_URL
from selenium.webdriver.common.by import By
from time import sleep


class Parser:
    def __init__(self):
        options = Options()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options)
        self.list_of_links = []

    def parse_list_of_advs(self):
        self.driver.get(WEBSITE_URL)
        self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight)")
        list_of_ads = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[3]/div/ul"
        ).find_elements(By.CLASS_NAME, "minicard-item")
        for ad in list_of_ads:
            element = ad.find_element(
                By.CLASS_NAME, "title-link"
            )
            self.list_of_links.append(
                {
                    "link": element.get_attribute("href"),
                    "name": element.text
                }
            )
        pprint.pprint(self.list_of_links)
        for parse_link in self.list_of_links[:1]:
            number = self.get_number(parse_link.get("link"))
            parse_link["number"] = number
        return self.list_of_links

    def get_number(self, link):
        self.driver.get(link)
        sleep(5)
        try:
            number = self.driver.find_element(
                By.CLASS_NAME, "js-phone"
            ).find_element(
                By.CLASS_NAME, "js-phone-number"
            ).get_attribute("href").replace("tel:", "")
        except selenium.common.exceptions.NoSuchElementException:
            return
        return number

