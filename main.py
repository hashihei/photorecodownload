#
# Copyright <2020> <hashihei>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

#
# Import library
#
import datetime
import sys
import os
from pathlib import Path
import logging
import traceback
import argparse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

# import orig Class and Functions
import config_reader

#
# logging setting.
#
LOGGING_FILE = ""


#WorkDir
WORKDIR = str(Path.cwd())
FOLDER_SIG = os.path.sep

#
# FTPS Conf file
#
CONFIG_FILE = WORKDIR + FOLDER_SIG + 'etc' + FOLDER_SIG + 'login.conf'

#
# define for this program function. 
#
def get_auth_info():

    LOGIN_URL = config_reader.get_LOGIN_URL()
    ACCOUNT = config_reader.get_USER()
    PASSWORD = config_reader.get_PASS()
    NUMBER_OF_SHEETS = config_reader.get_NOS()

    return LOGIN_URL, ACCOUNT, PASSWORD, NUMBER_OF_SHEETS

#
#login
#
def web_login(webdriver, URL, USER, PASS):
    #open login page
    webdriver.get(URL)

    #get form
    inputbox_id = driver.find_element_by_id('loginAccount')
    inputbox_password = driver.find_element_by_id('loginPass')
    login_button = driver.find_element_by_class_name('btnLogin')

    #set form value
    inputbox_id.send_keys(USER)
    inputbox_password.send_keys(PASS)

    #login
    login_button.click()

    return webdriver

if __name__ == '__main__':

    #
    #logging
    #
    LOGGING_FILE = config_reader.get_LOG_FILE(CONFIG_FILE)
    LOGGING_LEVEL = config_reader.get_LOG_LEVEL(CONFIG_FILE)

    logging.basicConfig(filename=LOGGING_FILE, level=logging.DEBUG)
    #console output message level is info.
    #default(file) message level is debug.
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-20s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    #main module logger
    logger_main = logging.getLogger(__name__)

    logger_main.info('%s program start.', datetime.datetime.now())

    #load setting
    URL, ACCOUNT, PASSWORD, NUMBER_OF_SHEETS = get_auth_info()
    
    #
    # web
    #

    #Open browser
    driver = webdriver.Chrome()

    # Seeting of Timeout
    wait = WebDriverWait(driver, 10)
    
    # load login info.
    driver = web_login(driver, URL, ACCOUNT, PASSWORD)
    logger_main.info('%s login complete.', datetime.datetime.now())

    #open album
    album = driver.find_element_by_class_name('bgWrap')
    album.click()
    time.sleep(3)

    #download image
    for i in range(1,int(NUMBER_OF_SHEETS)+1,1):
        btn_name = "btnDL_on" + str(i)
        download_btn = driver.find_element_by_id(btn_name)
        download_btn.click()

    logger_main.info('%s %s program end. ', datetime.datetime.now(), sys._getframe().f_code.co_name)
                
