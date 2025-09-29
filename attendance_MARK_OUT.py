from datetime import datetime
from playwright.sync_api import sync_playwright
import jenkins
import json
import os
from locator1 import *

with sync_playwright() as p:
    host = 'https://localhost:8080'
    username = '1188464bdd0a36c568a07383c54038b983'#'hardikshettyar'
    password = '11cfdb7d49b9dea762dc0b02ec44fc5f65'#'hardik2021'
    server = jenkins.Jenkins(host, username=username, password=password)

    user = server.get_whoami()
    version = server.get_version()
    print(f"Hello {user} jenkins version is {version}")

    browser = p.chromium.launch(headless=False, args=['--start-maximized'])
    page = browser.new_page()
    page.goto('https://ellicium.spinehrm.in/login.aspx?ReturnUrl=%2f')
    print('{} is opened'.format(page.title()))
    page.click('#btnAccept')
    username = page.wait_for_selector('#txtUser')
    username.type('Ell0560')
    page.wait_for_selector('#txtPassword').type('13/10/1998')
    page.click('#btnLogin')

    page.wait_for_selector('//select[@id="ctl00_BodyContentPlaceHolder_drpSwipeCategory"]')
    selector_val = page.query_selector('//select[@id="ctl00_BodyContentPlaceHolder_drpSwipeCategory"]')
    selector_val.select_option(label='SwipeReq')
    page.wait_for_selector('#ctl00_BodyContentPlaceHolder_btnMarkOut').click()
    print("Mark out", datetime.today())
    page.wait_for_timeout(9000)