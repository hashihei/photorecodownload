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
import configparser
import datetime
import sys
import os
import logging
import traceback

SECTION1 = 'login'
SECTION2 = 'system'
FOLDER_SIG = os.path.sep
DEFAULT_CONF_PATH = 'etc' + FOLDER_SIG + 'login.conf'

#
# define for config read function.
#
def get_config_value(conf_path,get_value,SECTION=SECTION1):

    #read config.
    config = configparser.ConfigParser()
    config.read(conf_path)

    return_value = None

    #check section and option value.
    if config.has_section(SECTION):
        if config.has_option(SECTION, get_value):
            return_value = config.get(SECTION, get_value)

    return return_value
    

def get_NOS(conf_path=DEFAULT_CONF_PATH):

    #setting get value
    get_value = 'NOS'

    return get_config_value(conf_path, get_value)

def get_LOGIN_URL(conf_path=DEFAULT_CONF_PATH):

    #setting get value
    get_value = 'LOGIN_URL'

    return get_config_value(conf_path, get_value)

def get_USER(conf_path=DEFAULT_CONF_PATH):

    #setting get value
    get_value = 'USER'

    return get_config_value(conf_path, get_value)

def get_PASS(conf_path=DEFAULT_CONF_PATH):

    #setting get value
    get_value = 'PASS'

    return get_config_value(conf_path, get_value)

def get_LOG_FILE(conf_path=DEFAULT_CONF_PATH):

    #setting get value
    get_value = 'LOGFILE'

    return get_config_value(conf_path, get_value,SECTION2)

def get_LOG_LEVEL(conf_path=DEFAULT_CONF_PATH):

    #setting get value
    get_value = 'LOGLEVEL'

    return get_config_value(conf_path, get_value,SECTION2)