import time
import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumRpa:

  

    def open_browser(self, link):
        self.link = link
        opcoes = webdriver.ChromeOptions()
        opcoes.add_experimental_option('prefs', {
            'download.default_directory': 'src',
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            'plugins.always_open_pdf_externally': True
        })

        self.browser = webdriver.Chrome(
            executable_path=r'./chromedriver.exe',
            chrome_options=opcoes
        )

        try:
            self.browser.maximize_window()
            self.browser.get(self.link)
        except ValueError:
            raise ValueError


    def exemploWait(self):
        try:
            wait = WebDriverWait(self.browser, 50)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="XPATH"]')
            )).send_keys('string')


        except ValueError:
            raise ValueError

    