from playwright.sync_api import sync_playwright
from datetime import datetime
from locator1 import *

def handle_response(response):
    if 'https://ellicium.spinehrm.in/login.aspx' in response.url:
        status = response.status()
        data = response.text()

        print('status {} and text {}'.format(status, data))

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
    page.wait_for_selector('#ctl00_BodyContentPlaceHolder_lnkGoToDashBoard').click()

    page.on('response', lambda response: handle_response(response))
    selector_val.select_option(label='SwipeReq')
    print("Mark In",datetime.today())

    # page.wait_for_selector('#ctl00_BodyContentPlaceHolder_btnMarkIn').click()


    # page.wait_for_selector('//span[text()="Select Category"]//following::select').type('s')


    # try:
    #     # selector_dropdown = page.wait_for_selector('//select[@id="ctl00_BodyContentPlaceHolder_drpSwipeCategory"]')
    #     # # selector_dropdown.click()
    #     # # page.click('//option[text()="SwipeReq"]')
    #     # page.wait_for_selector('//span[text()="Select Category"]//following::option[text()="SwipeReq"]').click()
    # except:
    #     page.wait_for_selector('//span[text()="Select Category"]//following::select').click()
    #     page.wait_for_selector('//span[text()="Select Category"]//following::option[text()="SwipeReq"]').click()

    # page.click('#ctl00_BodyContentPlaceHolder_drpSwipeCategory')
    # page.wait_for_selector('//option[@value="1"]').click()
    # page.wait_for_selector('#ctl00_BodyContentPlaceHolder_btnMarkIn').click()
    # page.wait_for_selector('#ctl00_BodyContentPlaceHolder_lnkGoToDashBoard').click()
    # page.wait_for_selector('(//div[@id="ctl00_BodyContentPlaceHolder_pnlSwipeCategory"]//following::select//descendant::option)[2]').click()


    page.wait_for_timeout(3000)

