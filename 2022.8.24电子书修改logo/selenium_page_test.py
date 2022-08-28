
#! -*- utf-8 -*-
import re
import json
import time
from lxml import etree
from selenium import webdriver
import pymysql
driver = webdriver.Chrome()














url_list =[
    "http://127.0.0.1:5000/disclaimer",
    "http://127.0.0.1:5000/index",
    "http://127.0.0.1:5000/base_title_blog",
    "http://127.0.0.1:5000/onePageBlog",
    "http://127.0.0.1:5000/Ebooklist",


]

for item in url_list:
    driver.get(item)
    print(item)
    time.sleep(3)

driver.close()