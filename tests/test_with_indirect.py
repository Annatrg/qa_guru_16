import pytest
from selene import have, browser


@pytest.fixture(params=['mobile', 'desktop'])
def browser_size(request):
    if request.param == 'mobile':
        browser.config.window_width = 320
        browser.config.window_height = 569
    if request.param == 'desktop':
        browser.config.window_width = 1366
        browser.config.window_height = 768
    yield
    browser.quit()


@pytest.mark.parametrize("browser_size", ['mobile'], indirect=True)
def test_mobile(browser_size):
    browser.open("https://github.com/")
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_size", ['desktop'], indirect=True)
def test_desktop(browser_size):
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
