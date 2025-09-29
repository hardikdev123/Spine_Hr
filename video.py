from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir='./video')
    page = context.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.wait_for_timeout(3000)
    username = page.wait_for_selector('//input[@name="username"]')
    username.fill('Admin')
    password = page.wait_for_selector('//input[@name="password"]')
    password.fill('admin123')
    # login = page.wait_for_selector('//button[text()=" Login "]')
    # login.click()
    page.screenshot(path='./screenshots/login_page.png')
    page.query_selector('//button[text()=" Login "]').click()
    page.wait_for_timeout(5000)
    page.screenshot(path='./screenshots/home_page.png')
    context.close()
    page.wait_for_timeout(3000)



