import pytest
from selene import have, browser


@pytest.fixture(params=[(320, 569), (360, 640), (1366, 768), (1920, 1080)])
def browser_size(request):
    if request.param[0] < 1024:  # мобильная версия
        browser.config.window_width = request.param[0]
        browser.config.window_height = request.param[1]
        return 'mobile'
    if request.param[0] >= 1024:  # компьютерная версия
        browser.config.window_width = request.param[0]
        browser.config.window_height = request.param[1]
        return 'desktop'


def test_sign_in_mobile(browser_size):
    if browser_size == 'desktop':
        pytest.skip(reason='В этом тесте проверяется авторизация в мобильной версии браузера')
    browser.open("https://github.com/")
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_sign_in_desktop(browser_size):
    if browser_size == 'mobile':
        pytest.skip(reason='В этом тесте проверяется авторизация в компьютерная версии браузера')
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
