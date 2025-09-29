import datetime

from playwright.sync_api import sync_playwright
from datetime import *
from locator1 import *

with sync_playwright() as p:
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
    page.wait_for_selector('#ctl00_BodyContentPlaceHolder_btnMarkIn').click()
    print("Mark In",datetime.today())
    page.wait_for_timeout(9000)
